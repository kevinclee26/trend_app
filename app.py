import streamlit as st
import yfinance as yf
import datetime

TICKER='NVDA'

st.sidebar.write(f'Ticker: {TICKER}')

start_date=st.sidebar.date_input('Select Date:', datetime.date(2023, 10, 23))
start_date_formatted=f'{start_date.year}-{start_date.month}-{start_date.day}'

ticker = yf.Ticker(TICKER)

# get all stock info
# st.write(ticker.info)

# get historical market data
hist=ticker.history(period="1y")

# st.write(hist.head())
st.line_chart(hist.loc[start_date_formatted:, 'Close'])