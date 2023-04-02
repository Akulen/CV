pdf: cv.tex cv.bib
	pdflatex cv.tex
	bibtex cv
	pdflatex cv.tex

html:
	python convert.py html

cv.tex:
	python convert.py pdf

cv.bib:
	python convert.py bib

clean:
	rm -f cv.{4tc,aux,bbl,blg,log,out,tmp,xref}
