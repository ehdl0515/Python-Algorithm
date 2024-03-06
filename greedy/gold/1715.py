"""
https://www.acmicpc.net/problem/1715

- 일반 리스트로 하는 경우, 최소값을 찾기 위해 항상 정렬해주어야 하므로
  시간 초과가 뜰 수 밖에 없다
- heap 자료구조를 이용해 최소값을 찾자!
"""

"""
# 시간초과

n = int(input())
cards = [int(input()) for _ in range(n)]
cards.sort()
answer = 0

while len(cards) > 1:
	a = cards.pop(0)
	b = cards.pop(0)
	answer += (a + b)
	cards.append(a + b)
	cards.sort()

print(answer)
"""
import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

answer = 0
while len(cards) > 1:
	a = heapq.heappop(cards)
	b = heapq.heappop(cards)
	answer += (a + b)
	heapq.heappush(cards, a + b)

print(answer)

