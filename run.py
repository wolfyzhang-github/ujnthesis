#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shutil, sys, subprocess,  os

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)
		print(path + " do not exist, will creat one.")
	else:
		print(path + " already exists, use it.")

def xelatex_compile(doc):
    subprocess.call(["xelatex", "-output-directory=build\\" + doc, "-interaction=nonstopmode", "-file-line-error", doc + ".tex"])

def bibtex_compile(doc):
    subprocess.call(["bibtex", "build\\main\\" + doc + ".aux"])

def run(doc):
    if doc == "main":
        mkdir("build\\main\\chapter")
        xelatex_compile(doc)
        bibtex_compile(doc)
        xelatex_compile(doc)
        xelatex_compile(doc)
    elif doc == "trans":
        mkdir("build\\trans")
        xelatex_compile(doc)

def clean():
    if (os.path.exists("build")):
        shutil.rmtree("build")
        print("workspace is clear now")
    else :
        print("workspace is already clear")

if len(sys.argv) > 1 and sys.argv[1] == "main":
    doc = "main"
    run(doc)
elif len(sys.argv) > 1 and sys.argv[1] == "trans":
    doc = "trans"
    run(doc)
elif len(sys.argv) > 1 and sys.argv[1] == "clean":
    clean()
else :
    print("Usage: python run.py <option>, and the option can be main or trans or clean.")
