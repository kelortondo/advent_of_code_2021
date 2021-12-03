from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def solve_part_1(self, input = None):
        """
        You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate).
        The power consumption can then be found by multiplying the gamma rate by the epsilon rate. Each bit in the gamma rate can be determined by
        finding the most common bit in the corresponding position of all numbers in the diagnostic report. The epsilon rate is calculated in a
        similar way; rather than use the most common bit, the least common bit from each position is used.

        Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.

        >>> solution.solve_part_1(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"])
        198
        """
        if not input:
            input = self._data

        c = len(input[0])
        r = len(input)
        gamma = ""
        epsilon = ""

        for col in range(c):
            zeros = 0
            ones = 0
            for row in range(r):
                if input[row][col] == '0':
                    zeros += 1
                elif input[row][col] == '1':
                    ones += 1
            if zeros > ones:
                gamma += "0"
                epsilon += "1"
            else:
                gamma += "1"
                epsilon += "0"

        return int(gamma, 2) * int(epsilon, 2)

    def solve_part_2(self, input = None):
        """
        Verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

        Start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

            - Keep only numbers selected by the bit criteria for the type of rating value for which you are searching.
            - Discard numbers which do not match the bit criteria.
            - If you only have one number left, stop; this is the rating value for which you are searching.
            - Otherwise, repeat the process, considering the next bit to the right.

        The bit criteria depends on which type of rating value you want to find:
            - To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers
              with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
            - To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers
              with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.

        Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating,
        then multiply them together. What is the life support rating of the submarine?

        >>> solution.solve_part_2(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"])
        230
        """
        if not input:
            input = self._data

        # Find oxygen rating
        oxygen_bits = input.copy()
        for col in range(len(oxygen_bits[0])):
            zeros = 0
            ones = 0
            temp = []
            for row in range(len(oxygen_bits)):
                if oxygen_bits[row][col] == '0':
                    zeros += 1
                elif oxygen_bits[row][col] == '1':
                    ones += 1

            for row_2 in range(len(oxygen_bits)):
                if oxygen_bits[row_2][col] == '0' and zeros > ones:
                    temp.append(oxygen_bits[row_2])
                elif oxygen_bits[row_2][col] == '1' and ones >= zeros:
                    temp.append(oxygen_bits[row_2])

            oxygen_bits = temp.copy()
            if len(oxygen_bits) == 1:
                break

        # Find co2 rating
        co2_bits = input.copy()
        for col in range(len(co2_bits[0])):
            zeros = 0
            ones = 0
            temp = []
            for row in range(len(co2_bits)):
                if co2_bits[row][col] == '0':
                    zeros += 1
                elif co2_bits[row][col] == '1':
                    ones += 1

            for row_2 in range(len(co2_bits)):
                if co2_bits[row_2][col] == '1' and ones < zeros:
                    temp.append(co2_bits[row_2])
                elif co2_bits[row_2][col] == '0' and zeros <= ones:
                    temp.append(co2_bits[row_2])

            co2_bits = temp.copy()
            if len(co2_bits) == 1:
                break

        return int(oxygen_bits[0], 2) * int(co2_bits[0], 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'solution': Solution()})

    solution = Solution()
    solution.read_input("input_03.txt", "string")
    solution.print_answers(3, 4103154, 4245351)