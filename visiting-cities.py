def solve(s,K: int):
        length = len(s)
        address=[i for i in range(length) if s[i]=='1']
        count = len(address)
        for i in address:
                #left side of starting point
                if i-K>0:
                        for n in range(i-K,i):
                                if s[n]=='0':
                                        count +=1
                                        s = s[:n] + '1' + s[n+1:]
                else:
                        for n in range(0,i):
                                if s[n]=='0':
                                        count +=1
                                        s = s[:n] + '1' + s[n+1:]

                #right side of starting point
                if i+K<length:
                        for n in range(i,i+K+1):
                                if s[n]=='0':
                                        count +=1
                                        s = s[:n] + '1' + s[n+1:]

                else:
                        for n in range(i,length):
                                if s[n]=='0':
                                        count +=1
                                        s = s[:n] + '1' + s[n+1:]
        return count



print(solve('00100100',1))
print(solve('0010100',1))
