import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas_datareader.data as pdr
import yfinance

yfinance.pdr_override()


st.header("Portfolio Analysis")
arquivo = st.file_uploader("Please upload your portfolio file (xlsx) here")

# st.write("---")
try:

    col1, col2 = st.columns([4, 1])

    with col2:

        # read the data
        dias = st.select_slider(
            "How many days", [45, 60, 90, 120, 180, 360, 720, 1440, 1180])
        df_carteira = pd.read_excel(arquivo)
        st.write(df_carteira)
        email = st.text_area(
            "Send us a comment (press ctrl + enter to send)", height=150)

    with col1:

        st.subheader("My Portfolio")
        # define the datatime
        data_inicial = datetime.now() - timedelta(days=dias)
        data_final = datetime.now()

        # define the stocks
        lista_ativos = list(df_carteira["Ativos"].astype(str) + ".SA")

        # define the stocks data
        df_cotacoes = pdr.get_data_yahoo(
            lista_ativos, data_inicial, data_final)["Adj Close"]

        # clean the data
        df_cotacoes = df_cotacoes.ffill()

        # normalize the data
        df_cotacoes_norm = df_cotacoes / df_cotacoes.iloc[0]

        # df_cotacoes_norm.plot(figsize=(15, 5))
        # plt.legend(loc="upper left")
        # plt.show()

        # plot the data
        chart_data = pd.DataFrame(df_cotacoes_norm)
        st.line_chart(df_cotacoes_norm)

        # take the indexfunds
        df_ibov = pdr.get_data_yahoo(
            "^BVSP", data_inicial, data_final)["Adj Close"]

        df_valor_investido = pd.DataFrame()

        for ativo in df_carteira["Ativos"]:
            qtde_acoes = df_carteira.loc[df_carteira["Ativos"]
                                         == ativo, "Qtde"].values[0]
            df_valor_investido[ativo] = qtde_acoes * df_cotacoes[f"{ativo}.SA"]

        df_valor_investido["Total"] = df_valor_investido.sum(axis=1)

        st.write("---")

        col11, col22, col33 = st.columns([1, 1, 1])

        with col33:
            valor_inv = (df_valor_investido["Total"][-1]).round(2)
            st.header(f"You have $ {valor_inv:,.0f} in investments")

        with col11:
            st.subheader("My Portfolio x Indexfunds")

            # normalize and concat the data
            df_ibov_norm = pd.DataFrame(df_ibov / df_ibov.iloc[0])
            df_valor_investido_norm = pd.DataFrame(
                df_valor_investido["Total"] / df_valor_investido.iloc[0]["Total"])
            newdf = pd.concat([df_ibov_norm, df_valor_investido_norm], axis=1)

            # rename the columns
            newdf.rename(columns={"Adj Close": "Indexfunds",
                         "Total": "Portfolio"}, inplace=True)

            # print the chart

            retorno_ibov = df_ibov_norm["Adj Close"][-1] - 1
            retorno_carteira = df_valor_investido_norm["Total"][-1] - 1
            correlação = df_valor_investido["Total"].corr(df_ibov)
            st.write(
                f" - The return of **IBOV** is **{retorno_ibov:.1%}** in **{dias}** days")
            st.write(
                f" - The return of your Stock Portfolio is **{retorno_carteira:.1%}** in **{dias}** days")
            st.write(
                f" - The correlation between your Stock Portfolio and **IBOV** is: {correlação:.1%}")

        st.write("---")
except:
    st.write("---")
    st.header("Choice a Portfolio to Analyze...")
    st.write("---")
    pass
