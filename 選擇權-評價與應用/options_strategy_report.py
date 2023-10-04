# %%
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import nbformat
#Define繪製策略損益圈方法
def draw_PnL_payoff(data, title):
    
    fig = go.Figure(data)
    
    #設定畫布屬性
    fig.update_layout(
        title=title,   #圖表標題名稱
        xaxis_title='股價', #x軸標題
        yaxis_title='只有報酬', #y軸標題
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
def draw_PnL_withpremium(data, title):
    
    fig = go.Figure(data)
    
    #設定畫布屬性
    fig.update_layout(
        title=title,   #圖表標題名稱
        xaxis_title='股價', #x軸標題
        yaxis_title='到期損益（不含手續費）', #y軸標題
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
def draw_PnL_withpremiumandfees(data, title):
    
    fig = go.Figure(data)
    
    #設定畫布屬性
    fig.update_layout(
        title=title,   #圖表標題名稱
        xaxis_title='股價', #x軸標題
        yaxis_title='到期損益', #y軸標題
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
# 組成
def BP_profits(stock_prices,strike_price,option_premium,fee):
    return np.where(stock_prices < strike_price - fee, (strike_price - stock_prices - fee) - option_premium -fee , -option_premium-fee)
def SP_profits(stock_prices,strike_price,option_premium,fee):
    return np.where(stock_prices > strike_price + fee, option_premium - fee, -((strike_price - stock_prices + fee) - option_premium) - fee)
def BC_profits(stock_prices,strike_price,option_premium,fee):
    return np.where(stock_prices > strike_price + fee, (stock_prices - strike_price - fee) - option_premium -fee , -option_premium - fee)
def SC_profits(stock_prices,strike_price,option_premium,fee):
    return np.where(stock_prices < strike_price - fee , option_premium - fee, -((stock_prices - strike_price + fee) - option_premium)-fee)
def long_call_spread(call_premium,call_strike_price,stock_prices,strategy_name):
    stock_prices = stock_prices
    strike_price = call_strike_price[0]
    option_premium = call_premium[0]
    fee = 0
    a = BC_profits(stock_prices,strike_price,option_premium,fee)
    stock_prices = stock_prices
    strike_price = call_strike_price[1]
    option_premium = call_premium[1]
    fee = 0
    b = SC_profits(stock_prices,strike_price,option_premium,fee)
    c = a + b
    trace1 = go.Scatter(x=prices_range,
                    y=a,
                   mode='lines',
                   name='+C',
                   line=dict(color='blue', dash='dash')
                   )
    trace2 = go.Scatter(x=prices_range,
                y=b,
                mode='lines',
                name='-C',
                line=dict(color='red', dash='dash')
                )
    trace3 = go.Scatter(x=prices_range,
                y=c,
                mode='lines',
                name='Strategy',
                line=dict(color='green')
                )
    data = [trace1, trace2, trace3]
    draw_PnL_withpremium(data, strategy_name)
    df = pd.DataFrame()
    df['策略'] = ['+C','-C']
    df['履約價格'] = [call_strike_price[0],call_strike_price[1]]
    df['權利金點數'] = [call_premium[0],call_premium[1]]
    print(df)
    # 含手續費
    # fee = int(input('單邊手續費'))
    # stock_prices = stock_prices
    # strike_price = call_strike_price[0]
    # option_premium = call_premium[0]
    # a = BC_profits(stock_prices,strike_price,option_premium,fee)
    # strike_price = call_strike_price[1]
    # option_premium = call_premium[1]
    # b = SC_profits(stock_prices,strike_price,option_premium,fee)
    # c = a + b
    # trace1 = go.Scatter(x=prices_range,
    #             y=a,
    #             mode='lines',
    #             name='+C',
    #             line=dict(color='blue')
    #             )
    # trace2 = go.Scatter(x=prices_range,
    #             y=b,
    #             mode='lines',
    #             name='-C',
    #             line=dict(color='red')
    #             )
    # trace3 = go.Scatter(x=prices_range,
    #             y=c,
    #             mode='lines',
    #             name='Strategy',
    #             line=dict(color='green')
    #             )
    # data = [trace1, trace2, trace3]
    # draw_PnL_withpremiumandfees(data, strategy_name)

def long_put_spread(put_premium,put_strike_price,stock_prices,strategy_name):
    stock_prices = stock_prices
    strike_price = put_strike_price[0]
    option_premium = put_premium[0]
    fee = 0
    a = BP_profits(stock_prices,strike_price,option_premium,fee)
    stock_prices = stock_prices
    strike_price = put_strike_price[1]
    option_premium = put_premium[1]
    fee = 0
    b = SP_profits(stock_prices,strike_price,option_premium,fee)
    c = a + b
    trace1 = go.Scatter(x=prices_range,
                    y=a,
                   mode='lines',
                   name='+P',
                   line=dict(color='lightblue')
                   )
    trace2 = go.Scatter(x=prices_range,
                y=b,
                mode='lines',
                name='-P',
                line=dict(color='red')
                )
    trace3 = go.Scatter(x=prices_range,
                y=c,
                mode='lines',
                name='Strategy',
                line=dict(color='green')
                )
    data = [trace1, trace2, trace3]
    draw_PnL_withpremium(data, strategy_name)
    # 含手續費
    # fee = int(input('單邊手續費'))
    # stock_prices = stock_prices
    # strike_price = put_strike_price[0]
    # option_premium = put_premium[0]
    # a = BP_profits(stock_prices,strike_price,option_premium,fee)
    # strike_price = put_strike_price[1]
    # option_premium = put_premium[1]
    # b = SP_profits(stock_prices,strike_price,option_premium,fee)
    # c = a + b
    # trace1 = go.Scatter(x=prices_range,
    #             y=a,
    #             mode='lines',
    #             name='+P',
    #             line=dict(color='blue')
    #             )
    # trace2 = go.Scatter(x=prices_range,
    #             y=b,
    #             mode='lines',
    #             name='-P',
    #             line=dict(color='red')
    #             )
    # trace3 = go.Scatter(x=prices_range,
    #             y=c,
    #             mode='lines',
    #             name='Strategy',
    #             line=dict(color='green')
    #             )
    # data = [trace1, trace2, trace3]
    # draw_PnL_withpremiumandfees(data, strategy_name)

def spread(call_premium,call_strike_price,put_premium,put_strike_price,stock_prices,strategy_name):
    stock_prices = stock_prices
    strike_price = put_strike_price[0]
    option_premium = put_premium[0]
    fee = 0
    a = BP_profits(stock_prices,strike_price,option_premium,fee)
    stock_prices = stock_prices
    strike_price = put_strike_price[1]
    option_premium = put_premium[1]
    fee = 0
    b = SP_profits(stock_prices,strike_price,option_premium,fee)
    stock_prices = stock_prices
    strike_price = call_strike_price[0]
    option_premium = call_premium[0]
    fee = 0
    c = BC_profits(stock_prices,strike_price,option_premium,fee)
    stock_prices = stock_prices
    strike_price = call_strike_price[1]
    option_premium = call_premium[1]
    fee = 0
    d = SC_profits(stock_prices,strike_price,option_premium,fee)
    e = a + b + c + d
    trace1 = go.Scatter(x=prices_range,
                    y=a,
                   mode='lines',
                   name='+P',
                   line=dict(color='blue', dash='dash')
                   )
    trace2 = go.Scatter(x=prices_range,
                y=b,
                mode='lines',
                name='-P',
                line=dict(color='red', dash='dash')
                )
    trace3 = go.Scatter(x=prices_range,
                    y=c,
                   mode='lines',
                   name='+C',
                   line=dict(color='lightblue', dash='dash')
                   )
    trace4 = go.Scatter(x=prices_range,
                y=d,
                mode='lines',
                name='-C',
                line=dict(color='pink', dash='dash')
                )
    trace5 = go.Scatter(x=prices_range,
                y=e,
                mode='lines',
                name='Strategy',
                line=dict(color='green')
                )
    data = [trace1, trace2, trace3, trace4, trace5]
    draw_PnL_withpremium(data, strategy_name)
    df = pd.DataFrame()
    df['策略'] = ['+P','-P','+C','-C']
    df['履約價格'] = [put_strike_price[0],put_strike_price[1],call_strike_price[0],call_strike_price[1]]
    df['權利金點數'] = [put_premium[0], put_premium[1], call_premium[0],call_premium[1]]
    print(df)
    # 含手續費
    # fee = int(input('單邊手續費'))
    # stock_prices = stock_prices
    # strike_price = put_strike_price[0]
    # option_premium = put_premium[0] 
    # a = BP_profits(stock_prices,strike_price,option_premium,fee)
    # stock_prices = stock_prices
    # strike_price = put_strike_price[1]
    # option_premium = put_premium[1] 
    # b = SP_profits(stock_prices,strike_price,option_premium,fee)
    # stock_prices = stock_prices
    # strike_price = call_strike_price[0]
    # option_premium = call_premium[0] 
    # c = BC_profits(stock_prices,strike_price,option_premium,fee)
    # stock_prices = stock_prices
    # strike_price = call_strike_price[1]
    # option_premium = call_premium[1] 
    # d = SC_profits(stock_prices,strike_price,option_premium,fee)
    # e = a + b + c + d
    # trace1 = go.Scatter(x=prices_range,
    #                 y=a,
    #                mode='lines',
    #                name='+P',
    #                line=dict(color='blue')
    #                )
    # trace2 = go.Scatter(x=prices_range,
    #             y=b,
    #             mode='lines',
    #             name='-P',
    #             line=dict(color='red')
    #             )
    # trace3 = go.Scatter(x=prices_range,
    #                 y=c,
    #                mode='lines',
    #                name='+C',
    #                line=dict(color='lightblue')
    #                )
    # trace4 = go.Scatter(x=prices_range,
    #             y=d,
    #             mode='lines',
    #             name='-C',
    #             line=dict(color='pink')
    #             )
    # trace5 = go.Scatter(x=prices_range,
    #             y=e,
    #             mode='lines',
    #             name='Strategy',
    #             line=dict(color='green')
    #             )
    # data = [trace1, trace2, trace3, trace4, trace5]
    # draw_PnL_withpremiumandfees(data, strategy_name)

strategy_name = input(str('策略名稱：（買權多頭價差or賣權多頭價差or投資組合）'))
if strategy_name == '買權多頭價差':
    # premium
    call1_premium = float(input('Call1權利金：'))
    call2_premium = float(input('Call2權利金：'))
    # strike_price
    call1_strike_price = float(input('Call1履約價：'))
    call2_strike_price = float(input('Call2履約價：'))
    call_premium = [call1_premium, call2_premium]
    call_strike_price = [call1_strike_price, call2_strike_price]
    # 定義股票價格區間
    prices_range = np.array(range(15500, 17000, 1))
    stock_prices = prices_range
    long_call_spread(call_premium,call_strike_price,stock_prices,strategy_name)
if strategy_name == '賣權多頭價差': 
    # premium
    put1_premium = float(input('Put1權利金：'))
    put2_premium = float(input('Put2權利金：'))
    # strike_price
    put1_strike_price = float(input('Put1履約價：'))
    put2_strike_price = float(input('Put2履約價：'))
    put_premium = [put1_premium, put2_premium]
    put_strike_price = [put1_strike_price, put2_strike_price]
    # 定義股票價格區間
    prices_range = np.array(range(15500, 17000, 1))
    stock_prices = prices_range
    long_put_spread(put_premium,put_strike_price,stock_prices,strategy_name)
if strategy_name == '投資組合':
    # premium
    call1_premium = float(input('Call1權利金：'))
    call2_premium = float(input('Call2權利金：'))
    # strike_price
    call1_strike_price = float(input('Call1履約價：'))
    call2_strike_price = float(input('Call2履約價：'))
    call_premium = [call1_premium, call2_premium]
    call_strike_price = [call1_strike_price, call2_strike_price]
    # premium
    put1_premium = float(input('Put1權利金：'))
    put2_premium = float(input('Put2權利金：'))
    # strike_price
    put1_strike_price = float(input('Put1履約價：'))
    put2_strike_price = float(input('Put2履約價：'))
    put_premium = [put1_premium, put2_premium]
    put_strike_price = [put1_strike_price, put2_strike_price]
    # 定義股票價格區間
    prices_range = np.array(range(15500, 17000, 1))
    stock_prices = prices_range
    spread(call_premium,call_strike_price,put_premium,put_strike_price,stock_prices,strategy_name)
# %%
