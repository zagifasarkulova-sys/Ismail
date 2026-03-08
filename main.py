import threading
import os
import asyncio
from flask import Flask, send_file
from bot import main as bot_main

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/')
def index():
    return send_file(os.path.join(BASE_DIR, 'index.html'))

@app.route('/health')
def health():
    return 'OK'

def run_bot():
    import time
    time.sleep(10)  # wait for old instance to shut down during rolling deploy
    while True:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            bot_main()
            break  # clean exit
        except Exception as e:
            if "Conflict" in str(e):
                print(f"[bot] Conflict detected, retrying in 15s...")
                time.sleep(15)
            else:
                print(f"[bot] Unexpected error: {e}")
                time.sleep(5)

if __name__ == '__main__':
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
