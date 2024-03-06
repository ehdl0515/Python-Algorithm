"""
https://www.acmicpc.net/problem/2720

입력으로 받는 게 무엇인지 정확히 파악해야 함
거스름돈만 받는 줄 알았는데, 총 개수도 받고 있었음
"""

data = int(input())

for i in range(data):

	cents = int(input())

	quaters = int(cents // 25)
	cents -= quaters * 25

	dimes = int(cents // 10)
	cents -= dimes * 10

	nickels = int(cents // 5)
	cents -= nickels * 5

	answers = map(str, [quaters, dimes, nickels, cents])
	print(" ".join(answers))
