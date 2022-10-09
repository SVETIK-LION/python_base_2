import csv

_CONTACTS = {}


def create_contact() -> dict:
    """
    Создает контакт
    """
    name = input('Введите Имя и Фамилию (через пробел): ').split()
    address = input('Введите адрес проживания: ')
    phone = input('Введите номер телефона: ')

    contact = {
        'name': name,
        'address': address,
        'phone': phone
    }

    return contact


def add_contacts(contact: dict):
    """Добавляет контакты в телефонный справочник"""
    name = contact['name'][-1]
    _CONTACTS[name] = contact
    print(f'Контакт {name} успешно добавлен')


def remove_contact(name: str):
    """Удаляет контакт из телефонного справочника"""
    contact = _CONTACTS.get(name)
    if contact:
        _CONTACTS.pop(name)
        print(f'Контакт {name} успешно удален')
    else:
        print(f'Контакт {name} не сущестует в телефонной книге')


def view_contacts(name=None):
    """Отображает контакты"""
    print('Контакты в телефонной книге: ')

    if not name:
        lst_contacts = _CONTACTS.values()
    else:
        lst_contacts = [name]
    if _CONTACTS:
        for item in lst_contacts:
            for contact in item.values():
                print(contact)
    else:
        print('Телефонная книга пустая')


def find_contact(name: str):
    """Ищет контакт в телефонном справочнике"""
    contact = _CONTACTS.get(name)
    if contact:
        view_contacts(contact)
    else:
        print(f'Контакт {name} в телефонном справочнике не найден')


def export_contacts_txt():
    """Экспортирует все контакты в текстовый файл"""
    print('Телефонная книга успешна выгружена phone_book.txt файл')
    with open('phone_book.txt', 'w', encoding='utf-8') as f:
        for item in _CONTACTS.values():
            tmp = []
            for contact in item.values():
                tmp.append(contact)
            print(*tmp, file=f)


def export_contacts_csv():
    """Экспортирует все контакты в csv файл"""
    print('Телефонная книга успешна выгружена phone_book.csv файл')
    with open('phone_book.csv', 'w', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        for item in _CONTACTS.values():
            csv_writer.writerow(contact for contact in item.values())
