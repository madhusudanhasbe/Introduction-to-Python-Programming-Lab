txt = input("Enter txt file location: ")
op = open(txt, 'r')
x = op.read()
y = ''.join(char for char in x if char.isalpha())
freq = {}
for i in y.lower():
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print (freq)