a = []
sets = {}
for i in range(int(input())):
    name = input()
    score = float(input())
    sets.add(score)
    a.append((name,score))
sets = sorted(sets)
for pair in a:
    if pair.second == sets[1]:
        print(pair.first)