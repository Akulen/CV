pdf:
	pdflatex cv.tex
	bibtex cv
	pdflatex cv.tex

clean:
	rm -f cv.{4tc,aux,bbl,bib,blg,log,out,tmp,xref}
