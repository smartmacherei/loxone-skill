#!/usr/bin/env python3
r"""BACnet/IP-Pruefwerkzeug ohne Fremdbibliothek (YABE-Ersatz, laeuft auch ohne Adminrechte).

    py -3 bacnet_probe.py <miniserver-ip>                 Who-Is, Geraetedaten, Objektliste mit Werten
    py -3 bacnet_probe.py <ip> --write binary-output,1 1  present-value schreiben (Prioritaet 8), 'null' = freigeben
    py -3 bacnet_probe.py <ip> --cov binary-input,1 30    30 s auf COV-Benachrichtigungen warten

Verifiziert 05.09.2026 am Miniserver Gen 2 (FW 17.2.8.28): antwortet als device,0 mit den in Config
angelegten BACnet-Objekten plus network-port; unterstuetzt readProperty(Multiple),
writeProperty(Multiple), subscribeCOV(Property), reinitializeDevice, who-Is/who-Has.
Von Windows aus muss der Rechner unaufgeforderte UDP-Antworten annehmen duerfen (Firewall) -
im Zweifel von einem Linux-Host im selben Netz starten. Nutzt Port 47808 als Quellport.
"""
import argparse
import socket
import struct
import sys
import time

OBJT = {0: "analog-input", 1: "analog-output", 2: "analog-value", 3: "binary-input", 4: "binary-output",
        5: "binary-value", 8: "device", 13: "multi-state-input", 14: "multi-state-output", 19: "multi-state-value",
        56: "network-port", 17: "schedule", 15: "notification-class"}
PROPS = {"object-name": 77, "object-type": 79, "present-value": 85, "description": 28, "units": 117, "object-list": 76,
         "vendor-name": 121, "vendor-identifier": 120, "model-name": 70, "firmware-revision": 44,
         "application-software-version": 12, "protocol-services-supported": 97, "protocol-object-types-supported": 96,
         "system-status": 112, "active-text": 4, "inactive-text": 46, "polarity": 84, "out-of-service": 81,
         "status-flags": 111, "location": 58, "max-apdu-length-accepted": 62, "segmentation-supported": 107,
         "protocol-revision": 139, "cov-increment": 22}
SERVICES = ["acknowledgeAlarm", "confirmedCOVNotification", "confirmedEventNotification", "getAlarmSummary",
            "getEnrollmentSummary", "subscribeCOV", "atomicReadFile", "atomicWriteFile", "addListElement",
            "removeListElement", "createObject", "deleteObject", "readProperty", "readPropertyConditional",
            "readPropertyMultiple", "writeProperty", "writePropertyMultiple", "deviceCommunicationControl",
            "confirmedPrivateTransfer", "confirmedTextMessage", "reinitializeDevice", "vtOpen", "vtClose", "vtData",
            "authenticate", "requestKey", "i-Am", "i-Have", "unconfirmedCOVNotification", "unconfirmedEventNotification",
            "unconfirmedPrivateTransfer", "unconfirmedTextMessage", "timeSynchronization", "who-Has", "who-Is",
            "readRange", "utcTimeSynchronization", "lifeSafetyOperation", "subscribeCOVProperty", "getEventInformation",
            "writeGroup", "subscribeCOVPropertyMultiple", "confirmedCOVNotificationMultiple",
            "unconfirmedCOVNotificationMultiple"]


def tag(buf, i):
    b = buf[i]
    tn, cls, lvt = b >> 4, (b >> 3) & 1, b & 7
    i += 1
    if tn == 15:
        tn = buf[i]
        i += 1
    if lvt == 6:
        return "open", tn, cls, None, i
    if lvt == 7:
        return "close", tn, cls, None, i
    if cls == 0 and tn == 1:
        return "data", tn, cls, bool(lvt), i          # boolean: Wert im Laengenfeld
    ln = lvt
    if lvt == 5:
        ln = buf[i]
        i += 1
        if ln == 254:
            ln = struct.unpack(">H", buf[i:i + 2])[0]
            i += 2
        elif ln == 255:
            ln = struct.unpack(">I", buf[i:i + 4])[0]
            i += 4
    return "data", tn, cls, buf[i:i + ln], i + ln


def bits(d):
    unused = d[0]
    out = []
    for k, byte in enumerate(d[1:]):
        for j in range(8):
            if byte & (0x80 >> j):
                out.append(k * 8 + j)
    return [x for x in out if x < (len(d) - 1) * 8 - unused]


