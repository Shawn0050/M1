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