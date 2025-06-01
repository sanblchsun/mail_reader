import email
import logging
import time
import body_email
import connect_mail
from email.header import decode_header
import email_tobot
import mv_email
import nums_emails



def read_email():
    while True:
        # подключаемся к почте
        mail = connect_mail.connect()
        # получаем количество писем в папке Входящие
        id_list = nums_emails.get(mail)

        for num in reversed(id_list):
            _, data = mail.fetch(num, '(RFC822)')  # Магическое число ^_^
            _, b = data[0]  # копаем до нужных нам данных
            email_msg = email.message_from_bytes(b)
            # Если тема письма на кириллице, нужно декодировать текст
            try:
                subject, encoding = decode_header(email_msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
            except TypeError as e:
                subject = email_msg["Subject"]

            header_email = {'subject': subject, 'from': email_msg['from'], 'date': email_msg['date']}

            # Получаем поле письма
            body = body_email.get(email_msg)
            if header_email['subject'] == 'Новая заявка':
                # Отправляем письмо в телеграмм чат
                res = email_tobot.send(header_email["date"], header_email["from"], body)
                if not res:
                    mail.close()
                    mail.logout()
                    try:
                        time.sleep(300)
                    except KeyboardInterrupt as e:
                        pass
                    break
            # перемещаем письмо в другую папку
            mv_email.perform(mail,num)

            try:
                time.sleep(5)
            except KeyboardInterrupt as e:
                pass

        mail.close()
        mail.logout()
        try:
            time.sleep(300)
        except KeyboardInterrupt as e:
            pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(message)s")
    read_email()
