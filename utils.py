import json
import os

path_student = os.path.join('data', 'students.json')
path_professions = os.path.join('data', 'professions.json')


def load_student_file(path):  # Загружает список студентов из файла

    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding="utf-8") as file:
        file = json.load(file)
        return file


def load_professions(path):  # Загружает список профессий из файла
    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding="utf-8") as file:
        file = json.load(file)
        return file


def get_student_by_pk(pk):  # Получает словарь с данными студента по его pk
    file = load_student_file(path_student)
    for data in file:
        if data["pk"] == pk:
            i = file.index(data)
            return file[i]
    else:
        print("Такого студента нет!")

def get_profession_by_title(title):  # Получает словарь с инфо о профе по названию
    file = load_professions(path_professions)
    for data in file:
        if data["title"] == title:
            i = file.index(data)
            return file[i]
    else:
        print("Такого студента нет!")


# def check_fitness(student, profession):
#     """
#     которая получив студента и профессию, возвращала бы словарь типа:
#     {
#       "has": ["Python", "Linux"],
#       "lacks": ["Docker, SQL"],
#       "fit_percent": 50
#     }
#     Эта функция должна использовать методы множеств.
#     """
#     pass
