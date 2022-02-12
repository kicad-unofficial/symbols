# Symbol Libraries

This is an unofficial collection of symbol libraries for KiCad 6.

The footprints used by these symbols are in the [footprints] repository.

[footprints]: https://github.com/kicad-unofficial/footprints

## Conventions

These symbols are intended to require no further specification once placed into
the schematic.

Parts are only included if their symbol can be "fully-specified". This means
each symbol uniquely identifies a specific part that can be ordered from a
supplier. Generic (non-fully-specified) symbols are also provided for parts that
are available in multiple footprints.

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

- [Hammond](#hammond)
- [NXP](#nxp)
- [onsemi](#onsemi)
### Hammond

- [1551KBK](https://www.hammfg.com/files/parts/pdf/1551KBK.pdf) 📦&nbsp; &mdash; enclosure, 80x40x20mm, black
- [1551KFLBK](https://www.hammfg.com/files/parts/pdf/1551KFLBK.pdf) 📦&nbsp; &mdash; enclosure, 80x40x20mm, black, mounting flanges
- [1551KFLGY](https://www.hammfg.com/files/parts/pdf/1551KFLGY.pdf) 📦&nbsp; &mdash; enclosure, 80x40x20mm, gray, mounting flanges
- [1551KGY](https://www.hammfg.com/files/parts/pdf/1551KGY.pdf) 📦&nbsp; &mdash; enclosure, 80x40x20mm, Gray
- [1551KRBK](https://www.hammfg.com/files/parts/pdf/1551KRBK.pdf) 📦&nbsp; &mdash; enclosure, 80x40x20mm, black, key ring
- [1551KRGY](https://www.hammfg.com/files/parts/pdf/1551KRGY.pdf) 📦&nbsp; &mdash; enclosure, 80x40x20mm, gray, key ring
- [1551KTBU](https://www.hammfg.com/files/parts/pdf/1551KTBU.pdf) 📦&nbsp; &mdash; enclosure, 80x40x20mm, translucent blue
- [1591XXLBK](https://www.hammfg.com/files/parts/pdf/1591XXLBK.pdf) 📦&nbsp; &mdash; enclosure, 86x56x36mm, black, brass screw inserts (lid), flame retardant
- [1591XXLFLBK](https://www.hammfg.com/files/parts/pdf/1591XXLFLBK.pdf) 📦&nbsp; &mdash; enclosure, 86x56x36mm, black, mounting flanges, brass screw inserts (lid), flame retardant
- [1591XXLFLGY](https://www.hammfg.com/files/parts/pdf/1591XXLFLGY.pdf) 📦&nbsp; &mdash; enclosure, 86x56x36mm, gray, mounting flanges, brass screw inserts (lid), flame retardant
- [1591XXLGY](https://www.hammfg.com/files/parts/pdf/1591XXLGY.pdf) 📦&nbsp; &mdash; enclosure, 86x56x36mm, gray, brass screw inserts (lid), flame retardant
- [1591XXLSBK](https://www.hammfg.com/files/parts/pdf/1591XXLSBK.pdf) 📦&nbsp; &mdash; enclosure, 86x56x36mm, black, self-tapping screws (lid)
- [1591XXLSFLBK](https://www.hammfg.com/files/parts/pdf/1591XXLSFLBK.pdf) 📦&nbsp; &mdash; enclosure, 86x56x36mm, black, mounting flanges, self-tapping screws (lid)
- [1591XXLTBU](https://www.hammfg.com/files/parts/pdf/1591XXLTBU.pdf) 📦&nbsp; &mdash; enclosure, 86x56x36mm, translucent blue, brass screw inserts (lid)

### NXP

- [74LV1T34-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) 🚗&nbsp; &mdash; single supply translating buffer, automotive qualified
  - [74LV1T34GV-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) &mdash; SC-74A
  - [74LV1T34GW-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) &mdash; TSSOP-5

### onsemi

- [SZESD7104MUTAG](https://www.onsemi.com/pdf/datasheet/esd7104-d.pdf) 🚗&nbsp; &mdash; ESD7104, low capacitance ESD protection diode for high speed data line, 5Vrwm, automotive qualified, UDFN10

## Notes for Symbol Creators

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

