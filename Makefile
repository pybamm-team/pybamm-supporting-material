all:pybamm.pdf 

%.pdf:%.md
	pandoc -t beamer --template my-pandoc-beamer.template $< -V theme:Warsaw --filter pandoc-citeproc -o $@

.PHONY=clean
clean:
	rm *.pdf
