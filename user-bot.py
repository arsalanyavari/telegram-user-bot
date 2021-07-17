# ArYa48 - 2021-July-17 start at: 20:20:55
# The project name: Telegram user bot

# import Telegram api-id and api hash
from data import *

# import needed libraries :)
from telethon.sync import TelegramClient
from telethon import functions, types
from datetime import datetime
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.types import InputPhoto
from telethon.tl.functions.account import UpdateUsernameRequest

# global variables
pre_time = 0    # pre: previous
cur_time = 0    # cur: current
now = datetime.now()


def setProfilePhoto(client, profile_path):  # stupid function =))
    client(UploadProfilePhotoRequest(
        client.upload_file(profile_path)))


def removeProfilePhoto(client, photo_num):
    p = client.get_profile_photos('me')[photo_num - 1]
    client(DeletePhotosRequest(
        id=[InputPhoto(
            id=p.id,
            access_hash=p.access_hash,
            file_reference=p.file_reference
        )]
    ))


def updateBio(client):
    result = client(functions.account.UpdateProfileRequest(
        # You can replace your own bio sentence
        #  instead of two these below lines :))
        about="Time and tide wait for no man " +
        str(cur_time) + " :)"
    ))


def updateFirstName(client, name):          # stupid function =))
    result = client(functions.account.UpdateProfileRequest(first_name=name))


def updateLastName(client, name):           # stupid function =))
    result = client(functions.account.UpdateProfileRequest(last_name=name))


def updateUsername(client, username):       # stupid function =))
    result = client(UpdateUsernameRequest(username))


def sendMessage(client, username, message):  # stupid function =))
    client.send_message(username, message)


def responseToMessage(client):
    # for message in client.iter_messages(chat, search='hello'):
    pass


def main():
    global pre_time
    global cur_time
    global now
    with TelegramClient('ArYa', api_id, api_hash) as client:
        while True:
            cur_time = now.strftime("%H:%M")
            if(cur_time != pre_time):
                sendMessage(client, "@Arsalanyavari", "message")
                setProfilePhoto(
                    client, '/home/arya/Desktop/Wallpapers/Wallpapers/Desktop-3.jpg')
                updateBio(client)
                updateFirstName(client, "arsalan")
                updateLastName(client, "yavari")
                updateUsername(client, "arsalanyavarikovskia")
                pre_time = cur_time

        # client.log_out()
        # client.disconnect()


if __name__ == "__main__":
    main()
