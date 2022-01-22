# Symbol Libraries

This is an unofficial collection of symbol libraries for KiCad 6. It depends on
the footprint libraries in [the footprints repository](https://github.com/kicad-unofficial/footprints).

## Conventions

- Name the component as the part number used for ordering, excluding packing alternatives.
- Start the description with the "general" part number (usually the one used to identify the datasheet).
- End the description with the package name, if multiple are available.
- Use a border of `0.254mm` on filled shapes
- Link directly to manufacturer's datasheet (not Mouser, for example)
- For automotive qualified parts:
  - Include `automotive` and `aec` keywords
  - Include `automotive qualified` in the description
