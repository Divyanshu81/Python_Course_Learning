from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME"]][:92]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/<station>/<date>")
def individual(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"  # zfill fills string to make particular length
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    data = {"station": station,
            "date": date,
            "temperature": temperature}
    return data


@app.route("/api/<station>")
def full_station(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"  # zfill fills string to make particular length
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/<station>/yearly/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"  # zfill fills string to make particular length
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)  # port=x
