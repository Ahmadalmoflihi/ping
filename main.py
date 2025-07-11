import discord
from discord.ext import commands
from discord.ui import View, Button
import threading
import time
import requests
from flask import Flask
import os
from dotenv import load_dotenv

# تحميل المتغيرات
load_dotenv()

# إعداد سيرفر Flask للتشغيل الدائم
app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# سكربت Ping تلقائي
def ping_loop():
    while True:
        try:
            requests.get("https://ping-nres.onrender.com/")
        except:
            pass
        time.sleep(60)

ping_thread = threading.Thread(target=ping_loop)
ping_thread.daemon = True
ping_thread.start()

# إعداد بوت ديسكورد
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def بينق(ctx):
    await ctx.send("🏓 Pong!")

# تشغيل البوت
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
