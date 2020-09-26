# Define class Person
class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

# Define class Name
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

myperson = Person(Name('Sam', 'Ham'), 'brown', 35)
print(myperson.name.first_name)
print(myperson.name.last_name)
print(myperson.eyecolor)
print(myperson.age)
