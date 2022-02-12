#!/usr/bin/env python3
from os.path import splitext, basename
from utils.common.kicad_sym import KicadLibrary
import sys

files = sorted(sys.argv[1:], key=str.casefold)


print("""# Symbol Libraries

This is an unofficial collection of symbol libraries for KiCad 6.
It depends on the footprint libraries in [the footprints repository](https://github.com/kicad-unofficial/footprints).

## Symbols
""")


for file in files:
    lib = KicadLibrary.from_file(file)
    name, _ = splitext(basename(file))
    name = name.removeprefix("Vendor_")

    print(f"### {name}")
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
