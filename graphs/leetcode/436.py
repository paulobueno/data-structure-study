from typing import List


class Solution:

    @staticmethod
    def bisect_right(elements, target):
        lo = 0
        hi = len(elements)
        while lo < hi:
            mid = (lo + hi) // 2
            if target > elements[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    @staticmethod
    def bisect_right_invert(elements, target):
        lo = 0
        hi = len(elements)
        while lo < hi:
            mid = (lo + hi) // 2
            if target < elements[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def output_for_sorted(self, intervals):
        output = []
        size = len(intervals)
        start_elements = [x[0] for x in intervals]

        if size <= 1:
            if intervals[0][0] == intervals[0][1]:
                return [0]
            else:
                return [-1]

        if start_elements[0] < start_elements[1]:
            bisect = self.bisect_right
        else:
            bisect = self.bisect_right_invert

        for i, interval in enumerate(intervals):
            target = interval[1]
            index = bisect(start_elements, target)
            if index == size:
                output.append(-1)
            elif index == 0 and target != intervals[index][0]:
                output.append(-1)
            else:
                output.append(index)
        return output

    def output_small_list_size(self, intervals):
        output = []
        sorted_by_start_intervals = sorted(intervals, key=lambda x: x[0])
        indexes = self.output_for_sorted(sorted_by_start_intervals)
        for interval in intervals:
            for i, sorted_interval in enumerate(sorted_by_start_intervals):
                if interval == sorted_interval:
                    if indexes[i] == -1:
                        output.append(-1)
                    else:
                        search_for = sorted_by_start_intervals[indexes[i]]
                        index = [i for i, el in enumerate(intervals) if el == search_for][0]
                        output.append(index)
        return output

    def find_right_interval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) < 100:
            return self.output_small_list_size(intervals)
        else:
            return self.output_for_sorted(intervals)
