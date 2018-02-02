## Python program to extract NCAA soccer data
## Two-Step Program
## Step 1: Extract team names from http://stats.ncaa.org/team/inst_team_list?sport_code=MSO&division=1

from requests import get
from bs4 import BeautifulSoup

schools = []
url = 'http://stats.ncaa.org/team/inst_team_list?sport_code=MSO&division=1'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

# For this website, there is only one relevant div tag
team_containers = html_soup.find_all('div', class_ = 'css-panes')
team_container = team_containers[0]

#Put the information for each table entry in an array
entryInformation = team_container.find_all('a')

for entry in entryInformation:
    schools.append(entry.text)

print(schools)

print("\n")

print(len(schools))
