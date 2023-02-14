build_dir := build/chapter/ch2-basic

all:
	$(shell if [ ! -e $(build_dir) ]; then mkdir -p $(build_dir); fi)
	xalatex -output-directory=build -interaction=nonstopmode -file-line-error main.tex
	biber build/main.tex
	xalatex -output-directory=build -interaction=nonstopmode -file-line-error main.tex
	xalatex -output-directory=build -interaction=nonstopmode -file-line-error main.tex

clean:
	rm -rf build

.PHONY: all clean
