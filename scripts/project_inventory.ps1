param(
    [Parameter(Mandatory=$true)][string]$ProjectPath,
    [Parameter(Mandatory=$true)][string]$OutputPath
)
$ErrorActionPreference = 'Stop'
# Read only: never serialize the input XML back to the project. XML parsing
# normalizes raw newlines in attributes (notably PicoC source code).
$resolved = (Resolve-Path -LiteralPath $ProjectPath).Path
$destination = [IO.Path]::GetFullPath($OutputPath)
if ($resolved -eq $destination) { throw 'Output must not overwrite the project.' }
[xml]$project = [IO.File]::ReadAllText($resolved)
$rows = @($project.SelectNodes('//C') | ForEach-Object {
    $node = $_
    [pscustomobject]@{
        type = $node.GetAttribute('Type')
        version = $node.GetAttribute('V')
        nio = $node.GetAttribute('Nio')
        parentType = if ($node.ParentNode -is [Xml.XmlElement]) { $node.ParentNode.GetAttribute('Type') } else { '' }
        attributes = @($node.Attributes | ForEach-Object { $_.Name } | Sort-Object -Unique)
        children = @($node.ChildNodes | Where-Object { $_ -is [Xml.XmlElement] } | ForEach-Object { $_.Name } | Sort-Object -Unique)
        connectors = @($node.SelectNodes('Co') | ForEach-Object { $_.GetAttribute('K') })
    }
})
$inventory = @($rows | Group-Object type | Sort-Object Name | ForEach-Object {
    $group = $_
    $variants = @($group.Group | Group-Object { (@($_.version, $_.nio) + $_.connectors) -join '|' } | ForEach-Object {
        [pscustomobject]@{ count = $_.Count; version = $_.Group[0].version; nio = $_.Group[0].nio; connectorKeys = @($_.Group[0].connectors) }
    })
    [pscustomobject]@{
        type = $group.Name
        count = $group.Count
        parentTypes = @($group.Group.parentType | Sort-Object -Unique)
        attributeNames = @($group.Group.attributes | Sort-Object -Unique)
        childElements = @($group.Group.children | Sort-Object -Unique)
        variants = $variants
    }
})
$result = [ordered]@{
    schemaVersion = 1
    evidence = 'Observed project structure only; not factory defaults or live verification.'
    sourceSha256 = (Get-FileHash -LiteralPath $resolved -Algorithm SHA256).Hash.ToLowerInvariant()
    controlListVersion = $project.DocumentElement.GetAttribute('Version')
    configVersion = $project.SelectSingleNode('//C[@Type="Document"]').GetAttribute('ConfigVersion')
    declaredObjects = [int]$project.SelectSingleNode('//C[@Type="Document"]').GetAttribute('NumO')
    actualObjects = $rows.Count
    typeCount = $inventory.Count
    types = $inventory
}
# Allowlist only: no titles, addresses, serials, UUIDs, passwords, pairing keys,
# code, commands, connector values, rights or project file paths are exported.
$header = [ordered]@{}
foreach ($field in $result.Keys) { if ($field -ne 'types') { $header[$field] = $result[$field] } }
$headerJson = $header | ConvertTo-Json -Compress
# One type per line keeps the reference searchable without excessive indentation.
$typeJson = @($inventory | ForEach-Object { $_ | ConvertTo-Json -Depth 12 -Compress })
$json = $headerJson.Substring(0, $headerJson.Length - 1) + ',"types":[' + "`n" + ($typeJson -join ",`n") + "`n]}" + "`n"
[IO.File]::WriteAllText($destination, $json, [Text.UTF8Encoding]::new($false))
Write-Output "Inventory: $($rows.Count) objects, $($inventory.Count) types."
