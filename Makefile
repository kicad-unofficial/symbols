.PHONY: README.md
README.md: $(wildcard *.kicad_sym)
	bin/generate_readme $^ > "$@"
