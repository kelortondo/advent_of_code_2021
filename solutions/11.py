from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def __init__(self):
        pass

    def solve_part_1(self):
        data = self._data
        octopi = []
        for line in data:
            octopi.append([int(x) for x in line])

        rows = len(data)
        cols = len(data[0])

        def increment_by_one(data):
            for r in range(rows):
                for c in range(cols):
                    data[r][c] += 1

            return data

        def flash(data):
            flashes = [0]

            def handle_flash(row, col):
                data[row][col] = float("-inf")
                flashes[0] += 1
                directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
                for move in directions:
                    new_row = row + move[0]
                    new_col = col + move[1]
                    if new_row in range(rows) and new_col in range(cols):
                        data[new_row][new_col] += 1
                        if data[new_row][new_col] > 9:
                            handle_flash(new_row, new_col)

            for r in range(rows):
                for c in range(cols):
                    if data[r][c] > 9:
                        handle_flash(r, c)

            return flashes[0]

        def set_zero(data):
            for r in range(rows):
                for c in range(cols):
                    if data[r][c] < 0:
                        data[r][c] = 0

        steps = 100
        total_flashes = 0
        for _ in range(0, steps):
            octopi = increment_by_one(octopi)
            total_flashes += flash(octopi)
            set_zero(octopi)

        return total_flashes

    def solve_part_2(self):
        data = self._data
        octopi = []
        for line in data:
            octopi.append([int(x) for x in line])

        rows = len(data)
        cols = len(data[0])

        def increment_by_one(data):
            for r in range(rows):
                for c in range(cols):
                    data[r][c] += 1

            return data

        def flash(data):
            flashes = [0]

            def handle_flash(row, col):
                data[row][col] = float("-inf")
                flashes[0] += 1
                directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
                for move in directions:
                    new_row = row + move[0]
                    new_col = col + move[1]
                    if new_row in range(rows) and new_col in range(cols):
                        data[new_row][new_col] += 1
                        if data[new_row][new_col] > 9:
                            handle_flash(new_row, new_col)

            for r in range(rows):
                for c in range(cols):
                    if data[r][c] > 9:
                        handle_flash(r, c)

            return flashes[0]

        def set_zero(data):
            for r in range(rows):
                for c in range(cols):
                    if data[r][c] < 0:
                        data[r][c] = 0
        step = 1
        while True:
            octopi = increment_by_one(octopi)
            num_flashes = flash(octopi)
            if num_flashes == rows * cols:
                return step
            set_zero(octopi)
            step += 1


if __name__ == "__main__":
    solution = Solution()
    solution.read_input("input11.txt", "string")
    solution.print_answers(11, 1725, 308)
