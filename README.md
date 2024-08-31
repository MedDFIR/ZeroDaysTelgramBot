# ZeroDaysTelegramBot

## Description
ZeroDaysTelegramBot is an educational project designed to help you create a Telegram bot that automatically fetches and sends updates on new Zero Day vulnerabilities directly to a Telegram channel. This project guides you through setting up the bot, configuring the environment, and understanding the code, making it an excellent resource for learning about web scraping, Telegram bot development, and automation in cybersecurity.

## Languages and Utilities Used

- **Python** - Main programming language used for scripting the bot and fetching data.
- **BeautifulSoup** - Used for parsing and extracting information from HTML content.
- **Requests** - Library used to make HTTP requests to fetch web content.
- **python-telegram-bot** - Python library to interact with Telegram’s Bot API.

## Environments Used

- **Windows 10** (21H2) - Development environment where the bot was created and tested.
- **Python 3.10** - Version of Python used in the project.

## Walkthrough:

This section provides a detailed walkthrough of setting up the bot and getting it to work. Below are the steps you’ll need to follow:

### Step 1: Create a Telegram Channel
1. **Open Telegram** and click on the menu (three lines at the top left).
2. Select "New Channel" and follow the prompts to name your channel. For this project, we’ll name it **ZeroDaysTelegramBot** (but name it however you'll like).
3. Set the channel to **private** if it’s for personal use.
4. You can customize your channel with a profile picture and description if desired.

### Step 2: Create Your Telegram Bot
1. In Telegram, search for **BotFather** and start a chat with it.
2. Type `/newbot` and follow the instructions:
   - Provide a name for your bot (e.g., `Zero Days Alert Bot`).
   - Set a unique username ending with `bot` (e.g., `ZeroDaysAlertBot`).
3. **Save the Bot Token** provided by BotFather. This token is essential for connecting your bot to the Telegram API.

### Step 3: Add the Bot to Your Channel
1. Go to your newly created channel (ZeroDaysTelegramBot).
2. Click on the channel name at the top, then on "Administrators."
3. Add your bot as an admin by searching for its username (e.g., `@ZeroDaysAlertBot`) and selecting it.

### Step 4: Set Up Your Development Environment
1. **Install Python**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. **Install Required Libraries**:
   - Open your terminal and run:
     ```bash
     pip install python-telegram-bot requests beautifulsoup4
     ```

### Step 5: Writing and Running the Bot Script
1. Create the main script file (`bot.py`) inside the `/src` directory of your project.
2. Copy the code provided in the repository and replace placeholders like `YOUR_TELEGRAM_BOT_TOKEN` and `@yourchannelname` with your actual bot token and channel username.
3. Run the script to test if the bot fetches and sends updates correctly to the channel.

### Step 6: Deploy and Automate
1. To keep your bot running 24/7, consider deploying it to a cloud platform like AWS, Heroku, or keeping it running on a personal server.
2. Set up a cron job or task scheduler to run the bot script at regular intervals, ensuring you receive the latest updates.

For further details, refer to the `/docs` directory in this repository, where additional guides and troubleshooting tips are provided.

---
