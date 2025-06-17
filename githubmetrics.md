curl -s <https://api.github.com/users/WeberLab/repos> -o repos.json

cat repos.json| jq '[.[].forks_count] | add'

cat repos.json| jq '[.[].stargazers_count] | add'
