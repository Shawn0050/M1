import pandas as pd
import numpy as np
# 組成
def BP_profits(stock_prices,strike_price,option_premium,fee):
    return np.where(stock_prices < strike_price - fee, (strike_price - stock_prices - fee) - option_premium -fee , -option_premium-fee)
def SP_profits(stock_prices,strike_price,option_premium,fee):
    return np.where(stock_prices > strike_price + fee, option_premium - fee, -((strike_price - stock_prices + fee) - option_premium) - fee)
def BC_profits(stock_prices,strike_price,option_premium,fee):
    return np.where(stock_prices > strike_price + fee, (stock_prices - strike_price - fee) - option_premium -fee , -option_premium - fee)
def SC_profits(stock_prices,strike_price,option_premium,fee):
    return np.where(stock_prices < strike_price - fee , option_premium - fee, -((stock_prices - strike_price + fee) - option_premium)-fee)