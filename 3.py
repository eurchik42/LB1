from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

api_id = 123
api_hash = ''
phone = ''
client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start()
    channel_username = '123'
    channel = await client.get_entity(channel_username)

    participants = await client(GetParticipantsRequest(
        channel,
        ChannelParticipantsSearch(''),
        offset=0,
        limit=2,
        hash=0
    ))
    for user in participants.users:
        print(user.id, user.first_name, user.last_name)

    saved_message = "TEST"
    await client.send_message('me', saved_message)
    print("TEST.")
with client:1