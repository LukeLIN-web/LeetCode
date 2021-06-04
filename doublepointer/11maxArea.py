#    max(  min ( ai , aj ) * (i - j)  )
#  
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        m = 0
        while l < r:
            tmp = min(height[l],height[r])*(r-l) # 有两处出现就可以设置变量了,  代码改起来快,然后速度快一些
            if m < tmp:
                m = tmp
            if height[l] <height[r]:
                l +=1
            else:
                r -=1
        return m


