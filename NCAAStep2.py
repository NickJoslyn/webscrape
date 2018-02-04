## Step 2: Grab schedule/results and season stats
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

def grabStats(url):

    # If url wasn't found in Step 1, return empty row for df
    if (url == "N/A"):
        print("No URL available")
        return pd.DataFrame({'A': [], 'B': [], 'C': []})

    else:
        url = "http://stats.ncaa.org" + url
        response = get(url)

        html_soup = BeautifulSoup(response.text, 'html.parser')
        team_container = html_soup.find('div', id = 'contentarea')

        try:
            teamName = team_container.fieldset.legend.a.text
        except:
            print("Couldn't find team name")
            teamName = "N/A"
        #------------Schedule and Results Information--------------------
        # Find schedule/results table in html_soup
        # Date of competition, opponent, and result in relevant array
        # Merge individual arrays into one for use in df

        try:
            scheduleTable = team_container.find_all('td', width = "50%")[0]
        except:
            print("Couldn't find schedule of " + str(teamName))
            return pd.DataFrame({'A': teamName, 'B': [], 'C': []})

        date = []
        opponent = []
        result = []

        try:
            matchInformation = scheduleTable.find_all('td', class_ = "smtext")
        except:
            print("Couldn't find match information of " + str(teamName))
            return pd.DataFrame({'A': teamName, 'B': [], 'C': []})

        counter = 0

        for match in matchInformation:
            if (counter == 0):
                try:
                    date.append(match.text)
                except:
                    print("Couldn't find date")
                    date.append("N/A")
                counter += 1
            elif (counter == 1):
                try:
                    opponent.append(match.find('a').text)
                except:
                    print("Couldn't find opponent")
                    opponent.append("N/A")
                counter += 1
            else:
                try:
                    result.append(match.find('a').text)
                except:
                    print("Couldn't find result")
                    result.append("N/A")
                counter = 0

        #Combine into one array - All have the same dimensions
        seasonMatchInformation = [date, opponent, result]

        #------------Team Statistical Information--------------------
        # Find season statistics table in html_soup
        # Category, national ranking, and actual stat in relvevant array
        # Merge into one array for df

        try:
            statsTable = team_container.find_all('td', width = "50%")[1]
        except:
            print("Couldn't find stats of " + str(teamName))
            return pd.DataFrame({'A': teamName, 'B': [], 'C': []})

        categories = statsTable.find_all('a')
        statType = []

        for category in categories:
            try:
                statType.append(category.text)
            except:
                print("Couldn't find stat category")
                statType.append("N/A")
                
        #Last element is "view complete ranking summary" which can be deleted
        statType = statType[:-1]

        statInformation = statsTable.find_all('td', align = "right")
        ranking = []
        value = []
        statCounter = 0

        for stat in statInformation:
            if (statCounter%2 == 0):
                try:
                    ranking.append(stat.text)
                except:
                    print("Couldn't find ranking")
                    ranking.append("N/A")
            else:
                try:
                    value.append(float(stat.text))
                except:
                    print("Couldn't find value")
                    value.append("N/A")
            statCounter += 1

        #Combine into one array - All have the same dimensions
        seasonStatInformation = [statType, ranking, value]

        #------------Put Together in a data frame--------------------

        singleTeamDF = pd.DataFrame({'A': teamName,
                                    'B': [seasonMatchInformation],
                                    'C': [seasonStatInformation]})

        return singleTeamDF
