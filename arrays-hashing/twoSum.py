import time
from memory_profiler import memory_usage


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        length = len(nums)
        for i in range(length):
            diff = target - nums[i]
            if diff not in d:
                d[diff] = i
            if nums[i] in d and i != d[nums[i]]:
                return [d[nums[i]], i]


sol = Solution()


nums = [2, 7, 11, 15]
target = 9

start_time = time.time()

mem_usage_before = memory_usage()[0]

result = sol.twoSum(nums, target)

end_time = time.time()

mem_usage_after = memory_usage()[0]

print(f"Time taken: {end_time - start_time} seconds")
print(f"Memory used: {mem_usage_after - mem_usage_before} MiB")
