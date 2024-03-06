"""
https://www.acmicpc.net/problem/11399

- sorted() 함수와 list.sort() 메서드의 차이
- 다 풀고 생각해보니, 굳이 index_minutes 변수를 만들 필요가 없었다.
  그냥 시간 순서대로 오름차순 정렬하고 이를 조건에 맞게 더하면 된다..
"""

persons = int(input())
spend_minutes = list(map(int, input().split()))
index_minutes = list()

for idx, minutes in enumerate(spend_minutes, start=1):
	index_minutes.append((idx, minutes))

sorted_minutes = sorted(index_minutes, key=lambda x: x[1])

answer = 0
for count, minutes in enumerate(sorted_minutes):
	answer += minutes[1] * (len(sorted_minutes) - count)

print(answer)