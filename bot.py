from pyrogram import Client, filters
from Config import api_id, api_hash, session_string

with Client(session_string) as app:
    print("Successfully Logged In")
    app.send_message(app.export_session_string())
