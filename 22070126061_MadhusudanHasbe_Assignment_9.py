string = input("Enter the string in which you want to count the strings: ")
occur = input("Enter the occurence you want to count: ")
count = 0

for letter in string.lower():
    if letter == occur:
        count += 1
    else:
        pass

print(f"The total occurenence in the string = {count}")