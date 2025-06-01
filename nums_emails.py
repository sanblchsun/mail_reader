def get(mail):
    # Выбираем для работы папку входящие (inbox)
    mail.select("inbox")
    # Получаем массив со списком найденных почтовых сообщений в этой папке
    result, data = mail.search(None, "ALL")
    # Сохраняем в переменную ids строку с номерами писем
    ids = data[0]
    # Получаем массив номеров писем
    id_list = ids.split()
    return id_list