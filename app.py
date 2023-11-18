from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a")
    data = response.json()
    cocktails = data['drinks']
    return render_template('index.html', cocktails=cocktails)

@app.route('/detail/<string:id>')
def detail(id):
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}")
    data = response.json()
    cocktail = data['drinks'][0]
    return render_template('detail.html', cocktail=cocktail)

if __name__ == '__main__':
    app.run(debug=True)
    
