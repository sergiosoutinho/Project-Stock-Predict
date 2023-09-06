#import libraries 

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas_datareader.data as pdr
import pandas_ta as ta
import yfinance

yfinance.pdr_override()

# Use try to don´t show errors in the app during the execution or changes of parameters
try:

    # stock list
    lista_bovespa = ["PETR4.SA","ITSA4.SA","VALE3.SA","ABEV3.SA","BBAS3.SA", "VIVA3.SA"]
    lista_portugal = ["EDP.LS","CTT.LS","PGAL","SCP.LS"]
    lista_eua = ["AAPL","MSFT","GOOGL","AMZN", "META"]

    # market list
    market = {"PSI20.LS":lista_portugal, "^BVSP":lista_bovespa, "^DJI":lista_eua}
    
    # define the columns to divide the page
    col1, col2 = st.columns([4,1])
    
    # put the inputs in a column
    with col2: 
        # define the stock out of list to analyze
        share = st.radio("Market", list(market.keys()))      
        # define the market to analyze     
        share_to_analyze = st.radio("Stock", market[share])
        # define the stock in the list to analyze
        stock_to_analyze = st.text_input("Write a Stock to Analyze (.SA)") 

         
        # define a new stock to analyze out of the list
        if stock_to_analyze != "":
            share_to_buy = stock_to_analyze
        else:
            share_to_buy = share_to_analyze
  

    # column with the data visualization
    with col1: 


        #function to take data from yahoofinance
        def take_data(): 

            # define period
            data_inicial = datetime.now() - timedelta(days=30)
            data_final = datetime.now()
            # define data to compare
            df_ibov = pdr.get_data_yahoo(share, data_inicial, data_final)["Adj Close"]
            
            # define data to analyze
            share_ibov = pdr.get_data_yahoo(share_to_buy, data_inicial, data_final)["Adj Close"]    

            return df_ibov, share_ibov

        

        # take the data
        df_ibov, share_ibov = take_data()         

        ticker = share_to_buy
        info = yfinance.Ticker(ticker).info
        company_name = info['longName']
   
      

        st.title(f"NEWS - {company_name}")
        st.write("---")
        noticias = yfinance.Ticker(ticker).news
        for noticia in noticias:
            titlo = noticia['title']
            link = noticia['link']
            st.subheader(f"{titlo}")
            st.write(f"Link: {link}")
            st.write("")




except:
    st.write("---")
    st.header("Choice a stock to see the news...")
    st.write("---")
    pass    