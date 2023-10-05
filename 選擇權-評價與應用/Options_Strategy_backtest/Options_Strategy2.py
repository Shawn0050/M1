# 10/31完成回測\\商品：週選or月選、交易成本＆滑價成本（進出共3點）
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import datetime as dt

atm_df = pd.read_csv()
pcr_df = pd.read_csv()
settledate_df = pd.read_csv()

atm_df['日期'] = pd.to_datetime(atm_df['日期'])
pcr_df['日期'] = pd.to_datetime(pcr_df['日期'])
settledate_df['日期'] = pd.to_datetime(settledate_df['日期'])

trading_cost = 3

atm_df.loc[0, '價平買權近週報酬'] = 0
atm_df.loc[0, '價平賣權次週報酬'] = 0

atm_df['價平買權近週報酬（金額）'] = atm_df['價平買權近週報酬']*50
atm_df['價平賣權次週報酬（金額）'] = atm_df['價平買權近週報酬']*50

capital = 1000000
#
# 策略邏輯
#
atm_df.loc[0, '策略累積資金'] = capital

for i in range(1, len(atm_df)):
    atm_df.loc[i, '策略累積資金'] = atm_df.loc[i-1, '策略累積資金'] + atm_df.loc[i, '策略損益']

atm_df['策略每日報酬率'] = atm_df['策略累積資金'].pct_change()
atm_df.loc[0, '策略每日報酬率'] = 0

atm_df['策略累積報酬率'] = (1 + atm_df['策略每日報酬率']).cumprod() - 1
atm_df.loc[0, '策略累積報酬率'] = 0

atm_df['每個時點最大累積資金'] = atm_df['策略累積資金'].cummax()
# DD
atm_df['回測比率'] = (atm_df['策略累積資金'] - atm_df['每個時點最大累積資金']) / capital

# plotly
from plotly.subplots import make_subplots
def draw_PnL(trace1,trace2,title1,title2):
    fig = make_subplots(rows=2,cols=1,subplot_titles=(title1,title2),row_heights=(0.75,0.25),
                        shared_xaxes=True,shared_yaxes=True)
    fig.add_trace(trace1,row=1,col=1)
    fig.add_trace(trace2,row=2,col=1)

    fig.update_layout(
                    title = '策略績效',
                    showlegend=True,
                    plot_becolor='while'
                )

    fig.update_xaxes(row=1,col=1,title='日期')
    fig.update_yaxes(title='金額')






