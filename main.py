# ШАГ. Д/з по сроку 14/08/2023. Сериализация pickle.
"""
Список людей на проекте (похожее на то что делали на занятии)

Действия:
    - Запись в файл(при выходе);
    - чтение из файла(при запуске программы);
    - Добавление человека на проект;
    - удаление человека с проекта;
    - получение списка людей на проекте;
    - есть ли человек на проекте.

В список людей должен храниться в алфавитном порядке
"""
from datetime import date

from clss.user import User
from clss.project import Project
import pickle


def save_project(obj: Project):
    file_name: str = f'.\\project-{obj.name}.pickle'
    with open(file_name, 'wb') as file:
        pickle.dump(obj, file, protocol=4)


def load_project(file_name: str):
    with open(file_name, 'rb') as file:
        res: Project = pickle.load(file)
    return res


users = list(
    [
        User('Nikolay', 'Zalivko', 'zalivkonikolay', '111'),
        # User('Denis', 'Zalivko', 'zalivkodenis', '123'),
        # User('Aleksandr', 'Situn', 'situnaleksandr', '321'),
        User('Maria', 'Zalivko', 'zalivkomaria', '777')
    ]
)

print(' Instant users: '.center(40, '*'))
for _ in users:
    for line in str(_).split('\n'):
        print(f'\t{line}')
# ************ Instant users: ************
# 	id=0: Zalivko Nikolay:
# 		login:		zalivkonikolay
# 		password:	111
# 	id=1: Zalivko Maria:
# 		login:		zalivkomaria
# 		password:	777


project = Project('step-00', date(2023, 5, 4), date(2024, 6, 1), list(users))

print(project)
# ****************************************
# id=0
# Project name:	step-00
# Start project:	2023-05-04
# End project:	2024-06-01
# ---------------- Users -----------------
# 	id=1: Zalivko Maria:
# 		login:		zalivkomaria
# 		password:	777
# 	id=0: Zalivko Nikolay:
# 		login:		zalivkonikolay
# 		password:	111


project1 = load_project('.\\project-step.pickle')

print(project1)
# ****************************************
# id=1
# Project name:	step
# Start project:	2023-05-04
# End project:	2024-06-01
# ---------------- Users -----------------
# 	id=2: Situn Aleksandr:
# 		login:		situnaleksandr
# 		password:	321
# 	id=1: Zalivko Denis:
# 		login:		zalivkodenis
# 		password:	123
# 	id=3: Zalivko Maria:
# 		login:		zalivkomaria
# 		password:	777
# 	id=0: Zalivko Nikolay:
# 		login:		zalivkonikolay
# 		password:	111


# save_project(project)
