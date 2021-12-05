from typing import DefaultDict, Tuple
from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def process_input(self, a:list = [str]):
        if not a:
            a = self._data

        pairs_straight = []
        pairs_diagonal = []

        for i in range(len(a)):
            nums = a[i].replace(" -> ", ",").split(",")
            if nums[0] == nums[2] or nums[1] == nums[3]:
                pairs_straight.append([[nums[0],nums[1]],[nums[2],nums[3]]])
            else:
                pairs_diagonal.append([[nums[0],nums[1]],[nums[2],nums[3]]])

        return pairs_straight, pairs_diagonal

    def count_overlaps(self, counts):
        overlaps = 0
        for key, value in counts.items():
            if value >= 2:
                overlaps +=1

        return overlaps

    def process_straight_lines(self, input):
        counts = DefaultDict(int)

        for pair in input:
            x1, y1 = int(pair[0][0]), int(pair[0][1])
            x2, y2 = int(pair[1][0]), int(pair[1][1])

            counts[f'{x1},{y1}'] += 1

            if x1 == x2:
                while y1 != y2:
                    y1 = y1 + 1 if y1 < y2 else y1 - 1
                    counts[f'{x1},{y1}'] += 1
            elif y1 == y2:
                while x1 != x2:
                    x1 = x1 + 1 if x1 < x2 else x1 - 1
                    counts[f'{x1},{y1}'] += 1

        return counts

    def process_diagonal_lines(self, input):
        counts = DefaultDict(int)

        for pair in input:
            x1, y1 = int(pair[0][0]), int(pair[0][1])
            x2, y2 = int(pair[1][0]), int(pair[1][1])

            if x1 < x2 and y1 < y2:
                while x1 <= x2 and y1 <= y2:
                    counts[f'{x1},{y1}'] += 1
                    x1 += 1
                    y1 += 1

            elif x1 < x2 and y2 < y1:
                while x1 <= x2 and y2 <= y1:
                    counts[f'{x1},{y1}'] += 1
                    x1 += 1
                    y1 -= 1

            elif x2 < x1 and y1 < y2:
                while x2 <= x1 and y1 <= y2:
                    counts[f'{x1},{y1}'] += 1
                    x1 -= 1
                    y1 += 1

            elif x2 < x1 and y2 < y1:
                while x2 <= x1 and y2 <= y1:
                    counts[f'{x1},{y1}'] += 1
                    x1 -= 1
                    y1 -= 1

        return counts

    def solve_part_1(self, input = None):
        if not input:
            input = self._data

        straight_lines, diagonal_lines = self.process_input(self._data)
        counts = self.process_straight_lines(straight_lines)
        return self.count_overlaps(counts)

    def solve_part_2(self, input = None):
        if not input:
            input = self._data

        straight_lines, diagonal_lines = self.process_input(self._data)
        counts_straight = self.process_straight_lines(straight_lines)
        counts_diag = self.process_diagonal_lines(diagonal_lines)

        counts = DefaultDict(int)
        for key, value in counts_diag.items():
            counts[key] += value

        for key, value in counts_straight.items():
            counts[key] += value

        return self.count_overlaps(counts)

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'solution': Solution()})

    solution = Solution()
    solution.read_input("input_05.txt", "string")
    solution.print_answers(5, 7085, 20271)
