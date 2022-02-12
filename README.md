
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

Automotive qualified parts (AEC-Q100, etc) are marked with a 🚗 (car icon) in
the [symbol index] below.

The keyword `automotive` can be used to find these symbols within KiCad.

## Enclosures

Some symbols represent PCB enclosures rather than parts to be placed on the PCB.
They are marked with a 📦 (package icon) in the [symbol index] below.

Enclosure footprints define the edge cuts layer (PCB shape) and mounting holes.


## Symbol Index

This is an index of the available libraries and the symbols they contain. Each
library contains symbols for a specific vendor or manufacturer.

- [Espressif](#espressif)
- [Hammond](#hammond)
- [NXP](#nxp)
- [onsemi](#onsemi)

### Espressif

- [ESP-PROG_JTAG_Counter_Clockwise](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html)  &mdash; JTAG connector for ESP-PROG debugger, counter-clockwise pinout
- [ESP-PROG_JTAG_Odd_Even](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html)  &mdash; JTAG connector for ESP-PROG debugger, odd/even pinout
  - [ESP-PROG_JTAG_TC2050-NL](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; TC2050-NL [👣](https://github.com/kicad-unofficial/footprints#user-content-tagconnect_tc2050-nl 'Footprint: TagConnect TC2050-NL')
  - [ESP-PROG_JTAG_TC2050-NL+CLIP](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; TC2050-NL, clearance for TC2050-CLIP [👣](https://github.com/kicad-unofficial/footprints#user-content-tagconnect_tc2050-nl+clip 'Footprint: TagConnect TC2050-NL+CLIP')

### Hammond

- [1551KBK](https://www.hammfg.com/files/parts/pdf/1551KBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 80x40x20mm, black
- [1551KFLBK](https://www.hammfg.com/files/parts/pdf/1551KFLBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 80x40x20mm, black, mounting flanges
- [1551KFLGY](https://www.hammfg.com/files/parts/pdf/1551KFLGY.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 80x40x20mm, gray, mounting flanges
- [1551KGY](https://www.hammfg.com/files/parts/pdf/1551KGY.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 80x40x20mm, Gray
- [1551KRBK](https://www.hammfg.com/files/parts/pdf/1551KRBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 80x40x20mm, black, key ring
- [1551KRGY](https://www.hammfg.com/files/parts/pdf/1551KRGY.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 80x40x20mm, gray, key ring
- [1551KTBU](https://www.hammfg.com/files/parts/pdf/1551KTBU.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 80x40x20mm, translucent blue
- [1591XXLBK](https://www.hammfg.com/files/parts/pdf/1591XXLBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 86x56x36mm, black, brass inserts (lid), flame retardant
- [1591XXLFLBK](https://www.hammfg.com/files/parts/pdf/1591XXLFLBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 86x56x36mm, black, mounting flanges, brass inserts (lid), flame retardant
- [1591XXLFLGY](https://www.hammfg.com/files/parts/pdf/1591XXLFLGY.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 86x56x36mm, gray, mounting flanges, brass inserts (lid), flame retardant
- [1591XXLGY](https://www.hammfg.com/files/parts/pdf/1591XXLGY.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 86x56x36mm, gray, brass inserts (lid), flame retardant
- [1591XXLSBK](https://www.hammfg.com/files/parts/pdf/1591XXLSBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 86x56x36mm, black, self-tapping screws (lid)
- [1591XXLSFLBK](https://www.hammfg.com/files/parts/pdf/1591XXLSFLBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 86x56x36mm, black, mounting flanges, self-tapping screws (lid)
- [1591XXLTBU](https://www.hammfg.com/files/parts/pdf/1591XXLTBU.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; enclosure, 86x56x36mm, translucent blue, brass inserts (lid)

### NXP

- [74LV1T34-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) [🚗](#automotive-qualified-parts 'Automotive Qualified Part') &mdash; single supply translating buffer
  - [74LV1T34GV-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) &mdash; SC-74A [👣](https://github.com/kicad-unofficial/footprints#user-content-nxp_sot-753 'Footprint: NXP SOT-753')
  - [74LV1T34GW-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) &mdash; TSSOP-5 [👣](https://github.com/kicad-unofficial/footprints#user-content-nxp_sot-353-1 'Footprint: NXP SOT-353-1')

### onsemi

- [SZESD7104MUTAG](https://www.onsemi.com/pdf/datasheet/esd7104-d.pdf) [🚗](#automotive-qualified-parts 'Automotive Qualified Part') &mdash; ESD7104, low capacitance ESD protection diode for high speed data line, 5Vrwm, UDFN10 [👣](https://github.com/kicad-unofficial/footprints#user-content-onsemi_517bb−01 'Footprint: onsemi 517BB−01')

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

<!-- references -->

[kicad library conventions]: https://klc.kicad.org/general/g2/g2.1/

[octopart bom generator]:
https://github.com/kicad-unofficial/bom/tree/main/octopart#readme

[kicad-unofficial/footprints]: https://github.com/kicad-unofficial/footprints

[symbol index]: #symbol-index

