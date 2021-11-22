string = input().strip()
print(str(str('+1')*string.count('1')+str('+2')*string.count('2')+str('+3')*string.count('3'))[1:])