# Trying to scrape http://stats.ncaa.org/team/inst_team_list?sport_code=MSO&division=1

from requests import get
from bs4 import BeautifulSoup

url = 'http://stats.ncaa.org/team/inst_team_list?sport_code=MSO&division=1'

response = get(url)
#print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'html.parser')

team_containers = html_soup.find_all('div', class_ = 'css-panes')

#print(type(team_containers))
#print(len(team_containers))

#print(team_containers)

team_container = team_containers[0]

print(team_container.td.a.text)


team_table = team_containers.find_all('td', valign_ = 'top')

print(team_table)
