import os
import requests
from bs4 import BeautifulSoup
from telegram import Bot
from datetime import datetime

# Ayarlar
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TESLA_URL = "https://www.tesla.com/tr_tr/inventory/new/my"

def get_stock():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(TESLA_URL, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Demo amaçlı basit çekim (Gerçekte site yapısına göre güncelleyin)
        items = soup.find_all('div', class_='inventory-item')[:3]  # İlk 3 araç
        return "\n".join([item.text.strip() for item in items]) if items else "Stok yok"
        
    except Exception as e:
        return f"Hata: {str(e)}"

if __name__ == "__main__":
    bot = Bot(token=TOKEN)
    message = f"🔄 {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
    message += get_stock()
    bot.send_message(chat_id=CHAT_ID, text=message)
