import datetime
from flask import Flask

app = Flask(__name__)
@app.route("/")

def main():
	now = datetime.datetime.now()
	print(now)
