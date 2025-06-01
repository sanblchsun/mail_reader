import logging
import requests
from bs4 import BeautifulSoup
from html_pattern import html
import config
import filter_for_chat


def send(Date, From, body):
    soup = BeautifulSoup(body, 'html.parser')
    lst = soup.find_all('td')
    firma = lst[0].string
    full_name = lst[1].string
    cont_telefon = lst[3].string
    e_mail = lst[4].string
    description = ''.join(map(str, lst[7].contents)).replace('<br/>', '')
    priority = lst[8].string
    html_tobot = html(Date, From, firma, full_name, cont_telefon, e_mail, description, priority)
    res = filter_for_chat.check(firma)
    if not res:
        return True
    BOT_TOKEN = config.bot_token
    CHAT_ID = config.chat_id
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    # Параметры запроса
    params = {
        "chat_id": CHAT_ID,
        "text": html_tobot,
        "parse_mode": "html"
    }
    response = requests.get(url, params=params)
    # Обработка ответа сервера
    if response.status_code != 200:
        logging.error(f"""Ошибка подключения к телеграмм, сообщение в телеграмм чат не отправлено :
        {response.status_code}""")
        return False

    return True
