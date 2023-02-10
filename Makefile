all:
	xalatex -output-directory=build -interaction=nonstopmode -file-line-error main.tex
	biber build/main.tex
	xalatex -output-directory=build -interaction=nonstopmode -file-line-error main.tex
	xalatex -output-directory=build -interaction=nonstopmode -file-line-error main.tex

clean:
	rm -rf build

.PHONY: all clean