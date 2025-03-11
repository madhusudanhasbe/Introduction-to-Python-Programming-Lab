
user_dict = {"A":"1234", "B":"4567", "C":"7890", "D":"0123", 'E':'3456'}
a = ["D", "E", "F", "G"]
value = 0

print("Use of fromkeys")
print(f"The list of keys are {a}")
print(f"The value each key wil have: {value}")
print(f"The created dictionary: {dict.fromkeys(a, value)}")

print()

print("Use of clear")
print(f"Before applying clear function: {user_dict}")
user_dict.clear()
print(f"After applying clear function: {user_dict}")

