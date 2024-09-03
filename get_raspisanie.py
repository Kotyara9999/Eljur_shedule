import telegram
from config import botId

path = "eljur.png"
tg = telegram.teleHandler(tele_token=botId)
tg.addPhoto(file=open(path, "rb"))
tg.sendMedia()