import yfinance as yf
import pandas as pd

# 定義股票代碼
nasdaq_symbol = "TSLA"  # NASDAQ 100 的代碼
bitcoin_symbol = "BTC-USD"  # 比特幣的代碼

# 獲取過去 10 年的歷史數據
end_date = pd.Timestamp.now()
start_date = end_date - pd.DateOffset(years=5)

nasdaq_data = yf.download(nasdaq_symbol, start=start_date, end=end_date)['Close']
bitcoin_data = yf.download(bitcoin_symbol, start=start_date, end=end_date)['Close']

# 結合數據並計算相關係數
combined_data = pd.DataFrame({'NASDAQ': nasdaq_data, 'Bitcoin': bitcoin_data})
correlation = combined_data.corr()

print(correlation)
