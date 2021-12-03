from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def __init__(self):
        pass

    def solve_part_1(self, input = None):
        """
        Given a list of integer depths, count the number of times a depth measurement
        increases from the previous measurement.

        >>> solution.solve_part_1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
        7
        """
        if not input:
          input = self._data

        l, r = 0, 1
        result = 0

        while r < len(input):
            if input[r] > input[l]:
                result += 1
            l += 1
            r += 1

        return result

    def solve_part_2(self, input = None):
        """
        Given a list of integer depths, count the number of times the sum of 3 measurements
        in a list increases from the previous sum.

        >>> solution.solve_part_2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
        5
        """
        if not input:
          input = self._data

        r = 3
        result = 0
        previous_sum = input[0] + input[1] + input[2]

        while r < len(input):
            current_sum = input[r - 2] + input[r - 1] + input[r]
            if current_sum > previous_sum:
                result += 1
            previous_sum = current_sum
            r += 1

        return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'solution': Solution()})

    solution = Solution()
    solution.read_input("input_01.txt", "integer")
    solution.print_answers(1, 1688, 1728)
