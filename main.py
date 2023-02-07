import os

from utils import get_student_by_pk, get_profession_by_title

path_student = os.path.join('data', 'students.json')
path_professions = os.path.join('data', 'professions.json')

number_student = int(input("Введите номер студента: ").capitalize().strip())
student = get_student_by_pk(number_student)

print(f"Студент {student['full_name']}")
print(f"Знает {' '.join(student['skills'])}")

professions_student = input(f"Выберите специальность для оценки студента {student['full_name']}: ").capitalize().strip()
professions = get_profession_by_title(professions_student)

a = student['skills']
b = professions['skills']
print(a)
print(b)

# Программа: Пригодность 50%
# Программа: Jane Snake знает Python, Linux
# Программа: Jane Snake не знает Docker, SQL
#
# # Пользователь: Backend
