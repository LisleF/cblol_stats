from bs4 import BeautifulSoup
import requests

#url = 'https://lol.fandom.com/wiki/Special:RunQuery/CastingHistory?CH%5B1%5D=Schaeppi&CH%5Blimit%5D=100&_run='
url = 'https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryPlayer?MHP%5Bpreload%5D=Player&MHP%5Btournament%5D=&MHP%5Blink%5D=Disamis&MHP%5Bchampion%5D=&MHP%5Brole%5D=&MHP%5Bteam%5D=&MHP%5Bpatch%5D=&MHP%5Byear%5D=&MHP%5Bregion%5D=&MHP%5Btournamentlevel%5D=&MHP%5Brecord%5D=&MHP%5Brecordorder%5D%5Bis_checkbox%5D=true&MHP%5Bitem%5D=&MHP%5Bjungleitem%5D=&MHP%5Bjungleenchant%5D=&MHP%5Brune%5D=&MHP%5Bchampionvs%5D=&MHP%5Blimit%5D=96&MHP%5Bwhere%5D=&MHP%5Bincludelink%5D%5Bis_checkbox%5D=true&MHP%5Btextonly%5D%5Bis_checkbox%5D=true&_run=&pfRunQueryFormName=MatchHistoryPlayer&wpRunQuery=&pf_free_text='
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

mytable = soup.find('table', {'class': 'wikitable'})

print(mytable.prettify())

for row in mytable.find_all('tr'):
    for cell in row.find_all('td'):
        print(cell.text)
