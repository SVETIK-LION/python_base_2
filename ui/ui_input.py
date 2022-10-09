from .ui_view import MENU_ITEMS


def read_menu_number():
    menu_number_check = False
    menu_number = None
    while not menu_number_check:
        menu_number = input("Введите пункт меню: ")
        if not menu_number.isdigit():
            print('Введите число!')
            continue
        menu_number = int(menu_number)
        if -1 < menu_number <= len(MENU_ITEMS):
            menu_number_check = True
        else:
            print('Такого пункта нет!')
    return menu_number


def input_group():
    name = input("Название: ")
    course_id = int(input("Номер курса: "))
    return {"name": name, "course_id": course_id}


def input_student():
    fio = input("ФИО: ")
    group_id = int(input("Номер группы: "))
    return {"fio": fio, "group_id": group_id}


def input_student_id():
    student_id = int(input('Введите номер id студента: '))
    return student_id


def input_group_id():
    group_id = int(input('Введите номер id группы: '))
    return group_id
