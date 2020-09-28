# Copy your Burrito class from the last exercise. Now,
# write a getter and a setter method for each attribute.
# Each setter should accept a value as an argument. If the
# value is a valid value, it should set the corresponding
# attribute to the given value. Otherwise, it should set the
# attribute to False.
#
# Edit the constructor to use these new setters and getters.
# In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
# new_burrito.meat would be False because "spaghetti" is not
# one of the valid options. Note that you should NOT try to
# check if the new value is valid in both the constructor and
# the setter: instead, just call the setter from the
# constructor using something like self.set_meat(meat).
#
# Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
# Make sure you name each setter with the format:
# "set_some_attribute" and "get_some_attribute"
#
# For example, the getter for meat would be get_meat. The
# getter for to_go would be get_to_go.
#
# Hint: Your code is going to end up *very* long. This
# will be the longest program you've written so far, but
# it isn't the most complex. Complexity and length are
# often very different!
#
# Hint 2: Checking for valid values will be much easier
# if you make a list of valid values for each attribute
# and check the new value against that.


# Write your code here!