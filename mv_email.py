import logging


def perform(mail, id_email):
# Перемещаем  письмо в папку INBOX/Completed
    copy_res = mail.copy(id_email, 'INBOX/Completed')
    if copy_res[0] == 'OK':
        mail.store(id_email, '+FLAGS', '\\Deleted')
        mail.expunge()
    else:
        logging.error("""Критичная ошибка, в почтовом ящике нет каталога: 'INBOX/Completed'""")
        exit(1)
