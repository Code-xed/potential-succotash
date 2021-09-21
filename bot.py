from pyrogram import Client

session_string = "...ZnUIFD8jsjXTb8g_vpxx48k1zkov9sapD-tzjz-S4WZv70M..."

with Client(session_string) as app:
    print(app.get_me())