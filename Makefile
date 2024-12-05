SHELL := /bin/bash

pdf: cv.tex cv.bib
	pdflatex cv.tex
	bibtex cv
	pdflatex cv.tex

html: cv.bib
	python3 convert.py html

cv.tex: cv.json
	python3 convert.py pdf

cv.bib:
	python3 convert.py bib

clean:
	rm -f cv.{4tc,aux,bbl,blg,log,out,tmp,xref,tex,bib}
