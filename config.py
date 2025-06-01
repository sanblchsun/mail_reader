from environs import Env

env = Env()
env.read_env()

mail_pass = env.str("MAIL_PASS")
email = env.str("EMAIL")
imap_server = env.str("IMAP_SERVER")

bot_token = env.str("BOT_TOKEN")
chat_id = env.int("CHAT")

# send_attach = False #пересылка вложений, чтобы отключить нужен параметр False
#
# encoding="utf-8"
