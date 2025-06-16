import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

def run_healthcheck_server():
    port = int(os.environ.get("PORT", 8080))
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is running")
        def do_HEAD(self):
            self.send_response(200)
            self.end_headers()
    server = HTTPServer(("", port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()

run_healthcheck_server()

import asyncio
import importlib
import signal
from pyrogram import idle
from Extractor.modules import ALL_MODULES
from Extractor import app, info_bot

loop = asyncio.get_event_loop()
should_exit = asyncio.Event()

def _handle_signal():
    print("Shutting down gracefully...")
    loop.create_task(should_exit.set())

# Proper signal handling for asyncio
signal.signal(signal.SIGTERM, lambda s, f: _handle_signal())
signal.signal(signal.SIGINT, lambda s, f: _handle_signal())

async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)
    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

async def main():
    await info_bot()
    await sumit_boot()
    await should_exit.wait()
    await app.stop()
    print("App stopped gracefully.")

if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        pending = asyncio.all_tasks(loop)
        for task in pending:
            task.cancel()
        loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
        loop.close()
        print("Loop closed.")
