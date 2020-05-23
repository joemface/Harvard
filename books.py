import os
import requests

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(
    "postgres://ugneirzujdicjz:10acfef913d6df3485839d772e56d2cd54e7f2c17e43046482eed0cfac3a9fb9@ec2-50-17-90-177.compute-1.amazonaws.com:5432/d8dbj1ut28rdj9")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


res = requests.get("https://www.goodreads.com/book/review_counts.json",
                   params={"key": "ogA93yMNFmZJdJH9igJxxQ", "isbns": "9781632168146"})
# print(res.json())
