# Project-Stock-Predict

This app can provide users with a reliable tool to assist them in making investment decisions in the stock market. By integrating with financial libraries, cleaning and processing data, and providing interactive visualizations, we strive to empower individuals to make informed investment choices.


# Features:
Stock Analysis: Analyze individual stocks and Indexfunds, including historical data, indicators, and performance comparisons.

Portfolio Analysis: Analyze and track the performance of your investment portfolio, including historical returns and correlation with Indexfunds.

Price Prediction: Get predictions on future stock prices based on historical data and indicators.

Stock News: Stay updated with the latest news related to stocks and Indexfunds

# Installation

1. Clone the repository:
https://github.com/sergiosoutinho/Project-Stock-Predict.git

2. Install the required dependencies:
pip install -r requirements.txt


# How to Use

1. Navigate to the project directory:
cd stock-market-app

2. Run the app:
streamlit run app.py


# User Manual
Stock Analysis:
On this page, users can analyze and track individual stocks and Indexfunds. Here's how you can use this page:

 - Choose the desired Indexfunds to visualize.
 - Select a stock from the provided list or enter a specific stock ticker in the designated field.
 - Specify the historical timeframe you wish to analyze using the 'How many days' field.
 - Use the 'Price date' field to check the specific price of the chosen asset at a particular date.
 - Select the desired indicators for the analysis, which will be displayed on the chart.
 - Below the chart, you will find a summary of the chosen ticker, including the return rates within the given time period, the correlation with the Indexfunds, the best performer, the current value of the stock, and a graphical-based prediction.

Portfolio Analysis:
This page allows you to analyze your investment portfolio. Follow these steps:

 - Upload an Excel file containing your portfolio information, including the quantity of shares and the ticker for each asset.
 - Once the file is loaded, a chart representing your portfolio will be generated, indicating the best and worst performing stocks.
 - Specify the historical timeframe you wish to analyze using the 'How many days' field.
 - Below the chart, there will be a summary of the portfolio, including return rates within the specified time period, correlation with Indexfunds, the best performer, and the total value of your investments.


Price Prediction:
Here, you can track the future price movement of a specific stock. To utilize this feature:

 - Choose a stock ticker for analysis.
 - The system will run a prediction based on historical prices and indicators of the stock.
 - The graphical representation will indicate whether the stock has an upward or downward trend.
 - The prediction section will display the estimated price for the following 6 months.


Stock News:
On this page, you can stay updated with the latest news related to stocks and Indexfunds. Here's how to use this feature:

 - Choose the desired Indexfunds to view.
 - Select a stock from the provided list or enter a specific stock ticker in the designated field.
 - Once you make a choice, the page will display the top news articles related to the selected stock, along with links for further reading.