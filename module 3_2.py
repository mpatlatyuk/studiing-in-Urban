def send_email(message, recipient,*, sender='university.help@gmail.com') -> str:
# """ф-я: 1. проверяет на корректность адреса отправителя и получателя
# 2. проверяет на отправку самому себе
# 3. проверяет на отправителя по умолчанию"""

    def send_email(message, recipient,*, sender='university.help@gmail.com') -> str:
# """ф-я: 1. проверяет на корректность адреса отправителя и получателя
# 2. проверяет на отправку самому себе
# 3. проверяет на отправителя по умолчанию"""

    
    if '@' not in sender or '@' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')) or not (
        recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif recipient == sender:
        print('Нельзя отправить письмо самому себе')

    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение - для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


send_email('Это сообщение - для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
