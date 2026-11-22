// Read-only geometric check for native Loxone XML. No external packages.
// node blattgrenzen_pruefen.cjs project.Loxone left top right bottom [report.json]
const fs=require('node:fs');
const [file,...args]=process.argv.slice(2);
const values=args.slice(0,4).map(Number);
if(!file||values.length!==4||!values.every(Number.isFinite)||values[2]<=values[0]||values[3]<=values[1]){
  console.error('Usage: node blattgrenzen_pruefen.cjs project.Loxone left top right bottom [report.json]\nBounds must be verified for the current sheet; PaperFormat is not guessed.');process.exit(2);
}
const [left,top,right,bottom]=values,raw=fs.readFileSync(file,'utf8');
const stack=[],pages=[];let paperFormat=null;
const decode=s=>s.replace(/&(quot|apos|lt|gt|amp);/g,(_,n)=>({quot:'"',apos:"'",lt:'<',gt:'>',amp:'&'})[n]);
const tags=/<(?:!--[\s\S]*?--|\?[\s\S]*?\?|!\[CDATA\[[\s\S]*?\]\]|(?:[^>"']|"[^"]*"|'[^']*')*)>/g;
for(const m of raw.matchAll(tags)){
  const t=m[0];if(/^<[!?]/.test(t))continue;
  if(t.startsWith('</')){const name=t.slice(2,-1).trim(),n=stack.pop();if(!n||n.name!==name)throw Error('Malformed XML at '+m.index);continue;}
  const name=/^<([^\s/>]+)/.exec(t)[1],a={};
  for(const v of t.matchAll(/([^\s=]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g))a[v[1]]=decode(v[2]??v[3]);
  const node={name,a};
  if(name==='C'&&a.Type==='Document')paperFormat=a.PaperFormat;
  if(name==='C'&&a.Type==='Page'){node.page={uuid:a.U,title:a.Title,objects:[],outside:[],invalid:[],overlaps:[]};pages.push(node.page);}
  else if(name==='C'&&stack.at(-1)?.a.Type==='Page'){
    const page=stack.at(-1).page,object={uuid:a.U,type:a.Type,title:a.Title,x:+a.Px,y:+a.Py,x2:+a.Px2,y2:+a.Py2};
    page.objects.push(object);
    if(![object.x,object.y,object.x2,object.y2].every(Number.isFinite)||object.x2<=object.x||object.y2<=object.y)page.invalid.push(object);
    else if(object.x<left||object.y<top||object.x2>right||object.y2>bottom)page.outside.push(object);
  }
  if(!t.endsWith('/>'))stack.push(node);
}
if(stack.length)throw Error('Unclosed XML');
for(const page of pages)for(let i=0;i<page.objects.length;i++)for(let j=i+1;j<page.objects.length;j++){
  const a=page.objects[i],b=page.objects[j];
  if(a.x<b.x2&&a.x2>b.x&&a.y<b.y2&&a.y2>b.y)page.overlaps.push([a.uuid,b.uuid]);
}
const report={file,paperFormat,bounds:{left,top,right,bottom},pages:pages.length,objects:pages.reduce((s,p)=>s+p.objects.length,0),outside:pages.reduce((s,p)=>s+p.outside.length,0),invalid:pages.reduce((s,p)=>s+p.invalid.length,0),overlaps:pages.reduce((s,p)=>s+p.overlaps.length,0),details:pages.map(p=>({...p,objects:p.objects.length}))};
if(args[4])fs.writeFileSync(args[4],JSON.stringify(report,null,2));
console.log(JSON.stringify({...report,details:report.details.filter(p=>p.outside.length||p.invalid.length||p.overlaps.length).map(p=>({title:p.title,uuid:p.uuid,objects:p.objects,outside:p.outside.length,invalid:p.invalid.length,overlaps:p.overlaps.length}))},null,2));
process.exitCode=report.outside||report.invalid||report.overlaps?1:0;
