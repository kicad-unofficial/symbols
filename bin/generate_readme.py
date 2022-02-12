#!/usr/bin/env python3
import functools
import os
from utils.common.kicad_sym import KicadLibrary
import sys

files = sorted(sys.argv[1:], key=str.casefold)


def symbol_cmp(a, b):
    a = a.name.lower()
    b = b.name.lower()

    if a.startswith(b):
        return +1
    if b.startswith(a):
        return -1

    return (a > b) - (a < b)


def footprint_markdown(sym):
    if "enclosure" in sym.get_property("ki_description").value.lower():
        return ""

    fp = sym.get_property("Footprint").value
    if not fp.startswith("Vendor_"):
        return ""

    lib, fp = fp.split(":")
    lib = lib.removeprefix("Vendor_")
    fp = fp.removeprefix(lib)
    fp = fp.replace("_", " ")
    fp = fp.strip(", ")

    anchor = f"user-content-{lib}_{fp}".lower()

    return f"[👣](https://github.com/kicad-unofficial/footprints#{anchor} 'Footprint: {lib} {fp}')"


def child_description(parent, child):
    p = parent.get_property("ki_description").value
    c = child.get_property("ki_description").value

    c = c.replace(parent.name, "")
    c = c.replace(p, "")
    c = c.removeprefix(sym.name)
    c = c.strip(", ")

    return c


print("""
<!-- THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT! -->

# Symbol Libraries

An unofficial collection of schematic symbols for KiCad 6.

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
qualified` in their description and are marked with a 🚗 (car icon) in the
[symbol index] below.

## Enclosures

Some symbols represent PCB enclosures rather than parts to be placed on the PCB.
They are marked with a 📦 (package icon) in the [symbol index] below.

Enclosure footprints define the edge cuts layer (PCB shape) and mounting holes.


## Symbol Index

This is an index of the available libraries and the symbols they contain. Each
library contains symbols for a specific vendor or manufacturer.
""")

for file in files:
    name, _ = os.path.splitext(os.path.basename(file).removeprefix('Vendor_'))
    print(f"- [{name}](#{name.lower()})")

print()

for file in files:
    name, _ = os.path.splitext(os.path.basename(file).removeprefix('Vendor_'))
    lib = KicadLibrary.from_file(file)

    print(f"### {name}")
    print()

    symbols = lib.symbols
    symbols.sort(key=functools.cmp_to_key(symbol_cmp))

    for sym in lib.symbols:
        if sym.extends:
            continue

        desc = sym.get_property("ki_description").value
        url = sym.get_property("Datasheet").value
        fp = footprint_markdown(sym)

        item = f"- [{sym.name}]({url}) "

        if "automotive" in desc.lower():
            item += "[🚗](#automotive-qualified-parts 'Automotive Qualified Part')"
        if "enclosure" in desc.lower():
            item += "[📦](#enclosures 'PCB Enclosure')"

        item += f" &mdash; {desc}"

        if fp:
            item += f" {fp}"

        print(item)

        for child in lib.symbols:
            if child.extends == sym.name:
                child_desc = child_description(sym, child)
                child_url = child.get_property("Datasheet").value
                child_fp = footprint_markdown(child)

                item = f"  - [{child.name}]({child_url}) &mdash; {child_desc}"
                if child_fp != fp:
                    item += f" {child_fp}"

                print(item)

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

<!-- references -->

[kicad library conventions]: https://klc.kicad.org/general/g2/g2.1/

[octopart bom generator]:
https://github.com/kicad-unofficial/bom/tree/main/octopart#readme

[kicad-unofficial/footprints]: https://github.com/kicad-unofficial/footprints

[symbol index]: #symbol-index
""")
