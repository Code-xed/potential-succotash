from pyrogram import Client, filters
from Config import api_id, api_hash, session_string

with open("config.ini", "w") as f:
    f.write(f"[pyrogram]\napi_id = {api_id}\napi_hash = {api_hash}")

with Client(session_string) as app:
    print("Successfully Logged In")
    app.send_message("me","Working")
