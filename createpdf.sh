#!/bin/bash

./boldauthors.sh

poetry run python3 cite.py
#
poetry run python3 altcite.py
#
pdflatex UBC_CV
bibtex UBC_CV
pdflatex UBC_CV
pdflatex UBC_CV
