import os

from utils import get_student_by_pk

path_student = os.path.join('data', 'students.json')
path_professions = os.path.join('data', 'professions.json')

number_student = int(input("Введите номер студента: "))
student = get_student_by_pk(number_student)

print(f"Студент {student['full_name']}")
print(f"Знает {' '.join(student['skills'])}")


