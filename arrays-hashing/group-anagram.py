import time
from memory_profiler import memory_usage


class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            sorted_tuple = tuple(sorted(s))
            if sorted_tuple in groups:
                groups[sorted_tuple].append(s)
            else:
                groups[sorted_tuple] = [s]
        return list(groups.values())


sol = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

start_time = time.time()
start_mem = memory_usage()[0]

result = sol.groupAnagrams(strs)

end_time = time.time()
end_mem = memory_usage()[0]

time_taken = end_time - start_time
mem_used = end_mem - start_mem

print(f"Time taken: {time_taken} seconds")
print(f"Memory used: {mem_used} MiB")
