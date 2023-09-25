#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shawn
"""
#%%
a=input("name1:")
b=input("name2:")
print(a,'and',b ,"are good friend")

c=float(input("Please enter your height (cm):"))
d=float(input("Please enter your weight (kg):"))
c=c/100
BMI=d/(c*c)
print("Your BMI is",BMI)

total_second = int(input())
hour = total_second // 3600
minute = (total_second % 3600) // 60
second = total_second % 60
print(str(hour) + ':' + str(minute) + ':' + str(second))

# %%
# 個人參數輸入
age = int(input("年紀："))
pregnant = input("懷孕與否 (True /False)：") #不能用 bool(input("懷孕與否 (True/False)：")
indigenous = input("是否有原住民身份(True/False)：")
casel = (age >= 75)
# 年紀已達 75歲
case2 = (pregnant =='True')
# 懷孕
case3 = ((indigenous == "TRUE") and (age >= 65)) #具原民身分且年紀已達 65歲
print (age)
print (pregnant)
print (indigenous )
result = (casel or case2 or case3)
# 輸出結果
print("The result is " + str(result) + "!")

# %%
print('Please Enter Your Income:')
income = float(input())
if income <= 10000:
    tax= 0.2*income
else:
    tax= 0.08*(income-10000)+200
print('tax amounat:$' +str(tax))
# %%
year = int(input("欲查詢年份："))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("閏年")
        else:
            print("平年")
    else:
        print("閏年")
else:
    print("平年")
# %%
key = input("continue? ")

if not (key == "y" or key == 'Y'):
    print("Game over!")
# %%
# GPA
midterm_por = 0.4
final_por = 0.6
gpa = 'A'

withdraw = input('停修(T/F):')

if withdraw == 'TRUE':
    gpa = 'X'
else:
    midterm = float(input('期中成績：'))
    final = float(input('期末成績：'))
    bonus = input('加分作業(T/F):')

    score = midterm*midterm_por + final*final_por

    if (score < 60) and (bonus == 'False'):
        gpa = 'F'
    elif score < 70:
        gpa = 'C'
    elif (score < 80) and (bonus == 'False'):
        gpa = 'B'
    else:
        gpa = 'A'

print('gpa = ',gpa)
# %%
# 數列問題:給定一個長度為三的數列,請判斷其是否為一嚴格遞增數列,並將三個數字以逗號分開。
n1 = int(input('n1:'))
n2 = int(input('n2:'))
n3 = int(input('n3:'))
print(n1, n2, n3, sep= ',', end='  ') # end = '<空格>'
if n1 < n2 and n2 < n3:
    print('是嚴格遞增數列')
else:
    print('不是嚴格遞增數列')
# %%
# 財力證明: 「Let me 貸」銀行貸款給客戶時,要求客戶提出新台幣 20000 元
# 的財力證明。假設一美金可換新臺幣 30 元,一臺幣可換日幣 4 圓。給定一整
# 數金額,及一表示幣種的字串(U:美金,N:臺幣,Y:日幣)。若財力大於
# 等於新臺幣 20000 元,請輸出「貸」,反之請輸出「Don’t 貸」。
ntd = int(input('所得（美金U/日圓Y)：'))
cur = input('幣別：')

if cur == 'U':
    ntd *= 30
if cur == 'Y':
    ntd /= 4

if ntd >= 20000:
    print('貸')
else:
    print('Don’t 貸」')


# %%
# Nand: 除了 and、or、not 以外,有另一個邏輯符號叫做 nand,不過 Python
# 似乎沒有這個運算子。nand 的輸入與輸出表格如下圖。給定兩個輸入 a、b
# (其 value 只會是 T 與 F,分別代表 True 與 False),請輸出 a nand b 的結果。
a = input('T/F:')
b = input('T/F:')

print(not(a == 'T' and b == 'T'))
# %%
# fetch price from yfinance
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn
data = yf.Ticker('AAPL') 
AAPL = data.history(period='D', start='2019-1-1', end='2023-1-1')
print(AAPL)
print(len(AAPL))
AAPL['Close'].value_counts().to_frame()
AAPL.describe()

seaborn.set()
plt.figure(figsize=(16,9))
AAPL['Close'].plot()

AAPL.to_csv('/Users/shawn/Desktop/AAPL.csv')
# %%
import pandas as pd
AAPL=pd.read_csv('/Users/shawn/Desktop/AAPL.csv',usecols=[0,4],index_col=0,parse_dates=True)
print(AAPL)
# %%
import pandas as pd

# 創建一個字典，包含您的數據
data = {
    '姓名': ['Alice', 'Bob', 'Charlie', 'David'],
    '年齡': [25, 30, 35, 40],
    '城市': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

# 使用字典創建 DataFrame
df = pd.DataFrame(data)

# 顯示 DataFrame
print(df)
# %%
