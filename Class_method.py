class Student:
    subject = "python"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def get_subject(cls):
        return cls.subject

    @classmethod
    def set_subject(cls,new_subject):
        cls.subject = new_subject

print(Student.get_subject())

Student.set_subject("Flutter")
print(Student.get_subject())
