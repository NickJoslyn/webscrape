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

matchInformation = scheduleTable.find_all('td', class_ = "smtext")
counter = 0

for match in matchInformation:
    if (counter == 0):
        date.append(match.text)
        counter += 1
    elif (counter == 1):
        opponent.append(match.find('a').text)
        counter += 1
    else:
        result.append(match.find('a').text)
        counter = 0

'''
print("Date: " + str(len(date)))
print(date)
print("\n Opponent: " + str(len(opponent)))
print(opponent)
print("\n Result: " + str(len(result)))
print(result)
'''

#Still need to find stats
statsTable = team_container.find_all('td', width = "50%")[1]
