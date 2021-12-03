from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def __init__(self):
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'solution': Solution()})

    solution = Solution()
    solution.read_input("input_03.txt", "integer")
    solution.print_answers(3, None, None)