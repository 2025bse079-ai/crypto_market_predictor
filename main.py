import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Download Bitcoin data
btc = yf.download("BTC-USD", start="2020-01-01", end="2026-01-01")
btc.columns = btc.columns.get_level_values(0)
btc.to_csv("data/bitcoin.csv")
btc.reset_index(inplace=True)

# ── Feature Engineering ──────────────────────────────────────────────
# Use PREVIOUS day's data to predict TODAY's close (no leakage)
btc['Prev_Close']  = btc['Close'].shift(1)
btc['Prev_Volume'] = btc['Volume'].shift(1)
btc['Prev_High']   = btc['High'].shift(1)
btc['Prev_Low']    = btc['Low'].shift(1)

# Moving averages (lagged, so no leakage)
btc['MA_7']  = btc['Close'].shift(1).rolling(7).mean()
btc['MA_30'] = btc['Close'].shift(1).rolling(30).mean()

# Price momentum
btc['Return_1d'] = btc['Close'].pct_change().shift(1)

# Drop rows with NaN from shifting/rolling
btc.dropna(inplace=True)

# ── Features & Target ────────────────────────────────────────────────
features = ['Prev_Close', 'Prev_Volume', 'Prev_High', 'Prev_Low',
            'MA_7', 'MA_30', 'Return_1d']

X = btc[features]
y = btc['Close']

# ── Time-Based Split (no leakage) ────────────────────────────────────
# 80% train, 20% test — keeping chronological order
split = int(len(btc) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

print(f"Training on {len(X_train)} days, testing on {len(X_test)} days")
print(f"Test period: {btc['Date'].iloc[split].date()} → {btc['Date'].iloc[-1].date()}")

# ── Train Model ───────────────────────────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)

# ── Evaluate ──────────────────────────────────────────────────────────
predictions = model.predict(X_test)

mae   = mean_absolute_error(y_test, predictions)
rmse  = np.sqrt(mean_squared_error(y_test, predictions))
r2    = model.score(X_test, y_test)

print(f"\nModel Evaluation:")
print(f"  R² Score : {r2:.4f}  (how much variance is explained)")
print(f"  MAE      : ${mae:,.2f}  (avg dollar error per prediction)")
print(f"  RMSE     : ${rmse:,.2f}  (penalises large errors more)")

# ── Predictions vs Actual ─────────────────────────────────────────────
results = pd.DataFrame({
    'Date':       btc['Date'].iloc[split:].values,
    'Actual':     y_test.values,
    'Predicted':  predictions
})
print("\nSample Predictions:")
print(results.head(10).to_string(index=False))
# Add this at the end of main.py, after model.fit(...)
import joblib
joblib.dump(model, 'models/btc_model.pkl')
print("Model saved to models/btc_model.pkl")
# Add this at the end of main.py after model.fit()
import json

# Generate predictions on test set
predictions_list = model.predict(X_test).tolist()
actual_list = y_test.tolist()
dates_list = btc['Date'].iloc[split:].dt.strftime('%Y-%m-%d').tolist()

# Save to JSON for the frontend
chart_data = {
    'dates': dates_list,
    'actual': [round(p, 2) for p in actual_list],
    'predicted': [round(p, 2) for p in predictions_list]
}

with open('static/chart_data.json', 'w') as f:
    json.dump(chart_data, f)

print("Chart data saved to static/chart_data.json")