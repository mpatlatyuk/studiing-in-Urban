def send_email(message, recipient,*, sender='university.help@gmail.com') -> str:
# """ф-я: 1. проверяет на корректность адреса отправителя и получателя
# 2. проверяет на отправку самому себе
# 3. проверяет на отправителя по умолчанию"""

    text_1 = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    text_2 = f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
    text_3 = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'

    #return text_2
    #return text_3


    if  '@' not in {sender} or '@' not in {recipient}:
        print(text_1)
    elif '.com' not in {sender} or 'com' not in {recipient}:
        print(text_1)
    elif '.ru' not in {sender} or '.ru' not in {recipient}:
        print(text_1)
    elif '.net' not in {sender} or '.net' not in {recipient}:
        print(text_1)


    elif recipient == sender:
        print('Нельзя отправить письмо самому себе')

    sender = True
    if sender:
        print(text_2)
    else:
        print(text_3)

    #return text


send_email('Это сообщение - для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')