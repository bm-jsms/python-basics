animal = "dog"
print(animal.upper())  # DOG
print(animal.capitalize())  # Dog
print(animal.replace("d", "c"))  # cog
print(animal.count("o"))  # 1

print(animal.find("d"))  # 0
print(animal.find("g"))  # 2
print(animal.find("x"))  # -1

print(animal.index("d"))  # 0


name = "  Josué emaxs  "
print(name.lower())  # josué emaxs
print(name.title())  # Josué Emaxs

print(name.strip())  # remove spaces
print(name.rstrip())  # remove spaces on the right
print(name.lstrip())  # remove spaces on the left

print("emaxs" in name)  # True
