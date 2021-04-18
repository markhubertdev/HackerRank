class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        result = []
        nums.sort()
        targetClose = 10000000000000000000000000000
        
        #print(nums)
        for i in range(len_nums):
          
            s = i + 1
            e = len_nums - 1
            
            while s<e:
                midEnd = e
                while s<midEnd:
                    sum = nums[s]+nums[midEnd]+nums[i]
                    if(sum == target):
                        found = target
                        
                        return found
                    else:
                        if(targetClose > abs(sum - target)):
                            targetClose = (abs(sum - target))
                            result.append(sum)
                        
                    midEnd -= 1
                s += 1
                
            
        return (result[len(result)-1])
            
        