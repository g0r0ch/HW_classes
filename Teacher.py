#-Преподаватель в инициализацию принимает контейнер предметов, которые ведёт
#- Преподавателям можно менять класс через set_class и читать их класс через get_class.
from Class import Class
from Human import Human
# from typing import List
from Subject import Subject
class Teacher(Human):
    _homeroom_class: Class | None
    _subjects: list[Subject]

    def __init__(self, name, last_name, subjects):
        super().__init__(name, last_name)
        self._subjects = list(subjects)

    def set_class(self, group):
        if isinstance(group, Class):
            self._homeroom_class = group
            group._homeroom_teacher = self
        else:
            raise Exception("Данный экземляр класса не найден")

    def get_class(self):
        return self._homeroom_class

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def __repr__(self):
        return f'{self.name} {self.last_name}'





