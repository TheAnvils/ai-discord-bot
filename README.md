# AI Discord bot
This is a simple, highly customisable AI discord bot using groq made in python. It will respond to your messages when you ping it or reply to it. Please note that it does not have any memory of past messages.
# Features
- Highly customisable settings
- Automated response filtering
- Lightning-fast speeds thanks to the groq API
- Access to up-to-date information (coming soon)
# How to use
This section showcases how to install and run this program. Make sure you have git and python installed. Using venv or conda is highly recommended
1. Clone the repository ``git clone https://github.com/TheAnvils/ai-discord-bot``
2. Move into the folder ``cd ai-discord-bot``
3. Install required tools ``pip install -r requirements.txt``
4. Move into src directory ``cd src``
5. Add ENV variables (Configuration)
6. Start the bot ``python main.py``
# Configuration
There are several options you can configure.
- BOT_TOKEN (required) - Your discord bot token
- GROQ_API_KEY (required) - Your groq api key
- GROQ_MODEL (optional) - The ai model which will be used
- SERVER_RULES (optional) - The rules of your server separated by commas
- GROQ_MAX_TOKENS (optional) - Maximum tokens that the AI should output. Defaults to 100