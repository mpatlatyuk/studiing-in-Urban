def send_email(message, recipient,*, sender='university.help@gmail.com') -> str:
# """ф-я: 1. проверяет на корректность адреса отправителя и получателя
# 2. проверяет на отправку самому себе
# 3. проверяет на отправителя по умолчанию"""

    #text_1 = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    #text_2 = f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
    #text_3 = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'

    #return text_2
    #return text_3
    text = ''

    if '@' not in {sender} or '@' not in {recipient}:
        print(text == f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '.com' not in {sender} or 'com' not in {recipient}:
        print(text == f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '.ru' not in {sender} or '.ru' not in {recipient}:
        print(text == f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '.net' not in {sender} or '.net' not in {recipient}:
        print(text == f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif recipient == sender:
        print(text == 'Нельзя отправить письмо самому себе')

    #sender = True
    if sender == True:
        print(text == f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(text == f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

    return text


send_email('Это сообщение - для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
