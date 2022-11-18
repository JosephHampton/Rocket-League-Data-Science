from bs4 import BeautifulSoup
from flask import Flask;
import re
import requests
import pandas as pd
import html5lib
url = 'https://rlstats.net/leaderboards/skills'
urltwo = 'https://rlstats.net/population'
request = requests.get(url)
request2 = requests.get(urltwo)
RLstats = BeautifulSoup(request.text, 'html.parser')
RLPopulation = BeautifulSoup(request2.text, 'html.parser')

def getonevone():
    url = 'https://rlstats.net/leaderboards/skills'
    request = requests.get(url)
    RLstats = BeautifulSoup(request.text, 'html.parser')
    onevonetable = RLstats.find("table", attrs={'data-platform':'Mixed', 'data-skill':'13'})
        #onevonedataframe = pd.read_html(str(onevonetable))[0]
        #print(onevonedataframe.to_string(max_rows=None))
    onevonetablefinal = onevonetable[0].text
    return onevonetable

def gettwovtwo():
    url = 'https://rlstats.net/leaderboards/skills'
    request = requests.get(url)
    RLstats = BeautifulSoup(request.text, 'html.parser')
    twovtwotable = RLstats.find("table", attrs={'data-platform':'Mixed', 'data-skill':'11'})
        #twovtwodataframe = pd.read_html(str(twovtwotable))[0]
        #print(twovtwodataframe.to_string(max_rows=None))
    twovtwotablefinal = twovtwotable[0].text
    return twovtwotable
def getthreevthree():
    url = 'https://rlstats.net/leaderboards/skills'
    request = requests.get(url)
    RLstats = BeautifulSoup(request.text, 'html.parser')
    threevthreetable = RLstats.find("table", attrs={'data-platform':'Mixed', 'data-skill':'10'})
        #threevthreedataframe = pd.read_html(str(threevthreetable))[0]
        #print(threevthreedataframe.to_string(max_rows=None))
    threevthreetablefinal = threevthreetable[0].text
    return threevthreetable
def population():
    url = 'https://rlstats.net/leaderboards/skills'
    request = requests.get(url)
    RLstats = BeautifulSoup(request.text, 'html.parser')
    playerPopulation = RLPopulation.find("table", attrs={ 'class' : "population"})
        #popdataframe = pd.read_html(str(playerPopulation))[0]
        #print(popdataframe.to_string(max_rows=None))
    playerPopulationfinal = playerPopulation[0].text
    return playerPopulation


print(getonevone)



