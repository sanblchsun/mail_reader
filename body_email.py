def get(email_msg):
    # Получаем поле письма
    for part in email_msg.walk():
        if part.get_content_type() == 'text/plain':  # текст
            body = part.get_payload(decode=True)
            body = body.decode()
        elif part.get_content_type() == 'text/html':  # html
            html_body = part.get_payload(decode=True)
            body = html_body.decode()
    return body