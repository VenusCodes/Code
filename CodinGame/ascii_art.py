import sys
import math

# Auto-generated code below aims at helping you parse
# the staandard input according to the problem statement.

length = int(input())
height = int(input())
letter = str(input())
letter = letter.upper()
alphabet = [str(input()) for i in range(height)]

for i in range(height):
    for ch in letter:
        if ch.isalpha():
            number = ord(ch) - ord('A')
        else:
            number = 26

        for j in range(length):
            print(alphabet[i][number*length + j],end="")

    print("")
