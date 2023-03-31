from flask import Flask, render_template
import yfinance as yf
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period="1d")
    return render_template("index.html", date=data.index[0], open=data["Open"][0], high=data["High"][0], low=data["Low"][0], close=data["Close"][0], volume=data["Volume"][0])

if __name__ == "__main__":
    app.run()
