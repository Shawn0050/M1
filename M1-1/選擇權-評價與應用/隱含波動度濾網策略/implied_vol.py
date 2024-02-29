# %%
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go  # 載入plotly套件
import numpy as np              # 載入numpy套件
import pandas as pd             # 載入pandas套件
import datetime as dt           # 載入datetime套件

def fetch_prices(ticker):
    dfs = yf.Ticker(ticker)
    start = '2020-01-01'
    end = '2023-09-01'
    hist = dfs.history(start=start, end=end, interval='1d')
    return hist

a = fetch_prices('^TWII')
a['Close'] = round(a['Close'], 2)

# 将日期时间格式转换为 'YYYY/MM/DD'
a.index = a.index.strftime('%Y-%m-%d')
a['日期'] = a.index
a.index = range(len(a))
a = a[['日期','Close']]
# 找到的
new_data = {'日期': '2021-04-06', 'Close': 16571.28}  # Close的值用'2021-04-0x'（有值的前一期，把判斷式刪掉了）帶入
# 将新行数据转换为DataFrame
new_row = pd.DataFrame(new_data, index=[0])
a = pd.concat([a, new_row]).sort_values(by='日期').reset_index(drop=True)
print(a)

atm_df = pd.read_csv('atm_option_settle.csv')
atm_df['日期'] = pd.to_datetime(atm_df['日期'])
atm_df['日期'] = atm_df['日期'].dt.strftime('%Y-%m-%d')
print(atm_df)


# %%
merged_df = pd.merge(a, atm_df, on="日期", how="inner")
merged_df

# %%
merged_df['Implied volatility of Call'] = 0
merged_df['Implied volatility of Put']  = 0
for i in range(0,len(merged_df)):
    merged_df['Implied volatility of Call'][i] = merged_df['價平買權次週每日結算價'][i]/0.4/merged_df['Close'][i]/((7/365)**0.5)
    # print(merged_df['Implied volatility of Call'][i])
    merged_df['Implied volatility of Put'][i] = merged_df['價平賣權次週每日結算價'][i]/0.4/merged_df['Close'][i]/((7/365)**0.5)

# %%
merged_df

# %%
merged_df['Signal of Long Call'] = 0
merged_df['Signal of Long Put'] = 0
print(merged_df['Implied volatility of Call'].mean())
print(merged_df['Implied volatility of Put'].mean())
for i in range(0,len(merged_df)):
    # if merged_df['Implied volatility of Call'][i] > merged_df['Implied volatility of Call'].mean():
    if merged_df['Implied volatility of Call'][i] > 0.25:
        merged_df['Signal of Long Call'][i] = 1 
    else:
        merged_df['Signal of Long Call'][i] = 0
    # if merged_df['Implied volatility of Put'][i] > merged_df['Implied volatility of Put'].mean():
    if merged_df['Implied volatility of Put'][i] > 0.2:
        merged_df['Signal of Long Put'][i] = 1 
    else:
        merged_df['Signal of Long Put'][i] = 0
merged_df

# %%
merged_df['Signal of Long Call_E'] = 0
merged_df['Signal of Long Put_E'] = 0
prev_value1 = 0  # 儲存上一個非NaN值的index
prev_value2 = 0  # 儲存上一個非NaN值的index

for i in range(len(merged_df)):
    if not pd.isna(merged_df['價平買權次週每日結算價'][i]):  # 檢查a['1']是否為NA
        merged_df['Signal of Long Call_E'][i] = merged_df['Signal of Long Call'][i]
        prev_value1 = i
    else:
        merged_df['Signal of Long Call_E'][i] = merged_df['Signal of Long Call'][prev_value1]
        
    if not pd.isna(merged_df['價平賣權次週每日結算價'][i]):  # 檢查a['1']是否為NA
        merged_df['Signal of Long Put_E'][i] = merged_df['Signal of Long Put'][i]
        prev_value2 = i
    else:
        merged_df['Signal of Long Put_E'][i] = merged_df['Signal of Long Put'][prev_value2]
merged_df

# %%
# 測試用
# import pandas as pd
# import numpy as np

# data = {'1': [82, np.nan, np.nan, np.nan, 62, np.nan, np.nan, np.nan, 93, np.nan, np.nan, np.nan],
#         '2': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}

# a = pd.DataFrame(data)
# a['3'] = 0

# prev_value = 0  # 儲存上一個非NaN值的index

# for i in range(len(a)):
#     if not pd.isna(a['1'][i]):  # 檢查a['1']是否為NA
#         a['3'][i] = a['2'][i]
#         prev_value = i
#     else:
#         a['3'][i] = a['2'][prev_value]

# result = a['3'].tolist()
# print(result)
# print(a)


# %%
merged_df.to_csv('/Users/shawn/Github/M1/價內shortPut策略程式/ck.csv')

