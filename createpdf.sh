#!/bin/bash

echo "Running boldauthors.sh"
./boldauthors.sh

echo "Running cite.py"
uv run python3 cite.py
#
echo "Running altcite.py"
uv run python3 altcite.py
#
echo "Running githubstats.py"
uv run python3 githubstats.py

echo "Running pdflatex and bibtex"
pdflatex UBC_CV
bibtex UBC_CV
pdflatex UBC_CV
pdflatex UBC_CV
