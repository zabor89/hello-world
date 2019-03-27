import random, string
napis= input()
for letter in list(napis):
    print(chr(int(ord(letter)) + int(1)))
