#https://www.hackerrank.com/challenges/python-tuples/problem?h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(input())
    #get the elements into a list 
    # list to tuple
    # tuple to hash
    print(hash(tuple(list(int(N) for N in input().strip().split())[:n])))