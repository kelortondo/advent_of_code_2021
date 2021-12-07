from AoCInputReader import AoCInputReader
from collections import defaultdict
class Solution(AoCInputReader):
    def __init__(self, data = None):
        if data:
            self._data = data

    def solve_part_1(self, fishies = None):
        """
        Given a list of integer depths, count the number of times a depth measurement
        increases from the previous measurement.

        >>> solution.solve_part_1([3,4,3,1,2])
        5934
        """
        if not fishies:
          fishies = self._data

        end_day = 80
        start_day = 1
        counts = defaultdict(int)

        for fish in fishies:
            counts[fish] += 1

        for day in range(start_day, end_day + 1):
            counts[9] = counts[0]
            counts[7] += counts[0]
            for i in range(1, 10):
                counts[i-1] = counts[i]
            counts[9] = 0

        total = 0
        for value in counts.values():
            total += value
        return total


    def solve_part_2(self, fishies = None):
        """
        Given a list of integer depths, count the number of times a depth measurement
        increases from the previous measurement.

        >>> solution.solve_part_2([3,4,3,1,2])
        26984457539
        """
        if not fishies:
          fishies = self._data

        end_day = 256
        start_day = 1
        counts = defaultdict(int)

        for fish in fishies:
            counts[fish] += 1

        for day in range(start_day, end_day + 1):
            counts[9] = counts[0]
            counts[7] += counts[0]
            for i in range(1, 10):
                counts[i-1] = counts[i]
            counts[9] = 0

        total = 0
        for value in counts.values():
            total += value
        return total


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'solution': Solution()})
    test_data = [1,2,4,5,5,5,2,1,3,1,4,3,2,1,5,5,1,2,3,4,4,1,2,3,2,1,4,4,1,5,5,1,3,4,4,4,1,2,2,5,1,5,5,3,2,3,1,1,3,5,1,1,2,4,2,3,1,1,2,1,3,1,2,1,1,2,1,2,2,1,1,1,1,5,4,5,2,1,3,2,4,1,1,3,4,1,4,1,5,1,4,1,5,3,2,3,2,2,4,4,3,3,4,3,4,4,3,4,5,1,2,5,2,1,5,5,1,3,4,2,2,4,2,2,1,3,2,5,5,1,3,3,4,3,5,3,5,5,4,5,1,1,4,1,4,5,1,1,1,4,1,1,4,2,1,4,1,3,4,4,3,1,2,2,4,3,3,2,2,2,3,5,5,2,3,1,5,1,1,1,1,3,1,4,1,4,1,2,5,3,2,4,4,1,3,1,1,1,3,4,4,1,1,2,1,4,3,4,2,2,3,2,4,3,1,5,1,3,1,4,5,5,3,5,1,3,5,5,4,2,3,2,4,1,3,2,2,2,1,3,4,2,5,2,5,3,5,5,1,1,1,2,2,3,1,4,4,4,5,4,5,5,1,4,5,5,4,1,1,5,3,3,1,4,1,3,1,1,4,1,5,2,3,2,3,1,2,2,2,1,1,5,1,4,5,2,4,2,2,3]
    solution = Solution(test_data)
    solution.print_answers(6, 352872, 1604361182149)
