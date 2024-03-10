import time
from memory_profiler import memory_usage


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True


sol = Solution()

s = "anagram"
t = "nagaram"

start_time = time.time()
start_mem = memory_usage()[0]

result = sol.isAnagram(s, t)

end_time = time.time()
end_mem = memory_usage()[0]

time_taken = end_time - start_time
mem_used = end_mem - start_mem

print(f"Time taken: {time_taken} seconds")
print(f"Memory used: {mem_used} MiB")
