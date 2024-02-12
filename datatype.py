# Data Types
number = 45  # int
num = 56.78  # float
greeting = "Hello there"  # str
IsPythonInteresting = True  # bool

# Variable storing multiple values
Languages = ["python", "php", "java"]  # list
fruits = ("apple", "banana", "pineapple")  # tuple
countries = {"kenya", "china", "USA"}  # set
# dictionary
details = {
    "firstname": "Sally",
    "age": 17,
    "course": "MIT",
    "nationality": "North America"
}
print(details["nationality"])
print(details["course"])
print(number)
print(greeting)
print(countries)
print(IsPythonInteresting)
print(details)

# determining the datatype
print(type(details))
print(type(countries))

# Type casting . converting one data type to another

print(float(number))
print(int(num))
