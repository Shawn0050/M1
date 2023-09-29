#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shawn
"""
#indicator_ok0813
def h(n, prices):
    return prices.iloc[-1]['BidHigh'] / prices.iloc[-(n+1)]['BidHigh'] - 1

def l(n, prices):
    return 1- prices.iloc[-1]['BidLow'] / prices.iloc[-(n+1)]['BidLow'] 
def lk(k,n, prices):
    return 1- prices.iloc[-1-k]['BidLow'] / prices.iloc[-(n+1)]['BidLow'] 

def c(n, prices):
    return prices.iloc[-1]['BidClose'] / prices.iloc[-(n+1)]['BidClose'] - 1
def ck(k,n, prices):
    return prices.iloc[-1-k]['BidClose'] / prices.iloc[-(n+1)]['BidClose'] - 1

def v(t, prices): #Volatility Ratio
    return (max(prices.iloc[-(t+1) : -2]['AskHigh']) - min(prices.iloc[-(t+1): -2]['AskLow']))/ prices.iloc[-(t+1)]['AskOpen']

def vv(t, prices): #Volatility Value
    return (max(prices.iloc[-(t+1) : -2]['BTC/USD(High, Ask)']) - min(prices.iloc[-(t+1): -2]['BTC/USD(High, Ask)']))

def hv(n,t, prices): 
    return h(n, prices) / v(t, prices)

def lv(n,t, prices): 
    return l(n, prices) / v(t, prices)

def cv(n,t, prices): 
    return c(n, prices) / v(t, prices)

def maxx(t,prices):
		return max(prices.iloc[-(t+1):-2]['BidHigh'])

def minx(t,prices):
		return min(prices.iloc[-(t+1):-2]['BidLow'])

def hr(t,prices):
		return prices.iloc[-1]['BidHigh'] / maxx(t,prices)- 1

def lr(t,prices):
		return prices.iloc[-1]['BidLow'] / minx(t,prices)- 1