#!/usr/bin/env python3
from os.path import splitext, basename
from utils.common.kicad_sym import KicadLibrary
import sys

files = sorted(sys.argv[1:], key=str.casefold)


print("""# Symbol Libraries

This is an unofficial collection of symbol libraries for KiCad 6. It depends on
the footprint libraries in [the footprints
repository](https://github.com/kicad-unofficial/footprints).

Each library contains symbols for a specific vendor or manufacturer. All symbols
are "fully specified", meaning that they uniquely identify a specific part with
a specific footprint.

They are designed to require no further specification once placed into the
schematic. Where necessary an [`Octopart Query` field](https://github.com/kicad-unofficial/bom/tree/main/octopart#readme) is
included such that the symbol can be used with the [Octopart BOM generator](https://github.com/kicad-unofficial/bom/tree/main/octopart).

### Enclosure Symbols

Perhaps unconventially, some of these symbols represent PCB enclosures. The
footprint of these symbols defines the edge cuts layer and mounting holes for a
PCB that is suitable for the enclosure.

## Symbol Index
""")

for file in files:
    lib = KicadLibrary.from_file(file)
    base = basename(file)
    name, _ = splitext(base)

    print(f"### {name.removeprefix('Vendor_')}")
    print()
    print(f"These symbols are contained in the [`{name}`]({base}) library.")
    print()

    for sym in lib.symbols:
        desc = sym.get_property("ki_description").value
        url = sym.get_property("Datasheet").value

        if url:
            print(f"- [{sym.name}]({url}): {desc}", )
        else:
            print(f"- {sym.name}: {desc}", )

    print()

print("""## Conventions

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
