import requests

filename = "githubvalues.tex"

url = "https://api.github.com/users/WeberLab/repos"

response = requests.get(url)
if response.status_code == 200:  # | response2.status_code == 200:
    data = response.json()
    private_flags = [repo["private"] for repo in data]
    public_count = sum(not p for p in private_flags)
    total_forks = sum(repo["forks_count"] for repo in data)
    total_stars = sum(repo["stargazers_count"] for repo in data)


gitstatssentence = f"Number of Github public repositories: {public_count}\\newline \\indent Number of total forks: {total_forks}\\newline \\indent Number of total stars: {total_stars}"

gitstats = []
gitstats.append(f"\\newcommand{{\\gitcount}}{{{gitstatssentence}}}")

with open(filename, "w") as file:
    file.write("\n".join(gitstats))
