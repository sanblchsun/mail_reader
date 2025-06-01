def html(Date, From, firma,full_name,cont_telefon,e_mail,description,priority):
    html = f"""
               <i><b>Заявка от: </b></i>
    <code>{From}</code>
               <i><b>Время заявки: </b></i>
    <code>{Date}</code>
               <i><b>Компания: </b></i>
    <code>{firma}</code>
               <i><b>Фамилия Имя: </b></i>
    <code>{full_name}</code>
               <i><b>Контактный телефон: </b>
    </i><code>{cont_telefon}</code>
               <i><b>E-mail адрес: </b></i>
    <code>{e_mail}</code>
               <i><b>Описание проблемы: </b></i>
    <code>{description}</code>
               <i><b>Приоритет заявки: </b></i>
    <code>{priority}</code>"""
    return html