#!/bin/bash

rm test.bib
cp _Weber.bib test.bib
# Detect OS
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS
  sed -i '' 's/Weber/\\textbf{Weber}/g' test.bib
  sed -i '' 's/Noseworthy/\\textit{Noseworthy}/g' test.bib
  sed -i '' 's/Soreni/\\textit{Soreni}/g' test.bib
  sed -i '' 's/Rauscher/\\textit{\\textbf{Rauscher}}/g' test.bib
  sed -i '' 's/Zhang/\\underline{Zhang}/g' test.bib
  sed -i '' 's/Campbell/\\underline{Campbell}/g' test.bib
  sed -i '' 's/Zhu/\\underline{Zhu}/g' test.bib
  sed -i '' 's/Drayne/\\underline{Drayne}/g' test.bib
  sed -i '' 's/Mella/\\underline{Mella}/g' test.bib
  sed -i '' 's/Armour/\\underline{Armour}/g' test.bib
  sed -i '' 's/Carmichael/\\underline{Carmichael}/g' test.bib
  sed -i '' 's/Sochan/\\underline{Sochan}/g' test.bib
else
  # Linux
  sed -i 's/Weber/\\textbf{Weber}/g' test.bib
  sed -i 's/Noseworthy/\\textit{Noseworthy}/g' test.bib
  sed -i 's/Soreni/\\textit{Soreni}/g' test.bib
  sed -i 's/Rauscher/\\textit{\\textbf{Rauscher}}/g' test.bib
  sed -i 's/Zhang/\\underline{Zhang}/g' test.bib
  sed -i 's/Campbell/\\underline{Campbell}/g' test.bib
  sed -i 's/Zhu/\\underline{Zhu}/g' test.bib
  sed -i 's/Drayne/\\underline{Drayne}/g' test.bib
  sed -i 's/Mella/\\underline{Mella}/g' test.bib
  sed -i 's/Armour/\\underline{Armour}/g' test.bib
  sed -i 's/Carmichael/\\underline{Carmichael}/g' test.bib
  sed -i 's/Sochan/\\underline{Sochan}/g' test.bib
fi
