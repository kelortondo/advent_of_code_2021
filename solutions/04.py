from typing import Tuple
from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def process_input(self, a:list = []) -> Tuple[list[str], list[list[list[str]]]]:
        """
        Processes the list (a) formed by reading the AoC day 4 input text file to output a list of called Bingo
        numbers and a list of 5 x 5 matrices (boards)

        >>> solution.process_input(['1,2,3,4,5,6,7', '', ' 3 82 68 26 93', '61 90 29 69 92', '60 94 99  6 83', '77 80  2 58 55', '59 65 95 38 62', ''])
        (['1', '2', '3', '4', '5', '6', '7'], [[['3', '82', '68', '26', '93'], ['61', '90', '29', '69', '92'], ['60', '94', '99', '6', '83'], ['77', '80', '2', '58', '55'], ['59', '65', '95', '38', '62']]])
        """

        if not a:
            a = self._data

        nums = a[0].split(",")
        boards = []
        board = []
        for i in range(2, len(a)):
            if len(a[i]) == 0:
                boards.append(board)
                board = []
            else:
                row = a[i].strip().replace("  ", " ").split(" ")
                for item in row:
                    item = item.strip()
                board.append(row)

        return nums, boards

    def update_board(self, board:list[list[str]], num:str) -> list[list[str]]:
        """
        Given a bingo board and a number, search for that number on the board. If found, replace it with '-1'. Return the board.

        >>> solution.update_board([['-1', '-1', '-1', '-1', '6'], ['10', '16', '15', '-1', '19'], ['18', '8', '-1', '26', '20'], ['22', '-1', '13', '6', '-1'], ['-1', '-1', '12', '3', '-1']], '6')
        [['-1', '-1', '-1', '-1', '-1'], ['10', '16', '15', '-1', '19'], ['18', '8', '-1', '26', '20'], ['22', '-1', '13', '-1', '-1'], ['-1', '-1', '12', '3', '-1']]
        """

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == num:
                    board[row][col] = '-1'
        return board

    def check_row(self, row):
        """
        Given a list of strings representing a bingo row, check if all items in the column are
        equal to '-1'. If so, return True. Otherwise, return false.

        >>> solution.check_row(['0', '-1', '1', '-1', '-1'])
        False

        >>> solution.check_row(['-1', '-1', '-1', '-1', '-1'])
        True
        """

        for col in range(len(row)):
            if row[col] != '-1':
                return False
        return True

    def check_column(self, column:list[str]) -> bool:
        """
        Given a list of strings representing a bingo column, check if all items in the column are
        equal to '-1'. If so, return True. Otherwise, return false.

        >>> solution.check_column(['0', '-1', '1', '-1', '-1'])
        False

        >>> solution.check_column(['-1', '-1', '-1', '-1', '-1'])
        True
        """

        for row in range(len(column)):
            if column[row] != '-1':
                return False
        return True

    def validate_board(self, board:list[list[str]]) -> bool:
        """
        Given a bingo board, check if it has won by checking off all numbers in a row or column.
        A number being checked off is indicated by it having a value of '-1'

        >>> solution.validate_board([['0', '-1', '1', '-1', '-1'], ['0', '0', '1', '-1', '-1'], ['0', '-1', '1', '1', '-1'], ['0', '-1', '1', '-1', '1'], ['0', '-1', '1', '-1', '-1']])
        False

        >>> solution.validate_board([['0', '-1', '1', '-1', '-1'], ['0', '1', '1', '1', '1'], ['0', '1', '1', '-1', '-1'], ['0', '-1', '1', '-1', '1'], ['-1', '-1', '-1', '-1', '-1']])
        True

        >>> solution.validate_board([['0', '-1', '1', '1', '1'], ['0', '-1', '1', '-1', '-1'], ['0', '-1', '1', '-1', '-1'], ['0', '-1', '1', '-1', '-1'], ['1', '-1', '-1', '1', '-1']])
        True
        """

        for row in board:
            if self.check_row(row):
                return True

        for col in range(len(board[0])):
            column = [board[i][col] for i in range(len(board))]
            if self.check_column(column):
                return True

        return False

    def score_board(self, board: list[list[str]], last_num:str) -> int:
        """
        Score is calculated by finding the sum of all unmarked numbers on a board.
        Then, multiply that sum by the number that was just called when the board won.

        >>> solution.score_board([['-1', '-1', '-1', '-1',  '-1'], ['10', '16', '15', '-1', '19'], ['18', '8', '-1', '26', '20'], ['22', '-1', '13', '6', '-1'], ['-1', '-1', '12', '3', '-1']], 24)
        4512
        """

        total_sum = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '-1':
                    total_sum += int(board[row][col])
        return total_sum * int(last_num)

    def solve_part_1(self, input = None):
        """
        Given a list of bingo numbers to be called and a list of 5x5 boards (matrices), find which board will
        win first and calculate its score.
        """

        if not input:
            input = self._data

        nums, boards = self.process_input(input)
        for num in nums:
            for board in boards:
                board = self.update_board(board, num)
                winner = self.validate_board(board)
                if winner:
                    return self.score_board(board, num)

    def solve_part_2(self, input = None):
        """
        Given a list of bingo numbers to be called and a list of 5x5 boards (matrices), find which board will
        win last and calculate its score.
        """

        if not input:
            input = self._data

        nums, boards = self.process_input(input)
        for num in nums:
            losers = []
            for b in range(len(boards)):
                board = self.update_board(boards[b], num)
                is_winner = self.validate_board(board)
                if is_winner:
                    if len(boards) == 1:
                        return self.score_board(board, num)
                    else:
                        last_winner = self.score_board(board, num)
                else:
                    losers.append(board)

            boards = losers.copy()

        return last_winner



if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'solution': Solution()})

    solution = Solution()
    solution.read_input("input_04.txt", "string")
    solution.print_answers(4, 27027, 36975)
