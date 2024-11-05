import os

API_ID = API_ID =  20346550

API_HASH = os.environ.get("API_HASH", "bc79c3bea7a626887bdc0871eecf0327")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7667053478:AAGUm8yEaroZVT-utmZVeachNUv0uK1IMwM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7081036509))

LOG = -1002322080938,

# UPDATE_GRP = -1002322080938, # bot sat group

# auth_chats = [7081036509,7491167754]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7081036509").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


