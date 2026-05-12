# ₿ Crypto Market Predictor

A machine learning web application that predicts Bitcoin closing price based on previous day market data.

## About

This system uses a Linear Regression model trained on real Bitcoin historical data from 2020 to 2024, downloaded via Yahoo Finance. Given the previous day market indicators, it predicts the next day closing price and displays the result through a web interface.

## Features

- Predicts Bitcoin closing price from 7 market indicators
- Interactive web interface built with HTML, CSS and JavaScript
- REST API built with Flask
- Charts showing Actual vs Predicted prices
- Feature importance visualization

## Model Results

- Algorithm: Linear Regression
- R² Score: 0.9686
- MAE: $1,611.87
- RMSE: $2,202.23
- Training days: 1,729
- Test days: 433
- Test period: 2024-10-25 to 2025-12-31

## How to Run

1. Install dependencies
   pip install -r requirements.txt

2. Train the model
   python main.py

3. Start the web app
   python app.py

4. Open in browser
   http://127.0.0.1:5000

## Technologies Used

- Python
- Scikit-learn
- Flask
- Pandas
- YFinance
- Chart.js

## Author

GROUP 14