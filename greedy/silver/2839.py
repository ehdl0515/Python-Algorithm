"""
https://www.acmicpc.net/problem/2839

- 어떤 경우가 제일 최적의 해이며, 그 후순위도 판단한다
    - 5 로만 나뉘는 경우
    - 5와 3으로 나뉘는 경우
    - 3으로만 나뉘는 경우
    - 나뉘지 않는 경우

"""

weight = int(input())
answer = 0

if weight % 5 == 0:
	answer += int(weight // 5)
else:
	while True:
		weight -= 3
		answer += 1
		if weight % 5 == 0:
			answer += int(weight // 5)
			break
		elif weight == 1 or weight == 2:
			answer = -1
			break
		elif weight == 3:
			answer += 1
			break

print(answer)
