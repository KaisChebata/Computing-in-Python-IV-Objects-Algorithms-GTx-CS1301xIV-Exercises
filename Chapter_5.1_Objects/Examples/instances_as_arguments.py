class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

def capitalize(name):
    name.first_name = name.first_name.upper()
    name.last_name = name.last_name.upper()

def capital_all(a_string):
    a_string = a_string.upper()

myname = Name('Sam', 'Ham')
myperson = Person(myname, 'brown', 35)

# the two line below will not affect the name instance because the function is operate on
# immutable object which is here a string, whereas the other function will affect because it 
# operate on an object attribute values which the object itself is not mutable.
# capital_all(myperson.name.first_name)
# capital_all(myperson.name.last_name)
capitalize(myperson.name)
print(myperson.name.first_name, myperson.name.last_name, sep='\n')
