class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from sortedcontainers import SortedList
        table = Counter(nums)
        numbers = [*table.keys()]
        frequency = [*table.values()]
        #print(numbers)
        #print(frequency)
        #print('-'*10)
        #print(table)
        sorted_nums = SortedList()
        for n, f in zip(numbers, frequency):
            sorted_nums.add([f, n])
        # print(sorted_nums)
        # print('--'*20)
        top_freq = sorted_nums[-k:]
        result = sorted([x[1] for x in top_freq])
        # print(result)
        return result