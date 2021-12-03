from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def __init__(self):
        pass

    def solve_part_1(self, input = None):
        """
        Given a list of string input commands which perform the following:
            - forward X increases the horizontal position by X units.
            - down X increases the depth by X units.
            - up X decreases the depth by X units.

        Calculate the horizontal position *multiplied by* the depth you would have after following the planned course.
        Your horizontal position and depth both start at 0.

        >>> solution.solve_part_1(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"])
        150
        """
        if not input:
          input = self._data

        depth, horizontal = 0, 0

        for command in input:
            if "forward" in command:
                distance = int(command.replace("forward", "").strip())
                horizontal += distance
            elif "down" in command:
                distance = int(command.replace("down", "").strip())
                depth += distance
            elif "up" in command:
                distance = int(command.replace("up", "").strip())
                depth -= distance

        return depth * horizontal


    def solve_part_2(self, input = None):
        """
        Given a list of string input commands which perform the following:
            - "down X" increases your aim by X units.
            - "up X" decreases your aim by X units.
            - "forward X" does two things:
                - It increases your horizontal position by X units.
                - It increases your depth by your aim multiplied by X.

        Calculate the horizontal position *multiplied by* the depth you would have after following the planned course.
        Your horizontal position, aim, and depth all start at 0.

        >>> solution.solve_part_2(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"])
        900
        """
        if not input:
            input = self._data

        depth, aim, horizontal = 0, 0, 0

        for command in input:
            if "forward" in command:
                distance = int(command.replace("forward", "").strip())
                horizontal += distance
                depth += (distance * aim)
            elif "down" in command:
                distance = int(command.replace("down", "").strip())
                aim += distance
            elif "up" in command:
                distance = int(command.replace("up", "").strip())
                aim -= distance

        return depth * horizontal


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'solution': Solution()})

    solution = Solution()
    solution.read_input("input_02.txt", "string")
    solution.print_answers(2, 2102357, 2101031224)