def appval(tn, d):
    if isinstance(d, bool):
        return d
    if tn == 0:
        return None
    if tn == 2:
        return int.from_bytes(d, "big")
    if tn == 3:
        return int.from_bytes(d, "big", signed=True)
    if tn == 4:
        return struct.unpack(">f", d)[0]
    if tn == 5:
        return struct.unpack(">d", d)[0]
    if tn == 7:
        return d[1:].decode("utf-8", "replace") if d[:1] == b"\x00" else "str(enc%d):%s" % (d[0], d[1:].hex())
    if tn == 8:
        return "bits:" + ",".join(str(x) for x in bits(d))
    if tn == 9:
        return "enum:%d" % int.from_bytes(d, "big")
    if tn == 12:
        v = int.from_bytes(d, "big")
        return "%s,%d" % (OBJT.get(v >> 22, str(v >> 22)), v & 0x3FFFFF)
    return "tag%d:%s" % (tn, d.hex())


def npdu_skip(b, i):
    ctrl = b[i + 1]
    i += 2
    if ctrl & 0x20:
        i += 3 + b[i + 2]
    if ctrl & 0x08:
        i += 3 + b[i + 2]
    if ctrl & 0x20:
        i += 1
    return i


def decode_values(b, i, end):
    out = []
    while i < end:
        k, tn, cls, d, i = tag(b, i)
        if k in ("open", "close"):
            continue
        out.append(appval(tn, d) if cls == 0 else "ctx%d:%s" % (tn, d.hex() if isinstance(d, bytes) else d))
    return out


def objid_bytes(name: str) -> bytes:
    t, inst = name.rsplit(",", 1)
    tnum = {v: k for k, v in OBJT.items()}.get(t)
    if tnum is None:
        tnum = int(t)
    return struct.pack(">I", (tnum << 22) | int(inst))


