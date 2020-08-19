
#from telethon.tl.functions.messages import AddChatUserRequest
from telethon.sync import TelegramClient
from telethon import functions, types

api_id = 1652138
api_hash = 'b2f0d235e8f8d7f4d6a11a39058aef55'

with TelegramClient('TravisTon', api_id, api_hash) as client:
    result = client(functions.channels.InviteToChannelRequest(
        channel='blask',
        users=['@clynezino']
    ))
    print(result.stringify())    