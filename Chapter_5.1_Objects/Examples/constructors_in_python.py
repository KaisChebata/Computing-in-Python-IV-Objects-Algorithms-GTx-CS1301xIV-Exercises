#Define the Class Person
class Person:
    # Create new instance of Person
    def __init__(self, first_name='[no first name]', last_name='[no last name]'):
        self.first_name = first_name
        self.last_name = last_name
        self.eyecolor = '[no eye color]'
        self.age = -1

myperson1 = Person('Sam', 'Ham')
myperson2 = Person()
print(myperson1.first_name)
print(myperson1.last_name)
print(myperson2.first_name)
print(myperson2.last_name)
