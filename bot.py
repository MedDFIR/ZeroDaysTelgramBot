from telegram import Bot
import requests
from bs4 import BeautifulSoup

# Import configuration settings
from config import BOT_TOKEN, CHANNEL_NAME

# Initialize the bot with your token
bot = Bot(token=BOT_TOKEN)

# Function to fetch updates from a vulnerability source (Example: Exploit DB)
def fetch_updates():
    url = 'https://www.exploit-db.com/'  # Example source
    response = requests.get(url)
    updates = []

    if response.status_code == 200:
        # Parse the response using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('div', class_='exploit_list_entry')  # Adjust according to site structure

        for entry in entries:
            title = entry.find('h2').text  # Extract vulnerability title
            link = entry.find('a', href=True)['href']  # Extract link
            full_link = f'https://www.exploit-db.com{link}'  # Construct full URL
            update = f"**New Vulnerability Found**\n\nTitle: {title}\nSource: [Exploit DB]({full_link})"
            updates.append(update)

    return updates

# Function to send updates to Telegram channel
def send_update(update):
    bot.send_message(chat_id=CHANNEL_NAME, text=update, parse_mode='Markdown')

# Main function to fetch and send updates
def main():
    updates = fetch_updates()
    if updates:
        for update in updates:
            send_update(update)

if __name__ == "__main__":
    main()
