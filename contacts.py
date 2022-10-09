import csv

_CONTACTS = {}


def create_contact():
    """
    Создает контакт
    """
    name = input('Введите имя и фамилию (через пробел): ').split()
    address = input('Введите адрес: ')
    phone = input('Введите номер телефона: ')

    contact = {
        'name': name,
        'address': address,
        'phone': phone
    }

    name = contact['name'][0]
    _CONTACTS[name] = contact
    print(f'Контакт {name} добавлен в телефонную книгу')


def view_contacts(name=None):
    """
    Отображает контакты телефонной книги
    """
    print('Контакты в телефонной книге: ')

    if not name:
        contacts = _CONTACTS.values()
    else:
        contacts = [name]
    if _CONTACTS:
        for item in contacts:
            for contact in item.values():
                print(contact)
    else:
        print('Телефонная книга пуста')


def find_contact(name: str):
    """
    Ищет контакт в телефонной книге по имени
    """
    contact = _CONTACTS.get(name)
    if contact:
        view_contacts(contact)
    else:
        print(f'Контакт {name} не найден')


def remove_contact(name: str):
    """
    Удаляет контакт из телефонной книги
    """
    contact = _CONTACTS.get(name)
    if contact:
        _CONTACTS.pop(name)
        print(f'Контакт {name} удален')
    else:
        print(f'Контакт {name} не сущестует в телефонной книге')


def export_contacts_txt():
    """
    Экспортирует телефонную книгу в файл формата txt
    """
    print('Телефонная книга сохранена в файл phone_book.txt')
    with open('phone_book.txt', 'w', encoding='utf-8') as f:
        for item in _CONTACTS.values():
            contacts = []
            for contact in item.values():
                contacts.append(contact)
            print(*contacts, file=f)


def export_contacts_csv():
    """
    Экспортирует телефонную книгу в файл формата csv
    """
    print('Телефонная книга сохранена в файл phone_book.csv')
    with open('phone_book.csv', 'w', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        for item in _CONTACTS.values():
            csv_writer.writerow(contact for contact in item.values())
