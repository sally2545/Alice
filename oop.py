class person:
    def __init__(self, firstname, age, gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender

    def details(self):
        print(self.firstname, "is studying")


teacher = person("Joe", 34, "male")
accountant = person("Mary", 32, "female")
doctor = person("George", 45, "male")

print(teacher.firstname, teacher.age, teacher.gender)
print(accountant.firstname, accountant.age, accountant.gender)
print(doctor.firstname,doctor.age,doctor.gender)
