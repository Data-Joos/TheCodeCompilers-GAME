class IngenSträngException(Exception):
    
    def __init__(self, message="Det var ingen sträng"):
        self.message = message


class TomSträngException(Exception):

    def __init__(self, message="Strängen ska inte vara tom"):


class Student:
    def __init__(self, namn):
        if type(namn) is not str:
            raise IngenSträngException  
        self.namn = namn 


nyElev = Student("Johanna")
ytterligareElev = Student("")

try:
    annanElev = Student(None)
    print(nyElev.namn)
    print
except: