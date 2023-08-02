from flask import Flask,render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/meaning/<word>")
def meaning(word):
    url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    request = requests.get(url)
    content = request.json()
    requiredata = content[0]["meanings"][0]["definitions"][0]["definition"]
    datashown ={"word": word,
                "meaning": requiredata}
    return datashown

if __name__ == "__main__":
    app.run(debug=True)