Contact = {'A':'1234567890', 'B':'2345678901', 'C':'3456789012'}
Name = input("Enter the name: ")
def Digit_Checker(Naam):
    Number = input("Enter contact no.: ")
    if len(Number) == 10:
        Contact[Name] = Number
        print ("Contact No. of", Name, 'is', Contact[Name])
        print ("Contact list:", Contact)
    else:
        print ("Enter valid 10 digit number. Retype the number")
        Digit_Checker(Name)
if Name in Contact:
    print ("Contact No.:", Contact[Name])
    print ("Contact list:", Contact)
else:
    A = input ("Not present in Contacts. Do you wish to add? ")
    if A.lower() == 'yes':
        Digit_Checker(Name)
    elif A.lower() == 'no':
        print ("Contact not added.")