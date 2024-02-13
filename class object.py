# class is a blueprint of an object
# An object is an instance of a class
class person:
    # properties/attributes/characteristics
    age = 23
    name = "Bill"
    #method/function/behaviour

    def talk(self):
        print("person is talking")

teacher = person()
print(teacher.name)
print(teacher.age)

teacher.talk()