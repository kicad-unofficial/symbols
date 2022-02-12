# Symbol Libraries

This is an unofficial collection of symbol libraries for KiCad 6. It depends on
the footprint libraries in [the footprints
repository](https://github.com/kicad-unofficial/footprints).

## Symbols

Symbols are organized into libraries by manufacturer/vendor. All symbols are
"fully specified", meaning that they uniquely identify a specific part with a
specific footprint.

### Enclosure Symbols

Perhaps unconventially, some of these symbols represent PCB enclosures. The
footprint of these symbols defines the edge cuts layer and mounting holes for a
PCB that is suitable for the enclosure.

### Hammond

These symbols are contained in the [`Vendor_Hammond`](Vendor_Hammond.kicad_sym) library.

- [1551KBK](https://www.hammfg.com/files/parts/pdf/1551KBK.pdf): 1551 Series Enclosure, 80x40x20mm, Black
- [1551KFLBK](https://www.hammfg.com/files/parts/pdf/1551KFLBK.pdf): 1551 Series Enclosure, 80x40x20mm, Black, Mounting Flanges
- [1551KFLGY](https://www.hammfg.com/files/parts/pdf/1551KFLGY.pdf): 1551 Series Enclosure, 80x40x20mm, Gray, Mounting Flanges
- [1551KGY](https://www.hammfg.com/files/parts/pdf/1551KGY.pdf): 1551 Series Enclosure, 80x40x20mm, Gray
- [1551KRBK](https://www.hammfg.com/files/parts/pdf/1551KRBK.pdf): 1551 Series Enclosure, 80x40x20mm, Black, Key Ring
- [1551KRGY](https://www.hammfg.com/files/parts/pdf/1551KRGY.pdf): 1551 Series Enclosure, 80x40x20mm, Gray, Key Ring
- [1551KTBU](https://www.hammfg.com/files/parts/pdf/1551KTBU.pdf): 1551 Series Enclosure, 80x40x20mm, Translucent Blue
- [1591XXLBK](https://www.hammfg.com/files/parts/pdf/1591XXLBK.pdf): 1591XX Series Enclosure, 86x56x36mm, Black, Brass Screw Inserts (Lid), Flame Retardant
- [1591XXLFLBK](https://www.hammfg.com/files/parts/pdf/1591XXLFLBK.pdf): 1591XX Series Enclosure, 86x56x36mm, Black, Mounting Flanges, Brass Screw Inserts (Lid), Flame Retardant
- [1591XXLFLGY](https://www.hammfg.com/files/parts/pdf/1591XXLFLGY.pdf): 1591XX Series Enclosure, 86x56x36mm, Gray, Mounting Flanges, Brass Screw Inserts (Lid), Flame Retardant
- [1591XXLGY](https://www.hammfg.com/files/parts/pdf/1591XXLGY.pdf): 1591XX Series Enclosure, 86x56x36mm, Gray, Brass Screw Inserts (Lid), Flame Retardant
- [1591XXLSBK](https://www.hammfg.com/files/parts/pdf/1591XXLSBK.pdf): 1591XX Series Enclosure, 86x56x36mm, Black, Self-Tapping Screws (Lid)
- [1591XXLSFLBK](https://www.hammfg.com/files/parts/pdf/1591XXLSFLBK.pdf): 1591XX Series Enclosure, 86x56x36mm, Black, Mounting Flanges, Self-Tapping Screws (Lid)
- [1591XXLTBU](https://www.hammfg.com/files/parts/pdf/1591XXLTBU.pdf): 1591XX Series Enclosure, 86x56x36mm, Translucent Blue, Brass Screw Inserts (Lid)

### NXP

These symbols are contained in the [`Vendor_NXP`](Vendor_NXP.kicad_sym) library.

- [74LV1T34-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf): single supply translating buffer, automotive qualified
- [74LV1T34GV-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf): 74LV1T34-Q100, single supply translating buffer, automotive qualified, SC-74A
- [74LV1T34GW-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf): 74LV1T34-Q100, single supply translating buffer, automotive qualified, TSSOP-5

### onsemi

These symbols are contained in the [`Vendor_onsemi`](Vendor_onsemi.kicad_sym) library.

- [SZESD7104MUTAG](https://www.onsemi.com/pdf/datasheet/esd7104-d.pdf): ESD7104, low capacitance ESD protection diode for high speed data line, 5Vrwm, automotive qualified, UDFN10

## Conventions

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

