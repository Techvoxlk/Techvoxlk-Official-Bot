import os
import telebot
from telebot import types

bot = telebot.TeleBot("6902274799:AAEAIPxR8FcEu3jn8PfNiCTxsBAXVIuvv8w")

# Start command with buttons
@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("My Youtube Channel")
    item2 = types.KeyboardButton("My Telegram Group")
    markup.add(item1, item2)
    
    bot.reply_to(message, "👋 Welcome to Techvox Official Bot!\n\n"
                          "I'm thrilled to have you here! This bot is your gateway to a more interactive and personalized experience with my YouTube channel, Techvoxlk. Feel free to:", reply_markup=markup)

# Handler for My Youtube Channel button
@bot.message_handler(func=lambda message: message.text == "My Youtube Channel")
def my_youtube_channel(message):
    bot.send_message(message.chat.id, "Visit my YouTube Channel: [Techvoxlk](https://youtube.com/@Techvoxlk)", parse_mode='markdown', disable_web_page_preview=True)

# Handler for My Telegram Group button
@bot.message_handler(func=lambda message: message.text == "My Telegram Group")
def my_telegram_group(message):
    bot.send_message(message.chat.id, "Join my Telegram Group: [Techvoxlk Group](https://t.me/Techvoxlk_Group)", parse_mode='markdown', disable_web_page_preview=True)

# /Chat command
@bot.message_handler(commands=["chat"])
def chat_command(message):
    bot.reply_to(message, "Now you can Chat With Owner. Type Your Message.")
    # You can add logic to handle the owner being offline and reply with a button for the user to leave a message.

# /Search command
@bot.message_handler(commands=["search"])
def search_command(message):
    bot.reply_to(message, "Send your keyword.")
    # Add logic to handle searching based on the keyword.

# /Download command
@bot.message_handler(commands=["download"])
def download_command(message):
    bot.reply_to(message, "Search your file or video name.")
    # Add logic to handle downloading based on the file or video name.

# /Videos command
@bot.message_handler(commands=["videos"])
def videos_command(message):
    bot.reply_to(message, "List of all videos.")
    # Add logic to display all uploaded videos.

# /Blogs command
@bot.message_handler(commands=["blogs"])
def blogs_command(message):
    bot.reply_to(message, "List of all blogs.")
    # Add logic to display all uploaded blogs.

# /Contact_Numbers command
@bot.message_handler(commands=["contact_numbers"])
def contact_numbers_command(message):
    bot.reply_to(message, "Phone Number - 0776756992\nEmail - Techvoxlk@gmail.com")

# Handle the reply button
@bot.callback_query_handler(func=lambda call: True)
def handle_reply(call):
    # You can add logic here to handle replies based on the callback data.
    pass

bot.polling()
