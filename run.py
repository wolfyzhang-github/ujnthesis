import subprocess

def xalatex_compile():
    subprocess.call(["xelatex", "-output-directory=build", "-interaction=nonstopmode", "-file-line-error", "main.tex"])

def bibtex_compile():
    subprocess.call(["bibtex", "build/main.aux"])

def run():
    xalatex_compile()
    bibtex_compile()
    xalatex_compile()
    xalatex_compile()
