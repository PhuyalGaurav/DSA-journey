import time
from memory_profiler import memory_usage


class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


sol = Solution()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start_time = time.time()
start_mem = memory_usage()[0]

result = sol.containsDuplicate(nums)

end_time = time.time()
end_mem = memory_usage()[0]

time_taken = end_time - start_time
mem_used = end_mem - start_mem

print(f"Time taken: {time_taken} seconds")
print(f"Memory used: {mem_used} MiB")
