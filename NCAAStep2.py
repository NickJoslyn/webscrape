## Use list of schools/urls from Step 1 to grab statistics

from requests import get
from bs4 import BeautifulSoup

url = 'http://stats.ncaa.org/team/721/12621'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
team_container = html_soup.find('div', id = 'contentarea')

print(team_container.fieldset.legend.a.text)

