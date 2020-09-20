class Name:
    def __init__(self):
        self.first_name = '[no first name]'
        self.last_name = '[no last name]'

mydictionay = {'first name': 'Kais', 'last name': 'Chebata'}
my_name = Name()
my_name.first_name = 'Kais'
my_name.last_name = 'Chebata'

print('Dictionay:', mydictionay['first name'])
print('Instance:', my_name.first_name)