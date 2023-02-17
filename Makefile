build_dir := build

main:
	$(shell if [ ! -e $(build_dir)/main ]; then mkdir -p $(build_dir)/main/chapter; fi)
	xelatex -output-directory=build/main -interaction=nonstopmode -file-line-error main.tex
	bibtex build/main/main
	xelatex -output-directory=build/main -interaction=nonstopmode -file-line-error main.tex
	xelatex -output-directory=build/main -interaction=nonstopmode -file-line-error main.tex

trans:
	$(shell if [ ! -e $(build_dir)/trans ]; then mkdir -p $(build_dir)/trans; fi)
	xelatex -output-directory=build/trans -interaction=nonstopmode -file-line-error trans.tex

clean:
	rm -rf build

.PHONY: clean
