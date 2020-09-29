#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class. You don't
#actually have to copy/paste your previous code here if you
#don't want to, although you'll need to if you want to write
#some test code at the bottom.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.


#If you'd like to use the test code, paste your previous
#code here.

from typing import List, Union

class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False

class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

class Burrito:
    def __init__(self, meat, to_go, rice, beans, 
                extra_meat: bool = False, 
                guacamole: bool = False, 
                cheese: bool = False, 
                pico: bool = False, 
                corn: bool = False) -> None:
                self.set_meat(meat)
                self.set_to_go(to_go)
                self.set_rice(rice)
                self.set_beans(beans)
                self.set_extra_meat(extra_meat = extra_meat)
                self.set_guacamole(guacamole = guacamole)
                self.set_cheese(cheese = cheese)
                self.set_pico(pico = pico)
                self.set_corn(corn = corn)

    def set_meat(self, meat: str) -> None:
        self.meat = Meat(meat)
    
    def set_to_go(self, to_go: bool) -> None:
        self.to_go = to_go if isinstance(to_go, bool) else False
    
    def set_rice(self, rice: str) -> None:
        self.rice = Rice(rice)
    
    def set_beans(self, beans: str) -> None:
        self.beans = Beans(beans)
        
    def set_extra_meat(self, extra_meat: bool) -> None:
        self.extra_meat = extra_meat if isinstance(extra_meat, bool) else False
    
    def set_guacamole(self, guacamole: bool) -> None:
        self.guacamole = guacamole if isinstance(guacamole, bool) else False
    
    def set_cheese(self, cheese: bool) -> None:
        self.cheese = cheese if isinstance(cheese, bool) else False

    def set_pico(self, pico: bool) -> None:
        self.pico = pico if isinstance(pico, bool) else False

    def set_corn(self, corn: bool) -> None:
        self.corn = corn if isinstance(corn, bool) else False

    def get_meat(self) -> Union[str, bool]:
        return self.meat.get_value()
    
    def get_to_go(self) -> bool:
        return self.to_go
    
    def get_rice(self) -> Union[str, bool]:
        return self.rice.get_value()
    
    def get_beans(self) -> Union[str, bool]:
        return self.beans.get_value()
    
    def get_extra_meat(self) -> bool:
        return self.extra_meat
    
    def get_guacamole(self) -> bool:
        return self.guacamole
    
    def get_cheese(self) -> bool:
        return self.cheese
    
    def get_pico(self) -> bool:
        return self.pico
    
    def get_corn(self) -> bool:
        return self.corn

    def get_cost(self) -> float:
        cost = 5.00

        if self.get_meat() in ["chicken", "pork", "tofu"]:
            cost += 1.00
        elif self.get_meat() == 'steak':
            cost += 1.50

        if self.get_extra_meat():
            cost += 1.00

        if self.get_guacamole():
            cost += 0.75

        return cost

#Write your new function here.

def total_cost(burritos: List[Burrito]) -> float:
        return sum(burrito.get_cost() for burrito in burritos)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs. Note that these lines
#will ONLY work if you copy/paste your Burrito, Meat,
#Beans, and Rice classes in.
#
#If your function works correctly, this will originally
#print: 28.0

burrito_1 = Burrito("tofu", True, "white", "black")
burrito_2 = Burrito("steak", True, "white", "pinto", extra_meat = True)
burrito_3 = Burrito("pork", True, "brown", "black", guacamole = True)
burrito_4 = Burrito("chicken", True, "brown", "pinto", extra_meat = True, guacamole = True)
burrito_list = [burrito_1, burrito_2, burrito_3, burrito_4]
print(burrito_1.get_cost())
print(burrito_2.get_cost())
print(burrito_3.get_cost())
print(burrito_4.get_cost())
print(total_cost(burrito_list))