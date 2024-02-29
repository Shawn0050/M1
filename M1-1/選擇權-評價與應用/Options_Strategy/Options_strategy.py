# %%
import numpy as np
import plotly.graph_objs as go
import nbformat
#Define繪製策略損益圈方法
def draw_PnL(data, title):
    
    fig = go.Figure(data)
    
    #設定畫布屬性
    fig.update_layout(
        title=title,   #圖表標題名稱
        xaxis_title='股價', #x軸標題
        yaxis_title='損益', #y軸標題
        showlegend=True,  #顯示圖例
        plot_bgcolor='white', #底色白色
        xaxis=dict(linecolor='black', linewidth=2),  #x軸線為黑色，寬度=2
        yaxis=dict(linecolor='black', linewidth=2),  #y軸同上
        xaxis_showgrid=True,  #顯示x軸格線
        yaxis_showgrid=True,  #y軸同上
        xaxis_gridcolor='lightgray',  #x軸格線為亮灰色
        yaxis_gridcolor='lightgray',  #y軸同上
        #設定0軸格線為暗灰色
        shapes=[dict(type='line', xref='paper', x0=0, x1=1, y0=0, y1=0, line=dict(color='darkgrey', width=3))],
    )

    #展示圖表
    fig.show()

    return
#初始化參數
option_premium = 8  #Option權利金
strike_price = 75   #履約價格
prices_range = np.array(range(50, 101, 1)) #定義股票價格區間
stock_prices = prices_range #股價
#計算損益
BC75_profits = np.where(stock_prices > strike_price, (stock_prices - strike_price) - option_premium , -option_premium)
stock_profits = stock_prices - strike_price

#建立Plotly損益曲線
trace1 = go.Scatter(x=prices_range,
                    y=stock_profits,
                   mode='lines',
                   name='買入股票損益',
                   line=dict(color='black')
                   )

trace2 = go.Scatter(x=prices_range,
                    y=BC75_profits,
                    mode='lines',
                    name='買入買權損益',
                    line=dict(color='red')
                   )
#匯集所有損益曲線
data = [trace1, trace2]

#繪製策略損益圖
draw_PnL(data, '買入買權與買入股票到期損益之比較圖')
# %%
import numpy as np
import plotly.graph_objs as go
import nbformat
#Define繪製策略損益圈方法
def draw_PnL(data, title):
    
    fig = go.Figure(data)
    
    #設定畫布屬性
    fig.update_layout(
        title=title,   #圖表標題名稱
        xaxis_title='股價', #x軸標題
        yaxis_title='損益', #y軸標題
        showlegend=True,  #顯示圖例
        plot_bgcolor='white', #底色白色
        xaxis=dict(linecolor='black', linewidth=2),  #x軸線為黑色，寬度=2
        yaxis=dict(linecolor='black', linewidth=2),  #y軸同上
        xaxis_showgrid=True,  #顯示x軸格線
        yaxis_showgrid=True,  #y軸同上
        xaxis_gridcolor='lightgray',  #x軸格線為亮灰色
        yaxis_gridcolor='lightgray',  #y軸同上
        #設定0軸格線為暗灰色
        shapes=[dict(type='line', xref='paper', x0=0, x1=1, y0=0, y1=0, line=dict(color='darkgrey', width=3))],
    )

    #展示圖表
    fig.show()

    return
#初始化參數
put75_premium = 8  #Option權利金
put70_premium = 6  #Option權利金
put75strike_price = 75   #履約價格
put70strike_price = 70   #履約價格
prices_range = np.array(range(45, 101, 1)) #定義股票價格區間
stock_prices = prices_range #股價
#計算損益
SP70_profits = np.where(stock_prices > put70strike_price, put70_premium , -(put70strike_price - stock_prices) + put70_premium)
BP75_profits = np.where(stock_prices < put75strike_price, (put75strike_price - stock_prices) - put75_premium , -put75_premium)
stock_profits = stock_prices - strike_price
strategy = SP70_profits + BP75_profits
#建立Plotly損益曲線
trace1 = go.Scatter(x=prices_range,
                    y=SP70_profits,
                   mode='lines',
                   name='賣出低履約價賣權損益',
                   line=dict(color='black')
                   )

trace2 = go.Scatter(x=prices_range,
                    y=BP75_profits,
                    mode='lines',
                    name='買入高履約價賣權損益',
                    line=dict(color='red')
                   )

trace3 = go.Scatter(x=prices_range,
                    y=strategy,
                    mode='lines',
                    name='策略總損益',
                    line=dict(color='blue')
                   )
#匯集所有損益曲線
data = [trace1, trace2, trace3]

#繪製策略損益圖
draw_PnL(data, '賣權空頭價差策略')
# %%
