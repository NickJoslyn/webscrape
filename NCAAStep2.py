## Use list of schools/urls from Step 1 to grab statistics
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

url = 'http://stats.ncaa.org/team/721/12621'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
team_container = html_soup.find('div', id = 'contentarea')

teamName = team_container.fieldset.legend.a.text

#------------Schedule and Results Information--------------------

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

#Combine into one array - All have the same dimensions
seasonMatchInformation = [date, opponent, result]

#------------Team Statistical Information--------------------

statsTable = team_container.find_all('td', width = "50%")[1]

categories = statsTable.find_all('a')
statType = []

for category in categories:
    statType.append(category.text)

#Last element is "view complete ranking summary" which can be deleted
statType = statType[:-1]

statInformation = statsTable.find_all('td', align = "right")
ranking = []
value = []
statCounter = 0

for stat in statInformation:
    if (statCounter%2 == 0):
        ranking.append(stat.text)
    else:
        value.append(float(stat.text))
    statCounter += 1

#Combine into one array - All have the same dimensions
seasonStatInformation = [statType, ranking, value]

#------------Put Together in a data frame--------------------

singleTeamDF = pd.DataFrame({'A': teamName,
                            'B': [seasonMatchInformation],
                            'C': [seasonStatInformation]})

print(singleTeamDF)