# %%
# +Call
capital = 1000000
# 初始化策略累積資金
merged_df.loc[0, '策略累積資金(金額)'] = capital
results = []
merged_df.loc[0, '進場口數'] = 4

for i in range(1,len(merged_df['價平買權次週每日結算價'])):
    B = merged_df['價平買權次週每日結算價'][i - 1]
    B1 = merged_df['Signal of Long Call_E'][i - 1]
    C = merged_df['價平買權近週每日結算價'][i]

    if B*B1 > 1:
        result = round(C - B - 3 , 2)
        merged_df['進場口數'][i-1] = round(merged_df.loc[i-1, '策略累積資金(金額)']/250000)

    else:
        C_prev = merged_df['價平買權近週每日結算價'][i-1]
        result = round(C - C_prev , 2)*B1
        
    merged_df['進場口數'][i] = merged_df['進場口數'][i-1]
    merged_df.loc[i, '策略累積資金(金額)'] = merged_df.loc[i-1, '策略累積資金(金額)']+result*merged_df['進場口數'][i-1]*50
    
    results.append(result)

results.insert(0, 0)
print(results)
merged_df['策略近週報酬(點數)'] = results

# 總報酬率: 55.81%
# 年化報酬率: 13.36%
# 年化波動率: 19.89%
# 年化夏普值: 0.67
# 最大回撤(MDD): -20.88%

# %%
# # +Put
# capital = 1000000
# # 初始化策略累積資金
# merged_df.loc[0, '策略累積資金(金額)'] = capital
# results = []
# merged_df.loc[0, '進場口數'] = 4

# for i in range(1,len(merged_df['價平賣權次週每日結算價'])):
#     B = merged_df['價平賣權次週每日結算價'][i - 1]
#     B1 = merged_df['Signal of Long Put_E'][i - 1]
#     C = merged_df['價平賣權近週每日結算價'][i]

#     if B*B1 > 1:
#         result = round(C - B - 3 , 2)
#         merged_df['進場口數'][i-1] = round(merged_df.loc[i-1, '策略累積資金(金額)']/250000)

#     else:
#         C_prev = merged_df['價平賣權近週每日結算價'][i-1]
#         result = round(C - C_prev , 2)*B1
        
#     merged_df['進場口數'][i] = merged_df['進場口數'][i-1]
#     merged_df.loc[i, '策略累積資金(金額)'] = merged_df.loc[i-1, '策略累積資金(金額)']+result*merged_df['進場口數'][i-1]*50
    
#     results.append(result)

# results.insert(0, 0)
# print(results)
# # results = [-x for x in results]
# merged_df['策略近週報酬(點數)'] = results

# # 總報酬率: -23.79%
# # 年化報酬率: -7.4%
# # 年化波動率: 25.7%
# # 年化夏普值: -0.29
# # 最大回撤(MDD): -52.98%

# %%
# # +call-put
# capital = 1000000
# # 初始化策略累積資金
# merged_df.loc[0, '策略累積資金(金額)'] = capital
# results1 = []
# merged_df.loc[0, 'Call進場口數'] = 2
# results2 = []
# merged_df.loc[0, 'Put進場口數'] = 2

# for i in range(1,len(merged_df['價平買權次週每日結算價'])):
#     B = merged_df['價平買權次週每日結算價'][i - 1]
#     B1 = merged_df['Signal of Long Call_E'][i - 1]
#     C = merged_df['價平買權近週每日結算價'][i]

#     X = merged_df['價平賣權次週每日結算價'][i - 1]
#     X1 = merged_df['Signal of Long Put_E'][i - 1]
#     Y = merged_df['價平賣權近週每日結算價'][i]

#     if B*B1 > 1:
#         result1 = round(C - B - 3 , 2)
#         merged_df['Call進場口數'][i-1] = round(merged_df.loc[i-1, '策略累積資金(金額)']/250000)

#     else:
#         C_prev = merged_df['價平買權近週每日結算價'][i-1]
#         result1 = round(C - C_prev , 2)*B1

#     if X*X1 > 1:
#         result2 = round(Y - X - 3 , 2)
#         merged_df['Put進場口數'][i-1] = round(merged_df.loc[i-1, '策略累積資金(金額)']/250000)

#     else:
#         Y_prev = merged_df['價平賣權近週每日結算價'][i-1]
#         result2 = round(Y_prev - Y , 2)*X1
        
#     merged_df['Call進場口數'][i] = merged_df['Call進場口數'][i-1]
#     merged_df['Put進場口數'][i] = merged_df['Put進場口數'][i-1]
#     merged_df.loc[i, '策略累積資金(金額)'] = merged_df.loc[i-1, '策略累積資金(金額)']+result1*merged_df['Call進場口數'][i-1]*50+result2*merged_df['Put進場口數'][i-1]*50
    
