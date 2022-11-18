from flask import Blueprint, render_template
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import requests
import re
import html5lib
from bs4 import BeautifulSoup
views = Blueprint('view', __name__)

@views.route('/')

def basehtml():
    return render_template("homepage.html")


@views.route('/1v1Leaderboard')

def getonevone():
    url = 'https://rlstats.net/leaderboards/skills'
    request = requests.get(url)
    RLstats = BeautifulSoup(request.text, 'html.parser')
    onevonetable = RLstats.find("table", attrs={'data-platform':'Mixed', 'data-skill':'13'})
    df = pd.read_html(str(onevonetable))[0]
    df1 = df.style.set_properties(**{'background-color': 'black',
                           'color': '#f25b22',
                           'border-color': '#19181d'}).hide_index()
    titles = None
    return render_template("one.html", tables=[df1.to_html(classes='data')], titles=titles)


@views.route('/2v2Leaderboard')

def gettwovtwo():
    url = 'https://rlstats.net/leaderboards/skills'
    request = requests.get(url)
    RLstats = BeautifulSoup(request.text, 'html.parser')
    twovtwotable = RLstats.find("table", attrs={'data-platform':'Mixed', 'data-skill':'11'})
    df = pd.read_html(str(twovtwotable),header=None)[0]
    df2 = df.style.set_properties(**{'background-color': 'black',
                           'color': '#f25b22',
                           'border-color': '#19181d'}).hide_index()
    titles = None

    return render_template("two.html", tables=[df2.to_html(classes='data')], titles=titles)


@views.route('/3v3Leaderboard')

def getthreevthree():
    url = 'https://rlstats.net/leaderboards/skills'
    request = requests.get(url)
    RLstats = BeautifulSoup(request.text, 'html.parser')
    threevthreetable = RLstats.find("table", attrs={'data-platform':'Mixed', 'data-skill':'10'})
    df = pd.read_html(str(threevthreetable), index_col=None)[0]

    df3 = df.style.set_properties(**{'background-color': 'black',
                           'color': '#f25b22',
                           'border-color': '#19181d'}).hide_index()

    titles = None
    return render_template("three.html", tables=[df3.to_html(classes='data')], titles=titles)



@views.route('/Population')

def population():
    url = 'https://rlstats.net/population'
    request = requests.get(url)
    RLstats = BeautifulSoup(request.text, 'html.parser')
    playerPopulation = RLstats.find("table", attrs={ 'class' : "population"})

    df = pd.read_html(str(playerPopulation))[0]
    df4 = df.style.set_properties(**{'background-color': 'black',
                           'color': '#f25b22',
                           'border-color': '#19181d'}).hide_index()
    titles = None
    return render_template("population.html", tables=[df4.to_html(classes='data')], titles=titles)


@views.route('/About')

def About():
    return render_template("home.html")

@views.route('/Projects', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/About Me'))
    return render_template('Projects.html', error=error)
