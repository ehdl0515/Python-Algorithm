"""
https://www.acmicpc.net/problem/11047

"""

n, k = map(int, input().split())
prices = list()
for _ in range(n):
	prices.append(int(input()))
prices.sort(reverse=True)

answer = 0
for price in prices:
	if price <= k:
		share = k // price
		k = k - price * share
		answer += share

print(answer)