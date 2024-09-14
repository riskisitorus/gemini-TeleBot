# Gemini Virtual Assistant Bot 🤖
A Python-based Telegram bot built using Pyrogram, integrated with Google Gemini API. This bot acts as a virtual assistant, powered by Google Generative AI (Gemini), capable of handling text-based conversations and analyzing images.

## Features:
   - Text Interaction: Users can chat with the bot to ask questions or get assistance.
   - Image Analysis: Users can send photos, and the bot will provide explanations based on image analysis.
   - Google Gemini Integration: Utilizes Google Gemini (Generative AI) for advanced text and image processing, enhancing the conversational 
   capabilities of the bot.
   - Customizable Chat Sessions: Easily customizable history and behavior to suit specific needs.
   - File Upload to Gemini: Seamlessly upload media files to Google Gemini for analysis.

## How to Run:
1. Clone this repository.
3. Create a `.env` file with your API credentials for Pyrogram and Google Gemini.
2. Make sure to add your `API_HASH`, `API_ID`, `BOT_TOKEN`, and `GOOGLE_API` in the `.env` file.
4. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the bot:
```bash
python bot.py
```

## Customization:
```python
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "mulai sekarang kamu adalah Jarvis.",
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
```
This code is derived from the documentation of **[Google AI Studio](https://aistudio.google.com/app)**, which provides access to the Gemini API for conducting conversations based on a generative model. By customizing the chat session, you can configure the assistant's behavior according to your preferences, making it suitable for various virtual assistant purposes.

You can set the maximum number of tokens for the response from Gemini.
```python
"max_output_tokens": 500,
```
