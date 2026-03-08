import threading
import os
import asyncio
from flask import Flask, send_file
from bot import main as bot_main

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/health')
def health():
    return 'OK'

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot_main()
