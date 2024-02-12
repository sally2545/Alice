# Inbuilt functions
number = max(89, 78, 34, 93, 45)
print(number)

x = min(56, 75, 64, 43, 35)
print(x)

z = pow(2, 3)
print(z)


# user defined functions
def name():
    print("sally")


name()  # Calling a function


def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


# Parameters/variables and arguments/values

def student(name, age, course):
    print(name, age, course)


student("Grace", 17, "MIT")
student("Ken", 18, "MIT")
student("Prudence", 17, "MIT")
student("Aqua", 19, "MIT")


def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)


employees("Suzanne", 20, "female", "Assistant", "ksh.20,000")
employees("Samuel", 22, "male", "Manager", "ksh.50,000")
employees("Sally", 25, "female", "CEO", "ksh.300,000")
employees("Anita", 24, "female", "Treasurer", "ksh.20,000")
employees("Elly", 21, "male", "secretary", "ksh.25,000")
