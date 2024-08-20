def send_email(message, recipient, *, sender="university.help@gmail.com"):
    recipient = recipient.replace(' ', '')
    print('Отпровитель ' + sender)
    change_sender = input('Нужго ли поменять recipient: ').lower()
    if change_sender == 'да':
        sender = input('Напишите почту отпровителя: ')
    recipient.find("@")
    print()
    ending = ('.com', '.ru', '.net')
    if recipient.find("@") == -1 or recipient.endswith(ending) or sender.endswith(ending):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender.lower() == recipient.lower():
        print('Нельзя отправить письмо самому себе!')
    elif sender.lower() != recipient.lower() and change_sender == 'да':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    elif sender.lower() != recipient.lower():
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')




send_email(input('Напишите писмо: '), input('Напишите получателя: '))