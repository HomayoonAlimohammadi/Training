# from collections import deque

string = input()
n = int(input())

for i in range(n):
    s, e = input().split()
    s, e = int(s), int(e)

    substring = string[s, e]