# class Name:
#     def __init__(self):
#         self.first_name = '[no first name]'
#         self.last_name = '[no last name]'

class Person:
    def __init__(self):
        self.first_name = '[no first name]'
        self.last_name = '[no last name]'
        self.eye_color = '[no eye color name]'
        self.age = -1

my_person1 = Person()

print(my_person1.first_name)
my_person1.first_name = 'Kais'
print('my_person1.first_name = "Kais" ->', my_person1.first_name)
print(my_person1.last_name)
print(my_person1.eye_color)
print(my_person1.age)
print('----------------------------------------------------------')
my_person2 = Person()
my_person3 = Person()

my_person2.first_name = 'Sam'
my_person3.first_name = 'Ham'
print('my_person2:', my_person2.first_name)
print('my_person3:', my_person3.first_name)

