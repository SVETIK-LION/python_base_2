import models
from ui.ui_input import *
from ui.ui_view import *


def run():
    menu_number = 1
    while menu_number != MENU_EXIT:
        show_menu()
        menu_number = read_menu_number()

        if menu_number == MENU_UNIVERSITY_INFO:
            show_university(models.university)

        elif menu_number == MENU_GROUP_LIST:
            show_groups(models.groups)

        elif menu_number == MENU_ADD_GROUP:
            group = input_group()
            models.add_group(group)
            show_group_info(group)

        elif menu_number == MENU_ALL_STUDENTS:
            show_students(models.students)

        elif menu_number == MENU_ADD_STUDENT:
            student = input_student()
            models.add_student(student)
            show_student_info(student)

        elif menu_number == MENU_FIND_STUDENT:
            student_id = input_student_id()
            student = models.find_student(student_id)
            show_student_info(student)

        elif menu_number == MENU_REMOVE_STUDENT:
            student_id = input_student_id()
            student = models.remove_student(student_id)
            show_student_info(student)

        elif menu_number == MENU_PUSH_STUDENTS_GROUP:
            db = models.push_students_db()
            show_db(db)

        elif menu_number == MENU_PULL_DATA_FROM_FILE:
            models.pull_students_from_db()

        elif menu_number == MENU_STUDENTS_IN_GROUP:
            group_id = input_group_id()
            students = models.find_students_group(group_id)
            show_list_item(students)
