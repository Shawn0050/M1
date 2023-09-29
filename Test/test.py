# %%
a = 2
b = 3 
if a > b-1:
    print('yes')
else:
    print('no')

def run(a,b):
    if a > b-1:
        print('yes')
    else:
        a += 1
        run(a,b)

run(2,3)
# %%
import pandas as pd
def vv(t, prices): #Volatility Value
    return (max(prices.iloc[-(t+1) : -2]['BTC/USD(High, Ask)']) - min(prices.iloc[-(t+1): -2]['BTC/USD(High, Ask)']))
a = pd.read_csv('/Users/shawn/Github/M1/Test/BTC-S.csv')
coefmapping = {
    'ETH-USD': [-0.25,0.4,0.03,4],
    'BTC-USD': [-0.2,0.4,0.02,3]
}
def transcoef(ticker):
    if ticker in coefmapping:
        coef = coefmapping[ticker]
    else:
        coef = "''"  #若無對應的 IG ticker，則填入兩個單引號
    return coef
def check_short_condition(a):
    prices = a #Using FXCM's symbol to get hist
    coef = transcoef('BTC-USD')
    # vlx=fetch_prices_from_fxcm("VOLX").iloc[-1].BidClose
    if prices.iloc[-1]['BTC/USD(Low, Bid)*']<min(prices.iloc[-(115+1):-2]['BTC/USD(Low, Bid)*']) + coef[0]*vv(115, prices) and prices.iloc[-1]['BTC/USD(Close, Bid)*']>min(prices.iloc[-(115+1):-2]['BTC/USD(Low, Bid)*']) + coef[0]*vv(115, prices) :
        print("Check Entry")
    else:
        print('No Entry')
check_short_condition(a)
# %%
import os
import sys
# 取得當前script的絕對路徑
current_script_path = os.path.abspath(sys.argv[0])
# 提取取所需的部分
current_script_directory = os.path.dirname(current_script_path)
csv_file_path = os.path.join(current_script_directory, 'start_time_{}.csv'.format('test'))
try:
    start_time = pd.read_csv(csv_file_path)
except FileNotFoundError:
    # 如果文件不存在，創建一個空的 DataFrame
    start_time = pd.DataFrame(columns=['platform','ticker', 'start','direction','size'])
def test():
    if  start_time.empty:
        print('yes')
test()
# %%
