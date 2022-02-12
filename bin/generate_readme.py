#!/usr/bin/env python3
from os.path import splitext, basename
from utils.common.kicad_sym import KicadLibrary
import sys

files = sorted(sys.argv[1:], key=str.casefold)


print("""# Symbol Libraries

This is an unofficial collection of symbol libraries for KiCad 6.

The footprints used by these symbols are in the [footprints] repository.

[footprints]: https://github.com/kicad-unofficial/footprints

## Conventions

These symbols are intended to require no further specification once placed into
the schematic.

To that end, parts are only included if their symbol can be "fully-specified",
meaning that it uniquely identifies a specific part that can be ordered from a
supplier. Generic (non-fully-specified) symbols _are_ also provided for parts
that are available in multiple footprints.

Where appropriate, an `Octopart Query` field is added for use with the [Octopart
BOM generator].

[octopart bom generator]:
https://github.com/kicad-unofficial/bom/tree/main/octopart#readme

### Automotive Qualified Parts

Automotive qualified parts (AEC-Q100, etc) include the text `automotive
qualified` in their description and are marked with a 🚗&nbsp; (car) icon in the
[symbol index](#symbol-index) below.

### Enclosure Symbols

Some symbols represent PCB enclosures rather than parts to be placed on the PCB.
They are marked with a 📦&nbsp; (package) icon in the [symbol index] below.

The footprint of these symbols defines the edge cuts layer and mounting holes
for the PCB.

## Symbol Index

This is an index of the available libraries and the symbols they contain. Each
library contains symbols for a specific vendor or manufacturer.
""")

for file in files:
    lib = KicadLibrary.from_file(file)
    base = basename(file)
    name, _ = splitext(base)

    print(f"### {name.removeprefix('Vendor_')}")
    # print()
    # print(f"These symbols are contained in the [`{name}`]({base}) library.")
    print()

    for sym in lib.symbols:
        if sym.extends:
            continue

        desc = sym.get_property("ki_description").value
        url = sym.get_property("Datasheet").value

        icon = ""
        if "automotive" in desc:
            icon = "🚗&nbsp;"
        if "enclosure" in desc:
            icon += "📦&nbsp;"

        print(f"- [{sym.name}]({url}) {icon} &mdash; {desc}")

        for child in lib.symbols:
            if child.extends == sym.name:
                childDesc = child.get_property("ki_description").value
                childDesc = childDesc.replace(sym.name,  "")
                childDesc = childDesc.replace(desc,  "")
                childDesc = childDesc.removeprefix(sym.name).strip(", ")
                childURL = child.get_property("Datasheet").value
                print(f"  - [{child.name}]({childURL}) &mdash; {childDesc}")

    print()

print("""## Notes for Symbol Creators

- Name the component as the part number used for ordering, excluding packing alternatives.
- Start the description with the "general" part number (usually the one used to identify the datasheet).
- Prefer symbols that are easy to layout in schematics over symbols that match pin layouts.
- End the description with the package name, if multiple are available.
- Use a border of `0.254mm` on filled shapes
- Link directly to manufacturer's datasheet (not Mouser, for example)
- Include an [`Octopart Query` field](https://github.com/kicad-unofficial/bom/tree/main/octopart#readme), wherever possible
- For automotive qualified parts:
  - Include `automotive` and `aec` keywords
  - Include `automotive qualified` in the description
""")
