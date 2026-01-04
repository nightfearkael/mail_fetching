import email
import imaplib
from config import email_login, email_pass


def get_unread_messages(mail_dir: object) -> list:
    """
    Принимает в себя объект подключения к почтовому ящику.
    В функции select выбираем папку с сообщениями (здесь - входящие)
    Возвращает список uid непрочитанных (UNSEEN), либо всех (ALL) сообщений
    :param mail_dir: Объект подключения к почте
    :return: list of emails [uid1, uid2, uid3]
    """
    # Выбор конкретного ящика "входящие", нужно проверить как называется в доменной почте
    mail_dir.select('inbox')
    # result=OK, data = список ID непрочитанных писем (можно поставить ALL для дебага)
    result, data = mail_dir.uid('search', None, "UNSEEN")
    if result == 'OK':
        return data


def parse_messages(email_list: list) -> None:
    """
    Обрабатывает список полученных UID email
    :param email_list: Список uid сообщений из get_unread_messages()
    :return: None
    """
    email_list = email_list[0].split()

    for uid in email_list:
        # result=OK, email_data - объект письма
        result, email_data = mail.uid('fetch', uid, '(RFC822)')
        # Декодинг данных из письма
        raw_email_string = email_data[0][1].decode('utf-8')
        # Получение данных сообщения
        email_message = email.message_from_string(raw_email_string)

        ##### Добавить сюда Вашу логику обработки всех писем


if __name__ == '__main__':
    # Данные подключения к email на yandex
    EMAIL_ACCOUNT = email_login
    PASSWORD = email_pass
    imap_addr = 'imap.yandex.ru'
    imap_port = 993

    # Параметры подключения к IMAP серверу
    mail = imaplib.IMAP4_SSL(host=imap_addr, port=imap_port)
    # Авторизация в почте
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    # Список папок в почтовом ящике
    mail.list()

    message_uid_list = get_unread_messages(mail_dir=mail)

    parse_messages(email_list=message_uid_list)
