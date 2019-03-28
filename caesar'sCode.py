import random, string
napis= input("Enter message:")
key= input("Enter the key:")
for letter in list(napis):
    print(chr(int(ord(letter)) + int(key)),end='')
