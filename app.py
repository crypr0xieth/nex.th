from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

# Главная страница
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crypto_id = request.form['crypto_id']
        amount = float(request.form['amount'])
        price = get_crypto_price(crypto_id)
        total_value = price * amount
        return render_template('index.html', total_value=total_value, crypto_id=crypto_id, amount=amount)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
