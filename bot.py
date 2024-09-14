from pyrogram import filters , Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from dotenv import load_dotenv
import PIL.Image
import google.cloud.aiplatform
import google.generativeai as genai
import os

load_dotenv()

API_HASH  = os.getenv('API_HASH')
API_ID  = os.getenv('API_ID')
BOT_TOKEN  = os.getenv('BOT_TOKEN')
GOOGLE_API  = os.getenv('GOOGLE_API')

app= Client('gemini-TeleBot',
            api_hash=API_HASH,api_id=int(API_ID),
            bot_token=BOT_TOKEN)

genai.configure(api_key=GOOGLE_API)

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 500,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

files = []

# chat session dari AI Studio google atau buat histori percakapan dengan format serupa
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "mulai sekarang kamu adalah Jarvis",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Baiklah, Tuan. Saya Jarvis, asisten virtual Anda. Apa yang bisa saya lakukan untuk Anda hari ini? \n",
      ],
    },
  ]
)

@app.on_message(filters.command('start') & filters.private)
async def start(_,message:Message):
    welcome_message = (
        f" Halo @{message.chat.username}!\n\n"
        "Saya Jarvis 🤖, asisten virtual Anda. Apa yang ingin anda tanyakan hari ini?\n\n"
    )
    await message.reply(welcome_message,quote=True)

@app.on_message(filters.text & filters.private)
async def reponse(client, message):
    try:
        response = chat_session.send_message(message.text)
        await message.reply(response.text)
    except Exception as e:
        await message.reply('Gagal tersambung ke server!')
        raise e
    
@app.on_message(filters.photo & filters.private)
async def handle_photo(client, message):
    try:
        caption = message.caption if message.caption else "Jelaskan gambar ini." # caption sebagai prompt untuk gambar
        photo = message.photo
        file = await client.download_media(photo.file_id)
        img = PIL.Image.open(file)

        response = chat_session.send_message([caption, img], stream=True)
        response.resolve()

        await message.reply(response.text)

        if os.path.exists(file):
            os.remove(file)
    
    except Exception as e:
        await message.reply('Gagal memproses gambar!')
        raise e

app.run(print('Bot Started...'))
