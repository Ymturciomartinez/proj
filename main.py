string1 = input('Enter the message you would like to encode: ')

increment = int(input('Enter the increment you would like to encode message by: '))


string2 = ""
for i in string1:
        x = chr(ord(i) + increment)
        string2 += x

print(string2)