class Client:
    def __init__(self, host, timeout=3.0):
        self.host, self.inv = host, 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.s.bind(("0.0.0.0", 47808))
        except OSError as e:
            print("Port 47808 belegt (%s) - nehme freien Port; Broadcast-Antworten kommen dann evtl. nicht an" % e)
            self.s.bind(("0.0.0.0", 0))
        self.s.settimeout(timeout)

    def send(self, apdu, dst=None, broadcast=False):
        npdu = bytes([0x01, 0x20, 0xFF, 0xFF, 0x00, 0xFF]) if broadcast else bytes([0x01, 0x04])
        pkt = bytes([0x81, 0x0B if broadcast else 0x0A]) + struct.pack(">H", 4 + len(npdu) + len(apdu)) + npdu + apdu
        self.s.sendto(pkt, dst or (self.host, 47808))

    def recv(self, invoke=None, t=None):
        t0 = time.time()
        while time.time() - t0 < (t or self.s.gettimeout()):
            try:
                d, a = self.s.recvfrom(4096)
            except socket.timeout:
                return None, None
            i = npdu_skip(d, 4)
            if invoke is None or (len(d) > i + 1 and d[i + 1] == invoke):
                return d[i:], a
        return None, None

    def who_is(self):
        found = {}
        for dst, bc in ((("255.255.255.255", 47808), True), ((self.host, 47808), False)):
            self.send(bytes([0x10, 0x08]), dst, broadcast=bc)
            t0 = time.time()
            while time.time() - t0 < 2.5:
                apdu, a = self.recv(t=2.5)
                if apdu is None:
                    break
                if apdu[0] >> 4 == 1 and apdu[1] == 0:
                    vals = decode_values(apdu, 2, len(apdu))
                    found[a[0]] = vals
        return found

    def read(self, obj, prop, index=None):
        self.inv = (self.inv + 1) & 0xFF
        apdu = bytes([0x00, 0x05, self.inv, 0x0C, 0x0C]) + objid_bytes(obj) + bytes([0x19, PROPS.get(prop, prop)])
        if index is not None:
            apdu += bytes([0x29, index])
        self.send(apdu)
        r, _ = self.recv(self.inv)
        if r is None:
            return "timeout", None
        t = r[0] >> 4
        if t == 3:
            vals = decode_values(r, 3, len(r))
            return "ok", vals[2:] if len(vals) > 2 else vals
        if t == 5:
            e = decode_values(r, 3, len(r))
            return "error", "class %s code %s" % (e[0], e[1]) if len(e) > 1 else e
        return "reject/abort", r.hex()

    def write_pv(self, obj, value, prio=8):
        self.inv = (self.inv + 1) & 0xFF
        v = b"\x00" if value is None else (bytes([0x91, int(value)]) if "binary" in obj else b"\x44" + struct.pack(">f", float(value)))
        apdu = bytes([0x00, 0x05, self.inv, 0x0F, 0x0C]) + objid_bytes(obj) + bytes([0x19, 85, 0x3E]) + v + bytes([0x3F, 0x49, prio])
        self.send(apdu)
        r, _ = self.recv(self.inv)
        if r is None:
            return "timeout"
        return "SimpleACK" if r[0] >> 4 == 2 else "error " + r.hex()

    def subscribe_cov(self, obj, lifetime=60, pid=7):
        self.inv = (self.inv + 1) & 0xFF
        apdu = bytes([0x00, 0x05, self.inv, 0x05, 0x09, pid, 0x1C]) + objid_bytes(obj)
        if lifetime:
            apdu += bytes([0x29, 0x00, 0x39, lifetime])
        self.send(apdu)
        r, _ = self.recv(self.inv)
        return "SimpleACK" if r is not None and r[0] >> 4 == 2 else ("timeout" if r is None else "error " + r.hex())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("host")
    ap.add_argument("--write", nargs=2, metavar=("OBJ", "VALUE"), help="present-value schreiben, z.B. binary-output,1 1 | null")
    ap.add_argument("--cov", nargs=2, metavar=("OBJ", "SECONDS"), help="COV abonnieren und Benachrichtigungen zeigen")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    c = Client(args.host)

    if args.write:
        obj, val = args.write
        print("write", obj, "=", val, "->", c.write_pv(obj, None if val.lower() == "null" else val))
        print("present-value jetzt:", c.read(obj, "present-value"))
        return
    if args.cov:
        obj, secs = args.cov
        print("subscribeCOV", obj, "->", c.subscribe_cov(obj, int(secs)))
        t0 = time.time()
        while time.time() - t0 < int(secs):
            r, a = c.recv(t=1)
            if r is not None and r[0] >> 4 == 1 and r[1] in (2,):
                vals = decode_values(r, 2, len(r))
                print("%6.3f s  COV von %s: %s" % (time.time() - t0, a[0], vals))
        print("cancel ->", c.subscribe_cov(obj, 0))
        return

    found = c.who_is()
    if not found:
        print("kein I-Am - Server aus, anderer Port, oder Firewall verwirft die Antwort")
        return
    for ip, vals in found.items():
        dev = vals[0]
        print("I-Am von %s: %s (max APDU %s, Segmentierung %s, Vendor %s)" % (ip, dev, vals[1], vals[2], vals[3]))
        for p in ("object-name", "vendor-name", "model-name", "firmware-revision", "application-software-version",
                  "protocol-revision", "system-status", "location", "description"):
            st, v = c.read(dev, p)
            print("  %-30s %s" % (p, v if st == "ok" else st + " " + str(v)))
        st, v = c.read(dev, "protocol-services-supported")
        if st == "ok":
            print("  %-30s %s" % ("services", ", ".join(SERVICES[i] if i < len(SERVICES) else str(i) for i in
                                                        [int(x) for x in str(v[0]).split(":")[1].split(",") if x])))
        st, v = c.read(dev, "protocol-object-types-supported")
        if st == "ok":
            print("  %-30s %s" % ("object types", ", ".join(OBJT.get(i, str(i)) for i in
                                                            [int(x) for x in str(v[0]).split(":")[1].split(",") if x])))
        st, objs = c.read(dev, "object-list")
        if st != "ok":
            st, n = c.read(dev, "object-list", 0)
            objs = [c.read(dev, "object-list", k)[1][0] for k in range(1, int(n[-1]) + 1)]
        print("  object-list (%d): %s" % (len(objs), objs))
        for o in objs:
            row = [str(o)]
            for p in ("object-name", "present-value", "units", "polarity", "status-flags", "out-of-service"):
                st, v = c.read(o, p)
                if st == "ok":
                    row.append("%s=%s" % (p, v[0] if len(v) == 1 else v))
            print("    " + "  ".join(row))


if __name__ == "__main__":
    main()
