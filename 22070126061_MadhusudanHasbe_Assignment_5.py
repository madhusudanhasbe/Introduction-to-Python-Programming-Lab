def rotate_word(the_string, rot_num):
    for letter in the_string:
        if  letter == the_string[0]:
            print(letter, end = "")
        else:
            as_code = ord(letter)
            new_code = as_code + rot_num
            new_letter = chr(new_code)

            print(new_letter, end='')

input_string = input("Enter your string: ")
num = int(input("Enter the rotation number: "))

rotate_word(input_string, num)