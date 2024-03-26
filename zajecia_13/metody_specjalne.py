class Student:
    def __init__(self, name, surname, sex, age):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

    def __repr__(self):
        return f"Student o imieniu {self.name} nazwisku {self.surname}"

    def __int__(self):
        return self.age

    def __str__(self):
        return f"Student o imieniu {self.name} nazwisku {self.surname} string"

    def __bool__(self):
        return True if self.sex == "male" else False





student_1 = Student(name="Michal", surname="Zietkowski", sex="male", age=28)
print(int(student_1))
print(str(student_1))
print(bool(student_1))
