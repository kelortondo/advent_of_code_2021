class AoCInputReader():
    """
    Base class for implementing Advent of Code solutions. Includes methods for
    loading a text file into a python list, and printing solutions.
    """

    def solve_part_1(self):
        print("You haven't implemented the solution for part 1 yet.")
        return None

    def solve_part_2(self):
        print("You haven't implemented the solution for part 2 yet.")
        return None

    def read_input(self, file_name:str, data_type:str):
        """
        Takes a file name (located at root/input) and reads it into a list
        of <data_type>s and sets it equal to self._data

        Args:
            - file_name: a string representing the file name to be read
            - data_type: one of "integer" or "string"
        """
        data_type_options = ["integer", "string"]

        if type(data_type) is not str:
            msg = f"data_type is a {type(data_type)}, expected {type('')}"
            raise TypeError(msg)

        if data_type not in data_type_options:
            msg = f"Wrong data type option ('{data_type}'). Valid options include 'integer' and 'string'"
            raise ValueError(msg)

        with open(f"./input/{file_name}") as file:
            lines = file.readlines()

        if data_type == "integer":
            self._data = [int(line.rstrip()) for line in lines]
        elif data_type == "string":
            self._data = [line.rstrip() for line in lines]

        print(f"Loaded {len(self._data)} lines of type {type(self._data[0])} into self._data")

    def print_answers(self, day:int, p1_answer, p2_answer):
        """
        Args:
            - day (int): the # day of the challenge e.g. 1
            - p1_answer: the expected answer for part 1
            - p2_answer: the expected answer for part 2
        """
        answer_1 = self.solve_part_1()
        answer_2 = self.solve_part_2()
        print(f"~ Day {day} Solutions ~")
        print(f"Your part 1 solution ({answer_1}) is {'correct!' if answer_1 == p1_answer else 'incorrect.'}")
        print(f"Your part 2 solution ({answer_2}) is {'correct!' if answer_2 == p2_answer else 'incorrect.'}")