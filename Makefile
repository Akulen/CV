pdf: cv.tex
	pdflatex cv.tex
	bibtex cv
	pdflatex cv.tex

cv.tex:
	python convert.py

clean:
	rm -f cv.{4tc,aux,bbl,blg,log,out,tmp,xref}
