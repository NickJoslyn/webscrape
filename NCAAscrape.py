# Trying to scrape http://stats.ncaa.org/team/inst_team_list?sport_code=MSO&division=1

from requests import get

url = 'http://stats.ncaa.org/team/inst_team_list?sport_code=MSO&division=1'

response = get(url)
print(response.text[:500])
