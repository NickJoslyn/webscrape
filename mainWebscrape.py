## Main script for Python NCAA Webscrape
#Python modules
import numpy as np
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

#Slow crawl rate
from time import sleep
from random import randint

#Webscrape functions
from NCAAStep1 import grabTeams
from NCAAStep2 import grabStats

#Find url for desired data
sport = 'MSO'
division = '1'
year = '2018'
homeURL = ("http://stats.ncaa.org/team/inst_team_list?academic_year=" + year
    + "&conf_id=-1&division=" + division + "&sport_code=" + sport)

listOfURLS, listOfNames = grabTeams(homeURL)
scrapedInformation = pd.DataFrame({'A': [], 'B': [], 'C': []})

#Loop through schools and extract data to df
progressCounter = 0
for school in listOfURLS:
    sleep(randint(1,4))
    scrapedInformation = scrapedInformation.append(grabStats(school))
    progressCounter += 1
    if (progressCounter%20==0):
        print("Percent Complete: " + str(100 * (progressCounter/(len(listOfURLS)))) + "%")

scrapedInformation

# Additional column in scrapedInformation:
#idx = 3
#scrapedInformationWithNames = scrapedInformation.insert(loc = idx, column = 'D', value = listOfNames)
