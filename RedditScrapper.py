"""
Reddit Scrapper
Gets information on subreddit, saves to time specified .json for future use
Writes data to the data folder

"""
import praw             #For Reddit Data
import yfinance as yf   #For stock info
import reticker         #For stock-ticker detection
import json             #For storing data
import csv              #For writing data

#Litte Things
from datetime import date

#Globals
today = date.today()
today_formated = today.strftime("%b-%d-%Y")

#What subreddit to get data from
sub = 'wallstreetbets'

csv_file = "Data\Data " + today_formated + " "+ sub +".csv"
csv_columns = ['title','body']
post = {
    "title" : [],
    "body" : []
}

data = {
    "ticker" : [],
    "count" : []
}

reddit = praw.Reddit(
    client_id="MLgX0mJ4YXdlLw",
    client_secret="uhZ0nDVoPqitr_AKVhF9XG5Cm24",
    user_agent="Web Scraping Test",
)

for submission in reddit.subreddit(sub).hot(limit=20000):
    post["title"].append(submission.title)
    post["body"].append(submission.selftext)

def writeData():
    with open(csv_file, 'w', newline='') as csvfile:
        for line in post["title"]:
            for tick in reticker.TickerExtractor().extract(line):
                if tick not in data["ticker"]:
                    data["ticker"].append(tick)
                    data["count"].append(1)
                else:
                    data["count"][data["ticker"].index(tick)] = data["count"][data["ticker"].index(tick)] + 1


writeData()
print(data)
