# File not found

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Mi primer texto")
except KeyError as error:
    print(f"La palabra {error} no existe")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File has been closed")

# Raise my own exceptions
    raise

height = float(input("Your height in m: "))
weight = int(input("Your weight in kg: "))

if height > 3:
    raise ValueError("Height must be below 3 meters")

bmi = weight / height ** 2
print(bmi)




