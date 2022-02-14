
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
package (always alongside the fully-specified symbols), and in some other
special cases.

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

- [ESP-PROG JTAG <sub>CCW</sub>](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; ESP-PROG JTAG header • counter-clockwise pinout
- [ESP-PROG JTAG <sub>O/E</sub>](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; ESP-PROG JTAG header • odd/even pinout
  - [ESP-PROG JTAG TC2050-IDC-NL](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; use TC2050-IDC-NL cable [👣](https://github.com/kicad-unofficial/footprints#user-content-tagconnect_tc2050-nl 'Footprint: TagConnect TC2050-NL')
  - [ESP-PROG JTAG TC2050-IDC-NL+CLIP](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; use TC2050-IDC-NL cable and clip [👣](https://github.com/kicad-unofficial/footprints#user-content-tagconnect_tc2050-nl+clip 'Footprint: TagConnect TC2050-NL+CLIP')
- [ESP-PROG Program <sub>CCW</sub>](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; ESP-PROG programming header • counter-clockwise pinout
- [ESP-PROG Program <sub>O/E</sub>](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; ESP-PROG programming header • odd/even pinout
  - [ESP-PROG Program TC2030-IDC-NL](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; use TC2030-IDC-NL cable [👣](https://github.com/kicad-unofficial/footprints#user-content-tagconnect_tc2030-nl 'Footprint: TagConnect TC2030-NL')
  - [ESP-PROG Program TC2030-IDC-NL+CLIP](https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) &mdash; use TC2030-IDC-NL cable and clip [👣](https://github.com/kicad-unofficial/footprints#user-content-tagconnect_tc2030-nl+clip 'Footprint: TagConnect TC2030-NL+CLIP')
- [ESP32-WROVER](https://www.espressif.com/sites/default/files/documentation/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf) &mdash; module • ESP32-D0WD-V3 dual core • 240MHz • 802.11b/g/n • bluetooth/BLE • 3.0-3.6V

### Hammond

- [1551KBK](https://www.hammfg.com/files/parts/pdf/1551KBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 80×40×20mm • abs • black
- [1551KRBK](https://www.hammfg.com/files/parts/pdf/1551KRBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 80×40×20mm • abs • black • key ring
- [1551KFLBK](https://www.hammfg.com/files/parts/pdf/1551KFLBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 80×40×20mm • abs • black • mounting flanges
- [1551KGY](https://www.hammfg.com/files/parts/pdf/1551KGY.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 80×40×20mm • abs • gray
- [1551KRGY](https://www.hammfg.com/files/parts/pdf/1551KRGY.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 80×40×20mm • abs • gray • key ring
- [1551KFLGY](https://www.hammfg.com/files/parts/pdf/1551KFLGY.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 80×40×20mm • abs • gray • mounting flanges
- [1551KTBU](https://www.hammfg.com/files/parts/pdf/1551KTBU.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 80×40×20mm • abs • translucent blue
- [1591XXLBK](https://www.hammfg.com/files/parts/pdf/1591XXLBK.pdf) [📦](#enclosures 'PCB Enclosure') [🔥](#enclosures 'Flame Retardant') &mdash; 86×56×36mm • abs • black • brass lid screw inserts
- [1591XXLFLBK](https://www.hammfg.com/files/parts/pdf/1591XXLFLBK.pdf) [📦](#enclosures 'PCB Enclosure') [🔥](#enclosures 'Flame Retardant') &mdash; 86×56×36mm • abs • black • brass lid screw inserts • mounting flanges
- [1591XXLSBK](https://www.hammfg.com/files/parts/pdf/1591XXLSBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 86×56×36mm • abs • black • self-tapping lid screws
- [1591XXLSFLBK](https://www.hammfg.com/files/parts/pdf/1591XXLSFLBK.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 86×56×36mm • abs • black • self-tapping lid screws • mounting flanges
- [1591XXLGY](https://www.hammfg.com/files/parts/pdf/1591XXLGY.pdf) [📦](#enclosures 'PCB Enclosure') [🔥](#enclosures 'Flame Retardant') &mdash; 86×56×36mm • abs • gray • brass lid screw inserts
- [1591XXLFLGY](https://www.hammfg.com/files/parts/pdf/1591XXLFLGY.pdf) [📦](#enclosures 'PCB Enclosure') [🔥](#enclosures 'Flame Retardant') &mdash; 86×56×36mm • abs • gray • brass lid screw inserts • mounting flanges
- [1591XXLTBU](https://www.hammfg.com/files/parts/pdf/1591XXLTBU.pdf) [📦](#enclosures 'PCB Enclosure') &mdash; 86×56×36mm • abs • translucent blue • brass lid screw inserts

### NXP

- [74LV1T34-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) [🚗](#automotive-qualified-parts 'Automotive Qualified Part') &mdash; single supply translating buffer • 5V<sub>max</sub>
  - [74LV1T34GV-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) &mdash; SC-74A [👣](https://github.com/kicad-unofficial/footprints#user-content-nxp_sot753 'Footprint: NXP SOT753')
  - [74LV1T34GW-Q100](https://assets.nexperia.com/documents/data-sheet/74LV1T34_Q100.pdf) &mdash; TSSOP-5 [👣](https://github.com/kicad-unofficial/footprints#user-content-nxp_sot353-1 'Footprint: NXP SOT353-1')

### onsemi

- [ESD7104](https://www.onsemi.com/pdf/datasheet/esd7104-d.pdf) &mdash; low capacitance ESD protection diode for high speed data line • 5V<sub>rwm</sub>
  - [ESD7104MUTAG](https://www.onsemi.com/pdf/datasheet/esd7104-d.pdf) &mdash; UDFN10 [👣](https://github.com/kicad-unofficial/footprints#user-content-onsemi_517bb-01 'Footprint: onsemi 517BB-01')
  - [SZESD7104MTWTAG](https://www.onsemi.com/pdf/datasheet/esd7104-d.pdf) [🚗](#automotive-qualified-parts 'Automotive Qualified Part') &mdash; WDFNW10 [👣](https://github.com/kicad-unofficial/footprints#user-content-onsemi_515ah 'Footprint: onsemi 515AH')
  - [SZESD7104MUTAG](https://www.onsemi.com/pdf/datasheet/esd7104-d.pdf) [🚗](#automotive-qualified-parts 'Automotive Qualified Part') &mdash; UDFN10 [👣](https://github.com/kicad-unofficial/footprints#user-content-onsemi_517bb-01 'Footprint: onsemi 517BB-01')

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

