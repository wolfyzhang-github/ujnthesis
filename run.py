#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shutil, sys, subprocess, glob, os

def mkdir(path):
    os.makedirs(path)

def xalatex_compile():
    subprocess.call(["xelatex", "-output-directory=build", "-interaction=nonstopmode", "-file-line-error", "main.tex"])

def bibtex_compile():
    subprocess.call(["bibtex", "build/main.aux"])

def run():
    mkdir("build\\chapter\\ch2-basic")
    xalatex_compile()
    bibtex_compile()
    xalatex_compile()
    xalatex_compile()

def clean():
    for file in glob.glob("build"):
        shutil.rmtree(file)

if len(sys.argv) > 1 and sys.argv[1] == "clean":
    clean()
else:
    run()
