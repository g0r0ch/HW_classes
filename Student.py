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


 def set_class(self, cl: Class):
        if isinstance(cl, Class):
            self._class = cl
            cl.append(self)
        else:
            raise Exception("Данный экземляр класса не найден")

    def get_class(self):
        return self._class

    def __str__(self):
        return f'Ученик {self.name} {self.last_name}, {self._class}'

    def __repr__(self):
        return f'{self.name} {self.last_name}'
