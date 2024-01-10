#Coded by KA18 the @legend580 💛❤️

import re, os, logging
from os import environ,getenv
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "LegendBot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '3393749'))
API_HASH = environ.get('API_HASH', 'a15a5954a1db54952eebd08ea6c68b71')
BOT_TOKEN = environ.get('BOT_TOKEN', "6100891233:AAHo_OjnFWTdY_JewRdcqphxASAcAK1IHVg") #@dgfghgjbot
# BOT_TOKEN = environ.get('BOT_TOKEN', "5872747581:AAH7_XPCOCEVfbgUhepjJWlcOmj8wjDTjBk") #@jn_url_v3_bot
TG_BOT_WORKERS = int(environ.get('TG_BOT_WORKERS', '20'))
PORT = environ.get("PORT", "8080")
DOWNLOAD_LOCATION = "./DOWNLOADS"
PICS = (environ.get('PICS', 'https://graph.org/file/4cf3f3c83e15e2b80e9f3.jpg')).split() #SAMPLE PIC

# Admins, Channels & Users
OWNER_ID = int(environ.get('OWNER_ID', '1061576483'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1061576483 5963138883').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1061576483 5963138883').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002048677793'))
FILE_STORE_CHANNEL = int(environ.get('FILE_STORE_CHANNEL', '-1002048677793'))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Jayanna:Jayanna2023@yash.tm1c2bd.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "TEST_DB")

# Others
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://mj-filter-v01.onrender.com/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://mj-filter-v01.onrender.com/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '10'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'MJBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'MJhitz'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://mj-filter-v01.onrender.com/".format(FQDN)
else:
    URL = "https://mj-filter-v01.onrender.com/".format(FQDN)
