# tasks遍历一次存到dict 都提取出来
# 然后 依次遍历, -1.  不行, 不能把都用完, 所以count == 0就不用了, 省着下一次.
# 类似于流水线, 需要用字母来填充气泡
# 不能随便挑选, 剩余执行次数最多的那个任务，比如a快用完了,就用D
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict = {}
        res = 0
        for task in tasks:
            if task in dict:
                dict[task] +=1
            else:
                dict[task] =1
        m = max(dict.values())
        maxcount = sum( 1 for v in dict.values() if v == m)
        return max((m-1) *(n+1) +maxcount ,len(tasks) )
t = Solution()
print(t.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
print(t.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],2))
