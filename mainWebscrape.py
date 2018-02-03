## Main script for Python NCAA Webscrape
import numpy as np
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

#Slow crawl rate
from time import sleep
from random import randint

from NCAAStep1 import grabTeams
from NCAAStep2 import grabStats

sport = 'MSO'
division = '1'
year = '2018'
homeURL = ("http://stats.ncaa.org/team/inst_team_list?academic_year=" + year
    + "&conf_id=-1&division=" + division + "&sport_code=" + sport)

listOfURLS = grabTeams(homeURL)
scrapedInformation = pd.DataFrame({'A': [], 'B': [], 'C': []})

progressCounter = 0
for school in listOfURLS:
    sleep(randint(1,4))
    scrapedInformation.append(grabStats(school))
    progressCounter += 1
    if (progressCounter%20==0):
        print("Percent Complete: " + str(100 * (progressCounter/(len(listOfURLS)))) + "%")

scrapedInformation

print(scrapedInformation)
