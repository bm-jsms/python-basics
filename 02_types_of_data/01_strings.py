myVariable = "Hello World"

myDescription = """ 
This is a long string
that spans multiple lines 
"""

print(myVariable, myDescription)

print(len(myVariable))  # 11

print(myVariable[0])  # H
print(myVariable[0:5])  # Hello
print(myVariable[6:])  # World
print(myVariable[-1])  # d
print(myVariable[-5:])  # World
print(myVariable[:11])  # Hello World
print(myVariable[:])  # Hello World

print(myVariable[0::2])  # HloWrd
print(myVariable[0::3])  # HlWl

print(myVariable[::-1])  # dlroW olleH
