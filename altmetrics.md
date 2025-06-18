get dois from exported zotero csv:

`python3 -c "import csv; print('\n'.join(filter(None, (row['DOI'] for row in csv.DictReader(open('WeberPapers.csv'))))))"`

Example doi:

`curl "https://api.altmetric.com/v1/doi/10.1038/nature12373" | jq`

or

`curl -s "https://api.altmetric.com/v1/doi/10.1038/nature12373" > examplealtmet.json`

score:

`cat examplealtmet.json| jq '.score'`

readers count:

`cat examplealtmet.json| jq '.readers_count'`

posts count:

`cat examplealtmet.json|jq '.cited_by_posts_count'`

percent all papers tracked by altmetric:

`cat examplealtmet.json|jq '.context.all.pct'`

percent all last three months:

`cat examplealtmet.json|jq '.context.similar_age_3m.pct'`

Example way to report:
This paper has an Altmetrics score of 4, has been read by 300 people, posted 2 times. It scores higher than 21% of all papers, and 34% in the last three months.

| Metric             | API field                  | Why useful?                  |
| ------------------ | -------------------------- | ---------------------------- |
| Twitter/X mentions | `cited_by_tweeters_count`  | Shows social media reach     |
| News outlets       | `cited_by_msm_count`       | Indicates media attention    |
| Blogs              | `cited_by_feeds_count`     | Long-form discussion         |
| Wikipedia          | `cited_by_wikipedia_count` | Public knowledge integration |
| Policy docs        | `cited_by_policy_count`    | Impact on policy             |
| Patents            | `cited_by_patents_count`   | Possible commercialization   |
| Reddit             | `cited_by_rdts_count`      | Community discussion         |

python3 -c "import csv; print('\n'.join(filter(None, (row['DOI'] for row in csv.DictReader(open('WeberPapers.csv'))))))"
