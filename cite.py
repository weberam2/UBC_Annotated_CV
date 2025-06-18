from scholar_scraper import scholar_scraper
import json
from datetime import date

# get todya's date as month (word) and year (number)
todaydate = date.today().strftime("%B %Y")

# Define the list of authors Google Scholar IDs
scholarIds = [
    "nPuyG8gAAAAJ",
]

# Start scraping and print the resulted JSON to the console
with open("output.json", "w") as f:
    # Write data to the JSON file
    f.write(scholar_scraper.start_scraping(scholarIds))
# open the json file
with open("output.json", "r") as file:
    data_loaded = json.load(file)
# get number of total ciations
totalcitations = data_loaded[0]["citedby"]

# file to write to that latex will read from
filename = "citationvalues.tex"

# start with an empty list
latex_commands = []

# Write today's date
latex_commands.append(f"\\newcommand{{\\datecitationran}}{{{todaydate}}}")

# Write total citations
latex_commands.append(f"\\newcommand{{\\totalcitations}}{{{totalcitations}}}")

# Extract specific citation counts by matching titles
# NOTE: these links have to be identical to what google scholar points to. So get the links from there
urls_to_commands = {
    "https://www.nature.com/articles/nn.2657": "\\ntypecal",
    "https://www.nature.com/articles/nn0809-957a": "\\pdlim",
    "https://www.dl.begellhouse.com/journals/7e4ff0643eace965,0f56de4765dd934d,324a78f56257c7e5.html?utm_source=TrendMD&utm_medium=cpc&utm_campaign=Visualization%252C_Image_Processing_and_Computation_in_Biomedicine_TrendMD_1": "\\warsi",
    "https://www.cmajopen.ca/content/1/1/E48.short": "\\anglin",
    "https://www.sciencedirect.com/science/article/pii/S0925492714000316": "\\psychotropic",
    "https://www.sciencedirect.com/science/article/pii/S0278584614000773": "\\psychopharm",
    "https://link.springer.com/article/10.1007/s10334-013-0420-5": "\\ethanol",
    "https://www.frontiersin.org/articles/10.3389/fneur.2018.00575/full": "\\pathological",
    "https://www.ajnr.org/content/40/7/1221.abstract": "\\punctate",
    "https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/nbm.4222": "\\rtwostar",
    "https://www.ajnr.org/content/42/7/1327.abstract": "\\perinatal",
    "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2021.809943/full?field&journalName=Frontiers_in_Physiology&id=809943": "\\campbellfractal",
    "https://onlinelibrary.wiley.com/doi/abs/10.1002/hbm.25801": "\\campbellreview",
    "https://www.sciencedirect.com/science/article/pii/S1053811922008230": "\\bartel",
    "https://onlinelibrary.wiley.com/doi/abs/10.1002/jmri.28448": "\\fothergill",
    "https://meridian.allenpress.com/tscir/article/30/2/78/500875": "\\sci",
    "https://www.frontiersin.org/articles/10.3389/fnhum.2024.1316117/full": "\\dcdchanges",
    "https://www.frontiersin.org/articles/10.3389/fnhum.2024.1276057/full": "\\dcdcontrols",
    "https://www.mdpi.com/2072-6643/16/15/2559": "\\iron",
    "https://journals.plos.org/complexsystems/article?id=10.1371/journal.pcsy.0000024": "\\sickkids",
    "https://academic.oup.com/cercor/article-abstract/34/10/bhae426/7906856": "\\dhcp",
    "https://www.nature.com/articles/s41390-025-03966-6": "\\carmichael",
    "https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/nbm.70065": "\\zhucmro",
}

# count the total number of urls above
numberofpapers = len(urls_to_commands)
latex_commands.append(f"\\newcommand{{\\totalpapers}}{{{numberofpapers}}}")

# fill citations.tex with number of citations for each paper
citationslist = []
for pub in data_loaded[0]["publications"]:
    if pub["pub_url"] in urls_to_commands:
        command = urls_to_commands[pub["pub_url"]]
        latex_commands.append(f"\\newcommand{{{command}}}{{{pub['num_citations']}}}")
        citationslist.append(pub["num_citations"])


# calculate H-index
def h_index(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations, 1):
        if c >= i:
            h = i
        else:
            break
    return h + 1


latex_commands.append(f"\\newcommand{{\\hindex}}{{{h_index(citationslist)}}}")

# print(f"H-index = {h_index(citationslist)}")

# Write all commands to the file at once
with open(filename, "w") as file:
    file.write("\n".join(latex_commands))
