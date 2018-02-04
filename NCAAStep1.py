## Step 1: Extract team name/URLs from input url

from requests import get
from bs4 import BeautifulSoup

def grabTeams(url):

    schools = []
    schoolURLs = []
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    # For this website, there is only one relevant div tag
    team_containers = html_soup.find_all('div', class_ = 'css-panes')
    team_container = team_containers[0]

    #Put the information for each school entry in an array
    entryInformation = team_container.find_all('a')

    for entry in entryInformation:
        try:
            schoolURLs.append(entry.get('href'))
        except:
            print("Couldn't find schools URL")
            schoolURLS.append("N/A")

        try:
            schools.append(entry.text)
        except:
            print("Couldn't get schools name in Step 1")
            schools.append("N/A")

    return schoolURLs, schools
