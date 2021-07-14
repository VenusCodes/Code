#the last digit problem of spoj
# use binary expontentation
class Solution(object):
	def Main(self):
		list =[]
		n = int(input())
		for x in range(n):
			a,n = map(int, input().split())
			list.append((int(pow(a,n))%10))
		print(*list,sep="\n")

if __name__ == '__main__':
  Solution().Main()