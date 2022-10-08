from view import show_menu
from inputs import read_menu_number, read_contact_for_find
from contacts import (
    create_contact, add_contacts, find_contact,
    remove_contact, view_contacts, export_contacts_csv, export_contacts_txt
)


def start():
    """Запускает телефонную книгу"""
    run = True
    contact = {}
    while run:
        print('-' * 50)
        show_menu()
        menu_number = read_menu_number()
        if menu_number == 1:
            contact = create_contact()
        elif menu_number == 2 and contact:
            add_contacts(contact)
        elif menu_number == 3:
            view_contacts()
        elif menu_number == 4:
            name = read_contact_for_find()
            find_contact(name)
        elif menu_number == 5:
            name = read_contact_for_find()
            remove_contact(name)
        elif menu_number == 6:
            export_contacts_txt()
        elif menu_number == 7:
            export_contacts_csv()
        elif menu_number == 0:
            run = False
        else:
            print('*' * 100)
            print('Вы ввели недопустый пункт меню')
