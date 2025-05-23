"""
from os import getenv


API_ID = int(getenv("API_ID", "21567814"))
API_HASH = getenv("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
BOT_TOKEN = getenv("BOT_TOKEN", "7954807388:AAGeH_MMFHWdj3nwBPfkyLVF1PZ7I4rIEGk")
OWNER_ID = int(getenv("OWNER_ID", "6126688051"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6126688051").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://wadiro6523:08AwfhhKRdQaS1i6@cluster0.krzxuop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002649968638"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002668283003")) "6126688051"))
API_HASH = environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "21567814"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7954807388:AAGeH_MMFHWdj3nwBPfkyLVF1PZ7I4rIEGk")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("extractor_protxtbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6126688051"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6126688051").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002649968638"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://wadiro6523:08AwfhhKRdQaS1i6@cluster0.krzxuop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002668283003"))

