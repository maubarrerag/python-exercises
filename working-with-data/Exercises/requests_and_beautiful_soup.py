import requests
from bs4 import BeautifulSoup
import re

url = 'https://static.webucator.com/media/public/documents/hrleaders.html'

r = requests.get(url)
text = r.text

def get_rows(content):
    bt = BeautifulSoup(content, 'lxml')
    return bt.find_all('tr')

def parse_rows(rows):
    data = []
    start = 0
    for row in rows:
        if start > 0:
            record = {}
            cols = row.find_all('td')
            record["num"] = cols[0].text
            record["player"] = cols[1].text
            record["runs"] = int(cols[2].text)
            record["year"] = cols[3].text
            record["birth"] = cols[4].text
            data.append(record)
        else:
            start=1
    return data

def find_maxMark(records):  
    maxMark = max([player for player in records if player["player"] == "Mark McGwire"], key=lambda x:x["runs"])
    return maxMark

def find_top(records):
    topPlayers = []
    for player in records:
        if player["runs"] >= 50 and player["player"] not in topPlayers:
            topPlayers.append(player["player"])
    return topPlayers

def main():
    records = parse_rows(get_rows(text))
    maxMark = find_maxMark(records)
    topPlayers = find_top(records)
    print("Max record of Mark McGwire is "+str(maxMark["runs"])+" in the season "+maxMark["year"])
    for player in topPlayers:
        print(player)

if __name__ == '__main__':
    main()
    
