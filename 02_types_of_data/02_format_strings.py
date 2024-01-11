name = "Josué"
age = 19

complete_message = "My name is " + name + " and I am " + str(age) + " years old."
print(complete_message)

complete_message = "My name is {} and I am {} years old.".format(name, age)
print(complete_message)

complete_message = f"My name is {name} and I am {age} years old."

test = f"{name[0]} {10*2}"
print(test)  # J 20
