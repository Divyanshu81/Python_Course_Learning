import streamlit as st
import plotly.express as px
import datetime
from backend import get_data

page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-color:Black;
    }
    </style>
    """


st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Weather Forecast for Next Few Days')


inp1 = st.text_input(label="Place: ", placeholder="Enter the Value", key="place")
inp2 = st.slider(label="Forecast Days", min_value=1, max_value=5)
inp3 = st.selectbox(label="Select data to view", options=["Temperature", "Sky"])


if inp1 and inp2 and inp3:
    try:
        api_data = get_data(inp1, inp2)
        st.subheader(f"{inp3} for the next {inp2} days in {inp1}")
        if inp3 == "Temperature":
            temperatures = [data["main"]["temp"] for data in api_data]
            dates = [date["dt_txt"] for date in api_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature(C)"})
            st.plotly_chart(figure)
        if inp3 == "Sky":
            dates = [date["dt_txt"] for date in api_data]
            sky_condition = [f"Project7/images/{data['weather'][0]['main']}.png" for data in api_data]
            display_dates = [i.split('-') for i in dates]
            out=[]
            for i in range(len(dates)):
                out.append(datetime.datetime(int(display_dates[i][0]),int(display_dates[i][1]),int(display_dates[i][2][:2]),int(display_dates[i][2][3:5]),0))
            final = [x.strftime("%a, %b %d %H:%M") for x in out]
            st.image(sky_condition, width=100,caption=final)
    except KeyError:
        st.subheader("THIS PLACE DOESN'T EXIST!!!!")
