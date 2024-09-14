# Gemini Virtual Assistant Bot 🤖
A Python-based Telegram bot built using Pyrogram, integrated with Google Gemini API. This bot acts as a virtual assistant, powered by Google Generative AI (Gemini), capable of handling text-based conversations and analyzing images.

### Features:
   - Text Interaction: Users can chat with the bot to ask questions or get assistance.
   - Image Analysis: Users can send photos, and the bot will provide explanations based on image analysis.
   - Google Gemini Integration: Utilizes Google Gemini (Generative AI) for advanced text and image processing, enhancing the conversational 
   capabilities of the bot.
   - Customizable Chat Sessions: Easily customizable history and behavior to suit specific needs.
   - File Upload to Gemini: Seamlessly upload media files to Google Gemini for analysis.

### How to Run:
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

### Customization:
```python
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "From now on, you are Jarvis.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Alright, Sir. I am Jarvis, your virtual assistant. What can I do for you today?\n",
      ],
    },
  ]
)
```
