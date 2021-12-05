def solution(inputString):
	print(inputString + ' ' + inputString[::-1])
	return inputString == inputString[::-1]

print(solution("aabaa"))
print(solution("abac"))
print(solution("a"))