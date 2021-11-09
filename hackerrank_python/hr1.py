#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    thelist = []
    for i in range(N):
        string = input()
        string = string.split()
        if 'insert' in string:
            thelist.insert(int(string[1]),int(string[2]))

        elif 'print' in string :
            print(thelist)
        
        elif 'remove' in string :
            thelist.remove(int(string[1]))
        
        elif 'append' in string :
            thelist.append(int(string[1]))
        elif 'sort' in string : 
            thelist = sorted(thelist)

        elif 'pop' in string:
            thelist.pop()

        elif 'reverse' in string:
            thelist.reverse()
