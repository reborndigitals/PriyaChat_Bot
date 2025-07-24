from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "10284859"
# -------------------------------------------------------------
API_HASH = "b0ad58eb8b845ba0003e0d9ce5fc2196"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://heartbeat:Beat7Heart@heartbeat.1h1nbxv.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(getenv("OWNER_ID", "1281282633"))
SUPPORT_GRP = "HeartBeat_Fam"
UPDATE_CHNL = "HeartBeat_Offi"
OWNER_USERNAME = "rajeshrakis"