#     results1.append(result1)
#     results2.append(result2)

# results1.insert(0, 0)
# results2.insert(0, 0)

# # results = [-x for x in results]
# merged_df['Call策略近週報酬(點數)'] = results1
# merged_df['Put策略近週報酬(點數)'] = results2

# 總報酬率: 63.67%
# 年化報酬率: 14.95%
# 年化波動率: 26.3%
# 年化夏普值: 0.57
# 最大回撤(MDD): -28.99%

# %%
merged_df.to_csv('/Users/shawn/Github/M1/價內shortPut策略程式/IV_CallPut.csv')
merged_df['策略累積資金(金額)'].plot()

# %%
backtest_df = merged_df
backtest_df['策略每日報酬率'] = backtest_df['策略累積資金(金額)'].pct_change()
backtest_df.loc[0, '策略每日報酬率'] = 0  # 初始化第一天策略每日報酬率

# 計算累積報酬率
backtest_df['策略累積報酬率'] = (1 + backtest_df['策略每日報酬率']).cumprod()-1
backtest_df.loc[0, '策略累積報酬率'] = 0  # 初始化第一天策略累積報酬率

# 計算Drawdown
# 計算每個時間點的最大價格
backtest_df['每個時點最大策略累積資金(金額)'] = backtest_df['策略累積資金(金額)'].cummax()
# 計算每個時間點的 Drawdown
backtest_df['Drawdown'] = (backtest_df['策略累積資金(金額)'] - backtest_df['每個時點最大策略累積資金(金額)']) / backtest_df['每個時點最大策略累積資金(金額)']
# backtest_df.to_csv('/Users/shawn/Github/M1/價內shortPut策略程式/backtest.csv')
backtest_df.head(5)

# %%
from plotly.subplots import make_subplots  #載入plotly畫子圖的套件

# 定義繪製策略損益圖方法
def draw_PnL(trace1, trace2,  title1, title2):
    
    # 打開子畫布
    fig = make_subplots(rows=2, cols=1, subplot_titles=(title1, title2), row_heights=[0.75, 0.25], shared_xaxes=True, vertical_spacing=0.1)
    
    # 帶入資料到子畫布的特定位置
    fig.add_trace(trace1, row=1, col=1)
    fig.add_trace(trace2, row=2, col=1)
    
    # 設定子畫布共同屬性
    fig.update_layout(
        title='做空賣權策略績效', # 設定圖表標題名稱
        plot_bgcolor='white', # 設定底色為白色
    )
    
    # 設定子畫布屬性
    fig.update_xaxes(row=1, col=1, linecolor='black', linewidth=2, showgrid=True, gridcolor='lightgrey')
    fig.update_yaxes(title_text="損益(%)", row=1, col=1, linecolor='black', linewidth=2, showgrid=True, gridcolor='lightgrey', zerolinecolor='darkgrey')
    fig.update_xaxes(title_text="日期", row=2, col=1, linecolor='black', linewidth=2, showgrid=True, gridcolor='lightgrey')
    fig.update_yaxes(title_text="損益(%)", row=2, col=1, linecolor='black', linewidth=2, showgrid=True, gridcolor='lightgrey', zerolinecolor='darkgrey')

    #展示圖表
    fig.show()
    
    return

# %%
# 建立plotly損益曲線
trace1 = go.Scatter(x=backtest_df['日期'], 
                    y=backtest_df['策略累積報酬率']*100, 
                    mode='lines', 
                    name='做空賣權策略損益', 
                    line=dict(color='blue')
                    )
trace2 = go.Scatter(x=backtest_df['日期'], 
                    y=backtest_df['Drawdown']*100, 
                    mode='lines', 
                    name='Drawdown', 
                    line=dict(color='red')
                    )

# 繪製策略損益圖
draw_PnL(trace1, trace2, '策略損益曲線', 'Drawdown')

# %%
# 計算績效指標
total_return = backtest_df.loc[len(backtest_df)-1, '策略累積報酬率']
annualized_return = (1+backtest_df.loc[len(backtest_df)-1, '策略累積報酬率'])**(252/len(backtest_df))-1  # 年化報酬率
annualized_volatility = np.std(backtest_df['策略每日報酬率'])*np.sqrt(252)  # 年化波動率
sharpe_ratio = annualized_return/annualized_volatility  # 年化夏普值
max_drawdown = backtest_df['Drawdown'].min()  # 最大回撤(MDD)

print("總報酬率: {}%".format(round(total_return*100,2)))
print("年化報酬率: {}%".format(round(annualized_return*100,2)))
print("年化波動率: {}%".format(round(annualized_volatility*100,2)))
print("年化夏普值: {}".format(round(sharpe_ratio,2))) 
print("最大回撤(MDD): {}%".format(round(max_drawdown*100,2)))


