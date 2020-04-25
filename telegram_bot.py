import telegram

bot = telegram.Bot(token = '1139803811:AAGacF499aihkvE4Ga8NruMjxzVhEGKFeII')

# for i in bot.getUpdates():
#     print(i.message)

# bot 에 해당 id를 가져와 메시지 보내는 법
bot.sendMessage(chat_id = 685328737, text = '테스트')