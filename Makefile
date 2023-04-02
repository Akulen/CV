pdf: cv.tex
	pdflatex cv.tex
	bibtex cv
	pdflatex cv.tex

html:
	python convert.py html

cv.tex:
	python convert.py

clean:
	rm -f cv.{4tc,aux,bbl,blg,log,out,tmp,xref}
