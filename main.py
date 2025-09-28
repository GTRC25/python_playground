#In Python, no semicolon ( ; ) is needed at line ends (though optional).
#Parentheses are required around the string in Python 3.
print("Hello second world!")

#variables
x = 1000
y = 3.14
z = "string"

#Data types
num = 10  #int
pi = 3.14 #float
string_value = "python playground" #string
bool_value = True #bool
empty = None #NoneType

#conditionals
if x > 10:
    print("positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

#Loops (for)
for i in range(11):
    print(i)

for i in range(11, 21):
    print(i)

#(while)  #"subtract and assign" operator (n-=1)
# It means "subtract the value on the right from the variable on the left,
# and then assign the new value back to the variable".
n = 5
while n >= -2:
    print(n)
    n -= 1

#Dictionary
person = {
    "name": "Rajan",
    "Age": 26
}
print(person["name"])

#List

nums = [1,2,3]
nums.append(6)
print(nums[3])

#intermediate
#strings
s = "hello_mister"
print(len(s))
print(s.upper())
print(s[0:10])

#lists
numbs = [1, 2, 3]       # Create a list with elements 1, 2, and 3.
numbs.append(4)         # Add the number 4 to the end of the list. Now numbs is [1, 2, 3, 4].
numbs.pop()             # Remove and return the last element from the list (which is 4). List is back to [1, 2, 3].
numbs.pop(0)            # Remove and return the element at index 0 (which is 1). List becomes [2, 3].
numbs.insert(0, 10)      # Insert 10 at index 0. List becomes [0, 2, 3].
print(10 in numbs)       # Check if 2 is present in the list. Prints True because 2 is in the list.

#loop helpers
numbers = [10,20,30]

for val in numbers:
    print(val)

for i, val in enumerate(numbers):
    print(i, val) #use enumerate() for index + value.

#*args/**kwargs
def greet(name = "Guest"):
    return f"Hello {name}" #An f-string is a special kind of string in Python introduced in Python 3.6 that allows you to embed expressions or variables inside curly braces {} within the string itself.

def sum_all(*nums):   #The *nums means this function can take any number of arguments
                      # (called variable-length arguments).
    return sum(nums)

print(greet())
print(sum_all(1,2,3,4,5,6))

#Error handling
try:
    x = int("oops")
except ValueError as err:
    print("Error:", err)
finally:
    print("Done")


# math_utils.py
def add(a, b):
        return a + b
# main.py
#from math_utils import (add)
print(add(2, 3))










