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
