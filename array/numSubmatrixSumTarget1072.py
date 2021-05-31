# 递推公式, 能不能不要把整个矩阵每次都重新加起来, 每次计算, 时间复杂度是n^2
# 找和target的差距, 然后所有0的数量. 这样是 时间复杂度2n
# 不用维护一个二维, 其实一个list, 然后每次算完把答案加sum里就可以了.
# 注意从0到n递推动态规划是不对的,忽略了 中间里面的小矩阵.
# 我们枚举子矩阵的上下边界，并计算出该边界内每列的元素和，则原问题转换成了如下一维问题：
# 给定一个整数数组和一个整数 \textit{target}target，计算该数组中子数组和等于 \textit{target}target 的子数组个数。
# 力扣上已有该问题：560. 和为K的子数组，读者可以参考其官方题解，并掌握使用前缀和+哈希表的线性做法。
# 对于每列的元素和 \textit{sum}sum 的计算，我们在枚举子矩阵上边界 ii 时，初始下边界 jj 为 ii，此时 \textit{sum}sum 就是矩阵第 ii 行的元素。每次向下延长下边界 jj 时，我们可以将矩阵第 jj 行的元素累加到 \textit{sum}sum 中。

#给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], k: int) -> int:
        def getSumArray(nums: List[int], k: int) -> int:
            mp = Counter([0])#  map 记忆化
            count = pre = 0
            for x in nums:
                pre += x 
                if pre - k in mp:  # k 是目标
                    count += mp[pre - k]
                mp[pre] += 1 
            return count         
        width = len(matrix[0])
        height = len(matrix)
        ans = 0
        #复杂度 高度^2 * width
        #这个遍历顺序是非常难想的, 他是先第一行矩阵 小到大, 然后第一行加第二行, 加第三行
        # 之后上边界到第二行, 第二行加第三行.
        for i in range(height): #枚举上边界
            total = [0] * width
            for j in range(i, height,1): # 枚举下边界.
                for c in range(width):
                    total[c] += matrix[j][c]
                ans += getSumArray(total,k)
        return ans
