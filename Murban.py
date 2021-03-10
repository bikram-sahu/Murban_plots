import pandas as pd
import numpy as np
import plotly.express as px
import datetime
from dateutil.relativedelta import *
import plotly.graph_objects as go
import streamlit as st

data = pd.read_excel("Argus Historical Prices.xlsx", sheet_name= "Sheet1", engine='openpyxl')
data.dropna(inplace=True)
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.Date, y=data.Murban,
                    mode='lines',
                    name='Murban'))
fig.add_trace(go.Scatter(x=data.Date, y=data["Ice Brent"],
                    mode='lines',
                    name='Ice Brent'))

fig.update_layout(
    yaxis_title= "Mid Price"
)
st.plotly_chart(fig)

data["Spread"] = abs(data["Murban"] - data["Ice Brent"])
fig2 = px.line(data, x="Date", y="Spread")
st.plotly_chart(fig2)

data["Murban - Nymex WTI Spread"] = abs(data["Murban"] - data["Nymex WTI"])
fig4 = px.line(data, x="Date", y="Murban - Nymex WTI Spread")
st.plotly_chart(fig4)


data["Murban_pct"] = data["Murban"].pct_change()
data["Ice Brent_pct"] = data["Ice Brent"].pct_change()

data.dropna(inplace=True)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=data.Date, y=data.Murban_pct,
                    mode='lines',
                    name='Murban'))
fig3.add_trace(go.Scatter(x=data.Date, y=data["Ice Brent_pct"],
                    mode='lines',
                    name='Ice Brent'))

fig3.update_layout(
    yaxis_title= "Daily Return"
)
st.plotly_chart(fig3)
