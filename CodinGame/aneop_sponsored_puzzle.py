import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



speed = int(input())
light_count = int(input())
lights = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    lights.append([distance,duration])

def isRed(speed,distance,duration):
        return (18 * distance) % (10 * speed * duration) >= (5 * speed * duration)

for i in range(light_count):
    if(isRed(speed,lights[i][0],lights[i][1])):
        spedd = speed -1
        i = i-1

print(speed)