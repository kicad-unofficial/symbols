SYMBOL_LIBS = $(wildcard *.kicad_sym)

README.md: $(SYMBOL_LIBS) bin/generate_readme.py
	bin/generate_readme $(SYMBOL_LIBS) > "$@"
