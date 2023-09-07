import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas_datareader.data as pdr
import yfinance
import pandas_ta as ta
import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
yfinance.pdr_override()


col1, col2 = st.columns([4, 1])


with col2:
    p = st.select_slider("Select ARIMA P", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    stock_to_analyze = st.text_input("Ticker to Analyze")


with col1:
    try:
        # DEFINE TIME
        share_to_buy = stock_to_analyze
        dias = 1900
        # DEFINE DATE
        data_inicial = datetime.now() - timedelta(days=dias)
        data_final = datetime.now()
        # Take the stock company name
        ticker = share_to_buy+".SA"
        info = (yfinance.Ticker(ticker).info)
        company_name = info['longName']
        # st.subheader(company_name)

        st.title(f"Price Prediction for {company_name}")
        # TAKE DATA
        share_ibov = pdr.get_data_yahoo(
            share_to_buy+".SA", data_inicial, data_final)["Adj Close"]
        # TRANSFORM THE DATA
        share_ts = share_ibov.resample("MS").mean()
        model = sm.tsa.arima.ARIMA(share_ts, order=(
            p, 2, 3), seasonal_order=(0, 0, 1, 12)).fit()

        # pred
        pred = model.predict(start=len(share_ts), end=len(share_ts)+6)

        st.line_chart(pred)
        st.write(pred)

        share_ts.plot(legend=True, label="train", figsize=(10, 6))
        pred.plot(legend=True, label="pred")
        plt.tight_layout()
        st.pyplot(plt)

    except:
        st.write("---")
        st.header("Choice a stock to Predict")
        st.write("---")

st.sidebar.image("images/logo.png", use_column_width=True)
