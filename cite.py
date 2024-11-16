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
