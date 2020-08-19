import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import AddChatUserRequest


api_id = 1652138
api_hash = 'b2f0d235e8f8d7f4d6a11a39058aef55'
bot_token  = '1251418314:AAGaPAc7pcpKWzluP-PYYhGk9LbcSMtbcCM'

Client = TelegramClient('TravisTon', api_id, api_hash)

@Client.on(events.NewMessage)
async def my_event_handler(event):
   #print(event)
    if 'hello' in event.raw_text:
        await event.reply('hi how are you doing')
    if 'fine' in event.raw_text:
        await event.reply('very good, welcome to Travis_Bot. How may i help you?')    
    if 'help' in event.raw_text:
        await event.reply('yesss how do i help you')


Client.start()
Client.run_until_disconnected()


