import streamlit as st
import requests

api_key = "U9JqFAZ1nW3CYLUWUnW5KvbfJhU1xN7yX4A6PX8f"

url = "https://api.nasa.gov/planetary/apod?date=2022-12-29&api_key=U9JqFAZ1nW3CYLUWUnW5KvbfJhU1xN7yX4A6PX8f"  #date can be dynamic

# CONNECTING

request = requests.get(url)

# EXTRACTING DATA
content = request.json()
#print(content)

#CREATING WEB PAGE

st.title(content["title"])
st.image(content["url"])
st.write(content["explanation"])
