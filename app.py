# import streamlit to make user interface
import streamlit as st

# Definindo as opções para o radio button
options = ['Apresentation', 'User Manual']

# Configurando a barra lateral (sidebar)
st.sidebar.title('App Options')
choice = st.sidebar.radio('', options)

# Verificação da escolha do usuário e apresentação das imagens ou manual
if choice == 'Apresentation':
    st.image("images/1.png", width=1500)
    st.write("---")
    st.image("images/2.png", width=1500)
    st.write("---")
    st.image("images/3.png", width=1500)
    st.write("---")
    st.image("images/4.png", width=1500)
    st.write("---")
    st.image("images/5.png", width=1500)
    st.write("---")
    st.image("images/6.png", width=1500)
else:
    st.title("User Manual for the Investment Decision Tool")
    st.subheader("Thank you for using our app! This user manual will guide you through the features and functionalities of the app. Please find below a description of each page and its functionalities:")
    st.write("---")
    st.subheader("Stock Analysis:")
    st.markdown("""
On this page, users can analyze and track individual stocks and Indexfunds. Here's how you can use this page:
""")
    st.write("")            
    st.write(" - Choose the desired Indexfunds to visualize.")
    st.write(" - Select a stock from the provided list or enter a specific stock ticker in the designated field.")
    st.write(" - Specify the historical timeframe you wish to analyze using the 'How many days' field.")
    st.write(" - Use the 'Price date' field to check the specific price of the chosen asset at a particular date.")
    st.write(" - Select the desired indicators for the analysis, which will be displayed on the chart.")
    st.write(" - Below the chart, you will find a summary of the chosen ticker, including the return rates within the given time period, the correlation with the Indexfunds, the best performer, the current value of the stock, and a graphical-based prediction.")

    st.write("---")
    st.subheader("Portfolio Analysis:")
    st.markdown("""
This page allows you to analyze your investment portfolio. Follow these steps:""")
    st.write(" - Upload an Excel file containing your portfolio information, including the quantity of shares and the ticker for each asset.")
    st.write(" - Once the file is loaded, a chart representing your portfolio will be generated, indicating the best and worst performing stocks.")
    st.write(" - Specify the historical timeframe you wish to analyze using the 'How many days' field.")
    st.write(" - Below the chart, there will be a summary of the portfolio, including return rates within the specified time period, correlation with Indexfunds, the best performer, and the total value of your investments.")
    st.write("---")
    st.subheader("Price Prediction:")
    st.markdown(""" Here, you can track the future price movement of a specific stock. To utilize this feature:""")
    st.write(" - Choose a stock ticker for analysis.")
    st.write(" - The system will run a prediction based on historical prices and indicators of the stock.")
    st.write(" - The graphical representation will indicate whether the stock has an upward or downward trend.")
    st.write(" - The prediction section will display the estimated price for the following 6 months.")
    st.write("---")
    st.subheader("Stock News:")
    st.markdown("""   
 On this page, you can stay updated with the latest news related to stocks and Indexfunds. Here's how to use this feature:""") 
    st.write(" - Choose the desired Indexfunds to view.")
    st.write(" - Select a stock from the provided list or enter a specific stock ticker in the designated field.")
    st.write(" - Once you make a choice, the page will display the top news articles related to the selected stock, along with links for further reading.")
    st.write("---")
    st.subheader("""We hope this user manual helps you navigate our app effectively. If you have any further questions or need assistance, please don't hesitate to reach out to our support team. Happy investing!""") 
    
      # Coloque aqui o conteúdo do manual, seja texto ou um link para o manual em inglês.