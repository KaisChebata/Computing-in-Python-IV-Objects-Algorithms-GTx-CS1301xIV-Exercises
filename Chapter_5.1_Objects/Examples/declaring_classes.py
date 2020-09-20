# Define the class Name
class Name:
    def __init__(self):
        self.first_name = '[no first name]'
        self.last_name = '[no last name]'

# Define the class Person
class Person:
    def __init__(self):
        self.name = Name()
        self.eye_color = '[no eyd color]'
        self.age = -1


new_person = Person()
print(new_person.name.first_name)
print(new_person.eye_color)
