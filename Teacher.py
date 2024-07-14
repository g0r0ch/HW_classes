#-Преподаватель в инициализацию принимает контейнер предметов, которые ведёт
#- Преподавателям можно менять класс через set_class и читать их класс через get_class.

class Teacher(Human):
    _homeroom_class: Class | None
    _subjects: List[Subject]
