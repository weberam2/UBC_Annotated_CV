from scholar_scraper import scholar_scraper
import json

# Define the list of authors Google Scholar IDs
scholarIds = [
    "nPuyG8gAAAAJ",
]

# Start scraping and print the resulted JSON to the console
# print(scholar_scraper.start_scraping(scholarIds))
with open("output.json", "w") as f:
    # Write data to the JSON file
    f.write(scholar_scraper.start_scraping(scholarIds))

with open("output.json", "r") as file:
    data_loaded = json.load(file)

totalcitations = data_loaded[0]["citedby"]

# print(str(totalcitations))
filename = "citationvalues.tex"

latex_commands = []

# Write total citations
latex_commands.append(f"\\newcommand{{\\totalcitations}}{{{totalcitations}}}")

# Extract specific citation counts by matching titles
urls_to_commands = {
    "https://www.nature.com/articles/nn.2657": "\\ntypecal",
    "https://www.nature.com/articles/nn0809-957a": "\\pdlim",
    "https://www.cell.com/biophysj/fulltext/S0006-3495(08)02149-8": "\\warsi",
    "https://www.cmajopen.ca/content/1/1/E48.short": "\\anglin",
    "https://www.sciencedirect.com/science/article/pii/S0925492714000316": "\\psychotropic",
    "https://www.sciencedirect.com/science/article/pii/S0278584614000773": "\\psychopharm",
    "https://link.springer.com/article/10.1007/s10334-013-0420-5": "\\ethanol",
    "https://www.frontiersin.org/articles/10.3389/fneur.2018.00575/full": "\\pathological",
    "https://www.ajnr.org/content/40/7/1221.abstract": "\\punctate",
    "https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/nbm.4222": "\\rtwostar",
    "https://www.ajnr.org/content/42/7/1327.abstract": "\\perinatal",
    "https://www.frontiersin.org/articles/10.3389/fphys.2021.809943/full": "\\campbellfractal",
    "https://onlinelibrary.wiley.com/doi/abs/10.1002/hbm.25801": "\\campbellreview",
    "https://www.sciencedirect.com/science/article/pii/S1053811922008230": "\\bartel",
    "https://onlinelibrary.wiley.com/doi/abs/10.1002/jmri.28448": "\\fothergill",
    "https://meridian.allenpress.com/tscir/article/30/2/78/500875": "\\sci",
    "https://www.frontiersin.org/articles/10.3389/fnhum.2024.1316117/full": "\\dcdchanges",
    "https://www.frontiersin.org/articles/10.3389/fnhum.2024.1276057/full": "\\dcdcontrols",
    "https://www.mdpi.com/2072-6643/16/15/2559": "\\iron",
}

for pub in data_loaded[0]["publications"]:
    if pub["pub_url"] in urls_to_commands:
        command = urls_to_commands[pub["pub_url"]]
        latex_commands.append(f"\\newcommand{{{command}}}{{{pub['num_citations']}}}")

# Write all commands to the file at once
with open(filename, "w") as file:
    file.write("\n".join(latex_commands))
