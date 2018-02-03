## Use list of schools/urls from Step 1 to grab statistics

from requests import get
from bs4 import BeautifulSoup

url = 'http://stats.ncaa.org/team/721/12621'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
team_container = html_soup.find('div', id = 'contentarea')

scheduleTable = team_container.find_all('td', width = "50%")[0]
date = []
opponent = []
result = []

#Still need to find date
gameInformation = scheduleTable.find_all('a')
counter = 0
for game in gameInformation:
    if (counter%2 == 0):
        opponent.append(game.text)
    else:
        result.append(game.text)
    counter+=1

print(opponent)
print("\n")
print(result)


#Still need to find stats
statsTable = team_container.find_all('td', width = "50%")[1]
