class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = first_name

myperson1 = Person(Name('Sam', 'Ham'), 'brown', 35)
myperson2 = myperson1

myperson2.eyecolor = 'blue'

print('myperson1.eyecolor: ', myperson1.eyecolor)
print('myperson2.eyecolor: ', myperson2.eyecolor)

