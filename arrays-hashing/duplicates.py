class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# use timeit to measure the time
import timeit

print(
    timeit.timeit(
        "Solution().containsDuplicate([1,2,3,4,5,6,7,8,9,10])",
        setup="from __main__ import Solution",
        number=100000,
    )
)

# check the memory usage
import tracemalloc

tracemalloc.start()
Solution().containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
