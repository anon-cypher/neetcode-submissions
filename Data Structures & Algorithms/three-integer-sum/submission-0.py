class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(nums)-1

        nums = sorted(nums)
        print(nums)

        while i<n:
            target = -nums[i]
            j = i+1
            k = n
            while j<k:
                if nums[j]+nums[k]==target:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                
                elif nums[j]+nums[k]<target:
                    j+=1
                elif nums[j]+nums[k]>target:
                    k-=1
            i+=1
        
        return res

        
