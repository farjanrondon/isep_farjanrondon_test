
import random as rd

players = int(input('Players: '))
scores = []

for i in range(players):
	scores.append(rd.randint(0, 20))

print('\nScores: ', scores)
print('Max score: ', max(scores))
print('Last score: ', scores[players-1])

scores.sort(reverse=True)
print('\n1st: ', scores[0])
print('2nd: ', scores[1])
print('3rd: ', scores[2])
