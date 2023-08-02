import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as pt
import glob

analyzer = SentimentIntensityAnalyzer()
filepaths = glob.glob("Project8/diary/*.txt")

st.title("Diary Tone")

negativeCounter = []
positiveCounter = []
for file in filepaths:
    with open(file,"r") as singletext:
        data = singletext.read()
    score = analyzer.polarity_scores(data)
    negativeCounter.append(score["neg"])
    positiveCounter.append(score["pos"])

#['diary\\2023-10-21.txt', 'diary\\2023-10-22.txt', 'diary\\2023-10-23.txt', 'diary\\2023-10-24.txt', 'diary\\2023-10-25.txt', 'diary\\2023-10-26.txt', 'diary\\2023-10-27.txt']

dates = [text.strip('Project8//diary\\').strip(".txt") for text in filepaths]
#print(dates,positiveCounter,negativeCounter)
print(dates)
figure_p = pt.line(x=dates, y=positiveCounter, labels={"x": "Date", "y": "Positivity"})
figure_n = pt.line(x=dates, y=negativeCounter, labels={"x": "Date", "y": "Negativity"})

st.subheader("Positivity")
st.plotly_chart(figure_p)
st.subheader("Negativity")
st.plotly_chart(figure_n)