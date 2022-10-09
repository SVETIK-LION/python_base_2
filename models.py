
"""
Название ВУЗ-а

Информация о преподавателе
Курс
название
группа
Информация о студенте
фио
группа
"""

import pickle

university = {
    "name": "Рактостроения",
    "address": "г.Москва, ул.Левобержная, 1 с.5"
}

courses = [
    {
        "id": 1,
        "name": "Python разработчики",
        "duration": 1,
    },
    {
        "id": 2,
        "name": "C++ разработчики",
        "duration": 2
    }
]

groups = [
    {
        "id": 100,
        "name": "g100",
        "course_id": 1
    },
    {
        "id": 101,
        "name": "g101",
        "course_id": 2
    }
]

students = [
    {
        "id": 1001,
        "fio": "Ivan Petrov",
        "group_id": 100,
    },
    {
        "id": 1002,
        "fio": "Petya Maximov",
        "group_id": 100
    }
]


def add_group(group):
    assert group, "Нет группы!"
    # достать последнюю группу и увеличить id + 1
    group["id"] = groups[-1]["id"] + 1
    groups.append(group)


def add_student(student):
    assert student, "Студент None"
    student["id"] = students[-1]["id"] + 1
    students.append(student)


def find_student(_id):
    for s in students:
        if s["id"] == _id:
            return s

    return None


def remove_student(_id):
    idx = 0
    for s in students:
        if s["id"] == _id:
            idx = students.index(s)
            break

    return students.pop(idx)


def push_students_db():
    with open('students_db', 'wb') as file_db:
        db = groups, students
        pickle.dump(db, file_db)

    return db


def pull_students_from_db():
    global groups, students
    with open('students_db', 'rb') as file_db:
        groups, students = pickle.load(file_db)


def find_students_group(group_id):
    lst_st_group = [st for st in students if st["group_id"] == group_id]

    return lst_st_group if lst_st_group else None
