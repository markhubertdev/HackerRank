    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        area = 0
        
        while l < r:
            a = height[l]
            b = height[r]
            area = max(area, min(a,b) * (r - l))
            if a < b:
                l += 1
            else:
                r -= 1
        return area