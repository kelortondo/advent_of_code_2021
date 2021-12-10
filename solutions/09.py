from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def __init__(self):
        pass

    def solve_part_1(self):
        data = []
        for line in self._data:
            line = [int(x) for x in line]
            data.append(line)
        lows = 0

        for row in range(0, len(data)):
            for col in range(0, len(data[1])):
                neighbors = [
                    data[row][col] < data[row + 1][col] if row+1 in range(len(data)) else True,
                    data[row][col] < data[row - 1][col] if row-1 in range(len(data)) else True,
                    data[row][col] < data[row][col + 1] if col+1 in range(len(data)) else True,
                    data[row][col] < data[row][col - 1] if col-1 in range(len(data)) else True
                ]
                if all(neighbors):
                    lows += data[row][col] + 1

        return lows


    def solve_part_2(self):
        data = []
        for line in self._data:
            line = [int(x) for x in line]
            data.append(line)

        basins = []
        rows, cols = len(data), len(data[0])

        def bfs(row, col):
            queue = []
            queue.append((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while queue:
                r, c = queue.pop(0)
                data[r][c] = 9
                self.basin_size += 1

                for move in directions:
                    r_new = r + move[0]
                    c_new = c + move[1]

                    if r_new in range(rows) and c_new in range(cols):
                        if data[r_new][c_new] < 9:
                            queue.append((r_new, c_new))
                            data[r_new][c_new] = 9

        for r in range(rows):
            for c in range(cols):
                if data[r][c] < 9:
                    self.basin_size = 0
                    bfs(r, c)
                    basins.append(self.basin_size)

        basins.sort()
        return basins[-1] * basins[-2] * basins[-3]


if __name__ == "__main__":
    solution = Solution()
    solution.read_input("input09.txt", "string")
    solution.print_answers(9, 502, 1330560)
