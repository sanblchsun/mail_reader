import logging
import time

import config
import imaplib


def connect():
    while True:
        mail_pass = config.mail_pass
        username = config.email
        imap_server = config.imap_server
        try:
            mail = imaplib.IMAP4_SSL(imap_server)
            mail.login(username, mail_pass)
            return mail
        except Exception as e:
            logging.error(f"""У бота 'FormDesigner' ошибка чтения почты {username}.
    Каждые 5 минут идет попытка подключиться к почте""")
            try:
                time.sleep(300)
            except KeyboardInterrupt as e:
                pass