# UBC Annotated CV - in LaTeX

This is my attempt to write my CV in LaTeX

The main reasons for writing in LaTeX format are:

- Looks pretty
- Citations managed using Zotero
- Bold, italicized, etc. author names
- Auto populated number of citations
- Auto populated altmetric information

## Citations

I have a folder in Zotero for my papers, conferences, etc.

I have zotero auto update to a `.bib` file using ![Better Bib Tex](https://retorque.re/zotero-better-bibtex/)

## Create PDF

Running `createpdf.sh` should run the scripts below, and create the PDF.

### Font styles for author names

The .bib file I have auto updated is `_Weber.bib`, however, you'll notice that the `.tex` file actually calls `test.bib`. This file is created when you run `boldauthors.sh`. You will want to edit this `.sh` file to change your name, supervisor names, and student names.

### Auto populated number of citations

Using the python script `cite.py`, I have a google-scraper use my author ID number to create a json file of all of my papers. The main `.tex` file calls that number in my publications section. So you will need to edit the `cite.py` file to use your Google Scholar ID, and you will need to manually add the links to your papers. That part requires some work, but the amount of time it will save you in the future is pretty big.

### Auto populated altmetric data

Using the python script `altcite.py`, I use the altmetrics api to query a list of dois (you need to add these to the `altcite.py` file). When you run `altcite.py`, it creates the file `altcitationsvalues.tex` which is loaded in the latex file.
