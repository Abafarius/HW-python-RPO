import person
class Teacher(person.Person):
    __subject = ""
    _instance = None

    def __new__(cls, full_name, age, gender, subject):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, full_name: str, age: int, gender, subject):
        super().__init__(full_name, age, gender)
        self.__subject = subject

    @property
    # getter
    def subject(self):
        return self.__subject

    def set_subject(self, new_sub):
        self.__subject = new_sub

    def __str__(self):
        return f"Teacher: {self.first_name()} {self.last_name()} of subject {self.__subject}"
#singleton
vitaliy = Teacher("Vitaliy Nemikin", 39, "male", "python")
print(vitaliy)
Altynay = Teacher("Altynay Altynay", 22, 'female', "html")
print(Altynay)

Altynay.set_subject("JS")

print(Altynay.subject)
print(vitaliy.subject)

print(vitaliy.first_name())
