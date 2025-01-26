from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "24996524"
# -------------------------------------------------------------
API_HASH = "b0825fc3f523fd28b2ea1735a07a058e"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "6260080241"))
SUPPORT_GRP = "ANJALIWORLD"
UPDATE_CHNL = "ANJALINETWORK"
OWNER_USERNAME = "AnjaliOwnerBot"
