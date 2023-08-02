import requests

API_KEY = "9d00ce6fcfa9d54baeaeee1894a78d8b"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    nr_value = 8 * forecast_days
    filter_data = filter_data[:nr_value]
    return filter_data

if __name__=="__main__":
    print(get_data(place="Tokyo"))