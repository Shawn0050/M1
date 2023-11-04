import requests
import telebot
import schedule
from threading import Thread
import time
from bs4 import BeautifulSoup

# 設定 TAIFEX 期權數據的 URL
url = 'https://histock.tw/stock/option.aspx?m=week'

# 發送 HTTP 請求
response = requests.get(url)

# 解析網頁
soup = BeautifulSoup(response.text, 'html.parser')

# 找到買賣權價平的成交價
# 找到所有的td和th元素
cells = soup.find_all(['td', 'th'])

# 找出K的索引
strike_index = cells.index(soup.find('th', class_='strike tg'))
# K前的第五個值是買權價平權利金(要先手點)
call_premium_atm = cells[strike_index - 5].get_text()
# K後的第三個值是賣權價平權利金（要先手點）
put_premium_atm = cells[strike_index + 3].get_text()

print("Call ATM Premium:", call_premium_atm)
print("Put ATM Premium:", put_premium_atm)

# 尋找含有“台指期近月”文本的<a>標籤
a_tag = soup.find('a', string="台指期近月")

# 找到<a>標籤對應的父<span>標籤
parent_span = a_tag.find_parent('span')
# 然後找到父<span>標籤後的下一個<span>標籤
index_span = parent_span.find_next_sibling('span')
# 在index-data2中找到所有的<span class="clr-rd">標籤
clr_rd_spans = index_span.find_all('span', class_='clr-rd')
# 第一個<span class="clr-rd">即為所求
index_value = clr_rd_spans[0].get_text()

print("台指期近月:", index_value)

f1c = float(call_premium_atm)
f1p = float(put_premium_atm)
f2 = float(index_value)
Implied_vol_Call = f1c/0.4/f2/((5/252)**0.5)
Implied_vol_Put = f1p/0.4/f2/((5/252)**0.5)

print(Implied_vol_Call)
print(Implied_vol_Put)

BOT_TOKEN = "6266065543:AAGwRgl73SmqBrjNMNNrW6oCskobpUXijcg"
chat_id = "-1002131116027"
bot = telebot.TeleBot(BOT_TOKEN)
def send_message(msg, bot, chat_id):
        bot.send_message(chat_id, msg)
        print("Message sent successfully!")
def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(0.5)
def check(call_premium_atm, put_premium_atm,index_value):
    if Implied_vol_Call > 0.1:
          send_message(f'價平Call要進場，權利金參考{call_premium_atm}，履約價參考{index_value}', bot, chat_id)
    if Implied_vol_Put > 0.1:
          send_message(f'價平Put要進場，權利金參考{put_premium_atm}，履約價參考{index_value}', bot, chat_id)
def job():
    check(call_premium_atm, put_premium_atm,index_value)


if __name__ == '__main__':
    schedule.every().wednesday.at("10:30").do(job)
    Thread(target=schedule_checker).start()
    while(True):
        time.sleep(0.5)


