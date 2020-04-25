import requests
import telegram
from bs4 import BeautifulSoup

bot = telegram.Bot(token = '1139803811:AAGacF499aihkvE4Ga8NruMjxzVhEGKFeII')

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200502&screencodes=&screenratingcode=&regioncode='
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select('span.imax')

for i in imax:
    if i:
        # find_parent 부모 찾기
        imax_html = i.find_parent('div', class_='col-times')
        title = imax_html.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id = 685328737, text = title + ' IMAX 예매가 열렸습니다.')
    else:
        bot.sendMessage(chat_id = 685328737, text = 'IMAX 예매가 열리지 않았습니다.')