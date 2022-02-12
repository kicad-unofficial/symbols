#!/usr/bin/env python3
from os.path import splitext, basename
from utils.common.kicad_sym import KicadLibrary
import sys

files = sorted(sys.argv[1:], key=str.casefold)


print("""# Symbol Libraries

**An unofficial collection of schematic symbols for KiCad 6.**

## Atomic Parts

All parts are "atomic" &mdash; they have a "fully-specified" symbol and an
associated footprint. The footprints are created directly from the
manufacturer's specifications and are located in the
[kicad-unofficial/footprints] repository.

Because the symbols are fully-specified, they each represent a specific part
that can be ordered from a supplier. Furthermore, they work out-of-the-box with
the [Octopart BOM generator]. An `Octopart Query` field is included where
necessary.

Generic symbols are also provided for parts that are available in more than one
package, but no generic symbol is provided without accompanying fully-specified
symbols.

For more information about "atomic" parts, "fully-specified" symbols and
"generic" symbols, please see the [KiCad Library Conventions].

## Automotive Qualified Parts

Automotive qualified parts (AEC-Q100, etc) include the text `automotive
qualified` in their description and are marked with a 🚗&nbsp; (car icon) in the
[symbol index] below.

## Enclosures

Some symbols represent PCB enclosures rather than parts to be placed on the PCB.
They are marked with a 📦&nbsp; (package icon) in the [symbol index] below.

Enclosure footprints define the edge cuts layer (PCB shape) and mounting holes.


## Symbol Index

This is an index of the available libraries and the symbols they contain. Each
library contains symbols for a specific vendor or manufacturer.
""")

for file in files:
    name, _ = splitext(basename(file).removeprefix('Vendor_'))
    print(f"- [{name}](#{name.lower()})")

for file in files:
    name, _ = splitext(basename(file).removeprefix('Vendor_'))
    lib = KicadLibrary.from_file(file)

    print(f"### {name}")
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

[kicad library conventions]: https://klc.kicad.org/general/g2/g2.1/

[octopart bom generator]:
https://github.com/kicad-unofficial/bom/tree/main/octopart#readme

[kicad-unofficial/footprints]: https://github.com/kicad-unofficial/footprints

[symbol index]: #symbol-index
""")
