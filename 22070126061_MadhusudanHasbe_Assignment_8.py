alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

print(f"The first three letters are: {alphabet_list[0:3]}")

print(f"Any three letters from middle are: {alphabet_list[3:6]}")

x = int(input("Enter the start index of letter you want: "))
y = int(input("Enter the end index of letter you want: "))

print(f"The letter at index : {alphabet_list[x:y+1]}")