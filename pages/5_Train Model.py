from sklearn.metrics import mean_squared_error
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

        ticker = share_to_buy+".SA"
        info = (yfinance.Ticker(ticker).info)
        company_name = info['longName']

        st.title(f"Training Model for {company_name}")
        # TAKE DATA
        share_ibov = pdr.get_data_yahoo(
            share_to_buy+".SA", data_inicial, data_final)["Adj Close"]
        # TRANSFORM THE DATA
        share_ts = share_ibov.resample("MS").mean()

        col11, col22, col33 = st.columns([1, 1, 1])

        with col11:
            # EXPLORATORY DATA ANALYSIS
            decomposition = sm.tsa.seasonal_decompose(
                share_ts, model="additive")
            fig = decomposition.plot()
            plt.tight_layout()
            # Exibir o gráfico no Streamlit
            st.pyplot(fig)

        with col22:
            # ACF
            fig_acf = plt.figure(figsize=(8, 6))
            ax_acf = fig_acf.add_subplot()
            plot_acf(share_ts, lags=10, ax=ax_acf)
            plt.xlabel('Lags')
            plt.ylabel('ACF')
            plt.title('Autocorrelation Function (ACF)')

            # Exibir a plot ACF no Streamlit
            st.pyplot(fig_acf)

        with col33:
            # PACF
            fig_pacf = plt.figure(figsize=(8, 6))
            ax_pacf = fig_pacf.add_subplot()
            plot_pacf(share_ts, lags=10, ax=ax_pacf)
            plt.xlabel('Lags')
            plt.ylabel('PACF')
            plt.title('Partial Autocorrelation Function (PACF)')

            # Exibir a plot PACF no Streamlit
            st.pyplot(fig_pacf)

        with col11:
            # Differencing
            fig_diff = plt.figure(figsize=(8, 6))
            ax_diff = fig_diff.add_subplot()
            dados_diff = share_ts.diff().dropna()
            dados_diff.plot(ax=ax_diff)
            plt.xlabel('Índice')
            plt.ylabel('Differencing')
            plt.title('Differencing')

            # Exibir a plot Differencing no Streamlit
            st.pyplot(fig_diff)

        with col22:
            # SEPARATE TRAIN AND TEST
            size = int(len(share_ts)*0.80)
            train = share_ts[:size]
            test = share_ts[size:]

            # Because our data has seasonality, we should run SARIMA instead of ARIMA
            model = sm.tsa.arima.ARIMA(train, order=(
                p, 2, 3), seasonal_order=(0, 0, 1, 12)).fit()
            # PREDICTION
            pred = model.predict(start=len(train), end=len(share_ts)-1)

            # PLOT THE DATA WITH THE PREDICTIONS, TRAIN AND TEST
            train.plot(legend=True, label="train")
            pred.plot(legend=True, label="pred")
            test.plot(legend=True, label="test")
            plt.tight_layout()
            st.pyplot(plt)

        squared_error = np.sqrt(mean_squared_error(test, pred))
        st.write(f"The RMSE is: {squared_error:.2f}")

    except:
        st.write("---")
        st.header("Choice a stock to train the model...")
        st.write("---")

st.sidebar.image("images/logo.png", use_column_width=True)
