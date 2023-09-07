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
    # page title
    st.title("Stock Analysis and Price Prediction")

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
        # choose the number of days
        dias = st.select_slider("How many days",[30, 60, 90, 120, 180, 360, 720, 1080, 1440, 1180,1540,1900])
        # define the indicators in the page
        indicators = st.multiselect("Indicators", ["sma_21", "sma_50", "sma_200", "ema_21", "ema_50", "ema_200", "macd_21", "macd_50", "macd_200", "rsi_21", "rsi_50", "rsi_200"])
        # define the stock out of list to analyze
        share = st.radio("Indexfunds", list(market.keys()))      
        # define the market to analyze     
        share_to_analyze = st.radio("Ticker", market[share])
        # define the stock in the list to analyze
        stock_to_analyze = st.text_input("Write a Ticker to Analyze (.SA)") 
        
        

        # define the date to see the stock price
        date_store = st.date_input("Price date")
         
        # define a new stock to analyze out of the list
        if stock_to_analyze != "":
            share_to_buy = stock_to_analyze
        else:
            share_to_buy = share_to_analyze
        
        # create a email area
        email = st.text_area("Send us a comment (press ctrl + enter to send)", height=150)     

    # column with the data visualization
    with col1: 


        #function to take data from yahoofinance
        def take_data(): 

            # define period
            data_inicial = datetime.now() - timedelta(days=dias)
            data_final = datetime.now()
            # define data to compare
            df_ibov = pdr.get_data_yahoo(share, data_inicial, data_final)["Adj Close"]
            
            # define data to analyze
            share_ibov = pdr.get_data_yahoo(share_to_buy, data_inicial, data_final)["Adj Close"]    

            return df_ibov, share_ibov
        
        # take the price to a define date 
        price_store = pdr.get_data_yahoo(share_to_buy, date_store)["Adj Close"] 
        

        # take the data
        df_ibov, share_ibov = take_data()            

        # normalize the data
        df_ibov_norm = df_ibov / df_ibov.iloc[0]
        share_ibov_norm = share_ibov / share_ibov.iloc[0]
        
        # create indicators
        indicadores = {}

        #media_movel = share_ibov_norm.rolling(9).mean()
        sma_21 = ta.sma(share_ibov_norm, length=21) # Calcula a média móvel simples
        sma_50 = ta.sma(share_ibov_norm, length=50) # Calcula a média móvel simples
        sma_200 = ta.sma(share_ibov_norm, length=200) # Calcula a média móvel simples
        ema_21 = ta.ema(share_ibov_norm, length=21) # Calcula a média móvel exponencial
        ema_50 = ta.ema(share_ibov_norm, length=50) # Calcula a média móvel exponencial
        ema_200 = ta.ema(share_ibov_norm, length=200) # Calcula a média móvel exponencial
        macd_21 = ta.macd(share_ibov_norm, length=21) # Calcula o MACD
        macd_50 = ta.macd(share_ibov_norm, length=50) # Calcula o MACD
        macd_200 = ta.macd(share_ibov_norm, length=200) # Calcula o MACD
        rsi_14 = ta.rsi(share_ibov_norm, length=14) # Calcula o Índice de Força Relativa
        rsi_21 = ta.rsi(share_ibov_norm, length=21) # Calcula o Índice de Força Relativa
        rsi_50 = ta.rsi(share_ibov_norm, length=50) # Calcula o Índice de Força Relativa


        if "sma_21" in indicators:
            indicadores["sma_21"] = sma_21
        if "sma_50" in indicators:
            indicadores["sma_50"] = sma_50
        if "sma_200" in indicators:
            indicadores["sma_200"] = sma_200
        if "ema_21" in indicators:
            indicadores["ema_21"] = ema_21
        if "ema_50" in indicators:
            indicadores["ema_50"] = ema_50
        if "ema_200" in indicators:
            indicadores["ema_200"] = ema_200
        if "macd_21" in indicators:
            indicadores["macd_21"] = macd_21
        if "macd_50" in indicators:
            indicadores["macd_50"] = macd_50
        if "macd_200" in indicators:
            indicadores["macd_200"] = macd_200
        if "rsi_21" in indicators:
            indicadores["rsi_21"] = rsi_21
        if "rsi_50" in indicators:
            indicadores["rsi_50"] = rsi_50
        if "rsi_200" in indicators:
            indicadores["rsi_200"] = rsi_14
        
        indicadores[share] = df_ibov_norm
        indicadores[share_to_buy] = share_ibov_norm


        # put the chart in a container        
        chart_data = pd.DataFrame(indicadores)

    
        # print the chart
        st.line_chart(chart_data)

        
        col11, col22, col33 = st.columns([1,4,4])
        
        with col11:
            # images for the market countries
            if share == "^BVSP":
                st.image("images/br.png", width=100)
            elif share == "^DJI":
                st.image("images/eu.png", width=100)
            else:
                st.image("images/pt.png", width=100)


        with col22:
            # share_ibov = share_ibov["Adj Close"] # teste
            st.subheader(f"**{share}** x **{share_to_buy}**")
            retorno_ibov = df_ibov.iloc[-1] / df_ibov.iloc[0] - 1
            retorno_share = share_ibov.iloc[-1] / share_ibov.iloc[0] - 1
            st.write(f" - The return of **{share}** was: **{retorno_ibov:.1%}** in **{dias}** days")
            st.write(f" - The return of **{share_to_buy}** was: **{retorno_share:.1%}** in **{dias}** days")
            st.write(f" - The correlation between **{share}** and **{share_to_buy}** is: {share_ibov.corr(df_ibov):.1%}")
        
        
            if retorno_share > retorno_ibov:
                st.write(f" - The **{share_to_buy}** was better then the **{share}** in the period of **{dias}** days")
            else:
                st.write(f" - The **{share}** was better then the **{share_to_buy}** in the period of **{dias}** days")
            
        with col33:
            
            ticker = share_to_buy
            info = yfinance.Ticker(ticker).info
            company_name = info['longName']
            st.subheader(company_name)



            st.write(f" - The **{share_to_buy}** price was **{price_store.iloc[0]:,.2f}** in **{date_store}**")
            try:
                if sma_200[-1] < sma_50[-1]:
                    st.write(f" - The Ticker **{share_to_buy}** trend is **upward** according to the moving average")
                else:
                    st.write(f" - The Ticker **{share_to_buy}** trend is **down** according to the moving average")
            except:
                pass

        st.write("---")

        # st.title(f"NEWS - {company_name}")
        # noticias = yfinance.Ticker(ticker).news
        # for noticia in noticias:
        #     titlo = noticia['title']
        #     link = noticia['link']
        #     st.write(f"Título: {titlo}")
        #     st.write(f"Link: {link}")
        #     st.write("")




except:
    st.write("---")
    st.header("You have a typo: try again")
    st.write("---")
    pass    

    
st.sidebar.image("images/logo.png", use_column_width=True)


