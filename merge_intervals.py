class Solution:
    def check_overlap(self, arr1, arr2):
        if arr2[0] <= arr1[1]:
            return True
        return False

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        result = []
        result.append(intervals[0])
        # new_intervals = intervals[1:]
        for interval in intervals[1:]:
            current_start, current_stop = interval
            if current_start <= result[-1][1]:
                new_arr = [result[-1][0], max(current_stop, result[-1][1])] # for (i, j) get the max of prev_j and current_i
                result[-1] = new_arr # replace the new interval with the previous one
            else:
                new_arr = [current_start, current_stop] # otherwise, add the new interval to the results array.
                result.append(new_arr)

        return result
