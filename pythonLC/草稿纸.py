# from collections import Counter, deque
# from typing import List
# l = [[0,2,2],[4,2,4],[2,13,1000000000]]
import collections
num = list(map(int,input().split(" ")))
b = num[0] + num[1]
s = str(b)
if s[0] == "-":
    res = "-"
else:
    res = s[0]
count = 0
s = s[1:]
for i in s:
    res += i
    count +=1
    if count ==3:
        count ==0
        res += ","
print(res)
exit(0) 