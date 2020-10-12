#Imagine you're writing a program to check attendance on a
#classroom roster. The list of students in attendance comes
#in the form of a list of instances of the Student class.
#
#You don't have access to the code for the Student class.
#However, you know that it has at least two attributes:
#first_name and last_name.
#
#Write a function called check_attendance. check_attendance
#should take three parameters: a list of instances of
#Student representing the students in attendance, a first
#name as a string, and a last name as a string (in that
#order).
#
#The function should return True if any instance in the
#list has the same first and last name as the two
#arguments. It should return False otherwise.
#
#You may assume that the list of students is sorted
#alphabetically, by last name and then by first name. This
#allows you to solve this with a binary search. However,
#you may also solve this problem with a linear search if
#you would prefer.


#Write your function here!



#If you would like, you may implement the Student class as
#described and use it to test your code. This is not
#necessary to complete the problem, but it may help you
#debug. If you create a Student class, all you need is
#a constructor that assigns values to two attributes:
#self.first_name and self.last_name.
