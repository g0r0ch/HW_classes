#- Школьники в инициализацию могут принимать ещё и класс (не обязательно)
#- Школьникам можно менять класс через set_class и читать их класс через get_class.
from Human import Human
#from Class import Class
class Student(Human):
    def __init__(self, name, last_name, group=None):
        super().__init__(name, last_name)
        self._class = group


    def set_class(self, group):
        pass

    def get_class(self):
        pass


