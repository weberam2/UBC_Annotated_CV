# UBC Annotated CV - in LaTeX

This is my attempt to write my CV in LaTeX

The main reasons for writing in LaTeX format are:

- Looks pretty
- Citations managed using Zotero
- Bold, italicized, etc. author names
- Auto populated number of citations

## Citations

I have a folder in Zotero for my papers, conferences, etc.

I have the folder auto update to a `.bib` file using ![Better Bib Tex](https://retorque.re/zotero-better-bibtex/)

## Font styles for author names

The .bib file I have auto updated is `_Weber.bib`, however, you'll notice that the `.tex` file actually calls `test.bib`. This file is created when you run `boldauthors.sh`. You will want to edit this file to change your name, supervisor names, and student names.

## Auto populated number of citations

Using the python script `cite.py`, I have a google-scraper use my author ID number to create a json file of all of my papers. I then manually edit `citationvalues.tex` to associate the url id for the paper and the number of citations, with a unique id for that value. The `.tex` file then calls that number in my publications section. So you will need to edit both the `cite.py` file to use your Google Scholar ID, and you will need to manually change `citationvalues.tex` and add your papers. That part requires some work, but the amount of time it will save you in the future is pretty big.
