from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def __init__(self):
        pass

    def solve_part_1(self):
        data = self._data

        def isCorrupted(s):
            mappings = {
                '>': '<',
                '}': '{',
                ']': '[',
                ')': '('
            }

            stack = []

            for char in s:
                if char not in mappings:
                    stack.append(char)
                else:
                    top = stack.pop()
                    if top != mappings[char]:
                        return char
        points = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        output = 0
        for line in data:
            illegal_char = isCorrupted(line)
            if illegal_char:
                output += points[illegal_char]

        return output

    def solve_part_2(self):
        data = self._data

        def isCorrupted(s):
            mappings = {
                '>': '<',
                '}': '{',
                ']': '[',
                ')': '('
            }

            stack = []

            for char in s:
                if char not in mappings:
                    stack.append(char)
                else:
                    top = stack.pop()
                    if top != mappings[char]:
                        return True

            return False

        incomplete = []
        for line in data:
            if not isCorrupted(line):
                incomplete.append(line)

        def complete(s):
            mappings = {
                '>': '<',
                '}': '{',
                ']': '[',
                ')': '('
            }

            points = {
                '<': 4,
                '{': 3,
                '[': 2,
                '(': 1
            }

            stack = []

            for char in s:
                if char not in mappings:
                    stack.append(char)
                else:
                    stack.pop()

            stack.reverse()
            score = 0
            for char in stack:
                score = (score * 5) + points[char]
            return score

        scores = []
        for line in incomplete:
            scores.append(complete(line))

        scores.sort()
        return scores[len(scores)//2]



if __name__ == "__main__":
    solution = Solution()
    solution.read_input("input10.txt", "string")
    solution.print_answers(10, 311949, 3042730309)
