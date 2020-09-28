class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

myperson1 = Person(Name('Sam', 'Ham'), 'brown', 35)
myperson2 = Person(Name(myperson1.name.first_name, myperson1.name.last_name), myperson1.eyecolor, myperson1.age)
print('myperson1', myperson1.name.first_name, myperson1.name.last_name, 
        myperson1.eyecolor, myperson1.age, sep='\n')
print('-------------------------------------------')
print('myperson2', myperson2.name.first_name, myperson2.name.last_name, 
        myperson2.eyecolor, myperson2.age, sep='\n')
print('---------------------------------------')
print('changing copies eyecolors')
myperson2.eyecolor = 'blue'
print('myperson1.eyecolor:', myperson1.eyecolor)
print('myperson2.eyecolor:', myperson2.eyecolor)
print('---------------------------------------')
print('changing copies first names')
myperson2.name.first_name = 'Baz'
print('myperson1.name.first_name:', myperson1.name.first_name)
print('myperson2.name.first_name:', myperson2.name.first_name)
