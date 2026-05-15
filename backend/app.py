from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/prices")
def get_prices():
    coins = ["bitcoin", "ethereum", "dogecoin"]
    prices = {}

    for coin in coins:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        prices[coin] = data[coin]["usd"]

    return jsonify(prices)
