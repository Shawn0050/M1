#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shawn
"""
#%%
import datetime as dt
import yfinance as yf
import numpy as np
start = dt.datetime(2017,1,1)
end = dt.datetime(2021,12,31)
ticker = ['2454.TW']#2454 聯發科
Asset_MK= yf.download(ticker,start,end)
Adjclose_MK=Asset_MK["Adj Close"]
print(Adjclose_MK)
#(1)請取出聯發科2017年以後的收盤價，並畫成折線圖。
Adjclose_MK.plot(grid=True) #範例10
#(2)請取出聯發科2017年以後的收盤價，並畫成長條圖。
Adjclose_MK.plot(kind='hist',alpha=0.4,bins=50,legend=True)
#(3)請取出聯發科2017年以後的日收益率值，並畫成長條圖。
R_MK=np.log(Adjclose_MK/Adjclose_MK.shift()).dropna(how = 'all')
R_MK.plot(kind='hist',alpha=0.4,bins=50,legend=True)
# %%
