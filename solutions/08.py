from AoCInputReader import AoCInputReader

class Solution(AoCInputReader):
    def __init__(self):
        pass

    def solve_part_1(self):
        data = []
        for line in self._data:
            parts = line.split(" | ")
            patterns = parts[0].split(" ")
            output = parts[1].split(" ")
            data.append([patterns, output])
        count = 0

        for entry in data:
            mappings = {}
            total_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
            nums = [None] * 10
            length_five = []

            for num in entry[0]:
                if len(num) == 2:
                    nums[1] = set(num)
                elif len(num) == 3:
                    nums[7] = set(num)
                elif len(num) == 4:
                    nums[4] = set(num)
                elif len(num) == 5:
                    length_five.append(set(num))
                elif len(num) == 7:
                    nums[8] = set(num)

            mappings["top"] = nums[7] - nums[1]
            mappings["middle"] = set.intersection(length_five[0], length_five[1], length_five[2], nums[4])
            mappings["top_left"] = nums[4] - nums[1] - mappings["middle"]
            mappings["bottom"] = set.intersection(length_five[0], length_five[1], length_five[2]) - mappings["top"] - mappings["middle"]

            for num in length_five:
                num = num - mappings["bottom"] - mappings["top"] - mappings["middle"] - mappings["top_left"]
                if len(num) == 1:
                    mappings["bottom_right"] = num

            mappings["top_right"] = nums[1] - mappings["bottom_right"]

            mappings["bottom_left"] = nums[8]
            for key in mappings:
                if key == "bottom_left":
                    continue
                mappings["bottom_left"] = mappings["bottom_left"] - mappings[key]

            mappings_to_num = {
                0: total_set - mappings["middle"],
                1: mappings["top_right"].union(mappings["bottom_right"]),
                2: total_set - mappings["top_left"] - mappings["bottom_right"],
                3: total_set - mappings["top_left"] - mappings["bottom_left"],
                4: total_set - mappings["top"] - mappings["bottom"] - mappings["bottom_left"],
                5: total_set - mappings["top_right"] - mappings["bottom_left"],
                6: total_set - mappings["top_right"],
                7: total_set - mappings["top_left"] - mappings["bottom_left"] - mappings["middle"] - mappings["bottom"],
                8: total_set,
                9: total_set - mappings["bottom_left"]
            }


            for num in entry[1]:
                num_set = set(num)
                for entry, letter_set in mappings_to_num.items():
                    if num_set == letter_set and entry in [1, 4, 7, 8]:
                        count += 1

        return count

    def solve_part_2(self):
        data = []
        for line in self._data:
            parts = line.split(" | ")
            patterns = parts[0].split(" ")
            output = parts[1].split(" ")
            data.append([patterns, output])
        count = 0

        for entry in data:
            mappings = {}
            total_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
            nums = [None] * 10
            length_five = []

            for num in entry[0]:
                if len(num) == 2:
                    nums[1] = set(num)
                elif len(num) == 3:
                    nums[7] = set(num)
                elif len(num) == 4:
                    nums[4] = set(num)
                elif len(num) == 5:
                    length_five.append(set(num))
                elif len(num) == 7:
                    nums[8] = set(num)

            mappings["top"] = nums[7] - nums[1]
            mappings["middle"] = set.intersection(length_five[0], length_five[1], length_five[2], nums[4])
            mappings["top_left"] = nums[4] - nums[1] - mappings["middle"]
            mappings["bottom"] = set.intersection(length_five[0], length_five[1], length_five[2]) - mappings["top"] - mappings["middle"]

            for num in length_five:
                num = num - mappings["bottom"] - mappings["top"] - mappings["middle"] - mappings["top_left"]
                if len(num) == 1:
                    mappings["bottom_right"] = num

            mappings["top_right"] = nums[1] - mappings["bottom_right"]

            mappings["bottom_left"] = nums[8]
            for key in mappings:
                if key == "bottom_left":
                    continue
                mappings["bottom_left"] = mappings["bottom_left"] - mappings[key]

            mappings_to_num = {
                0: total_set - mappings["middle"],
                1: mappings["top_right"].union(mappings["bottom_right"]),
                2: total_set - mappings["top_left"] - mappings["bottom_right"],
                3: total_set - mappings["top_left"] - mappings["bottom_left"],
                4: total_set - mappings["top"] - mappings["bottom"] - mappings["bottom_left"],
                5: total_set - mappings["top_right"] - mappings["bottom_left"],
                6: total_set - mappings["top_right"],
                7: total_set - mappings["top_left"] - mappings["bottom_left"] - mappings["middle"] - mappings["bottom"],
                8: total_set,
                9: total_set - mappings["bottom_left"]
            }

            string_number = ""
            for num in entry[1]:
                num_set = set(num)
                for entry, letter_set in mappings_to_num.items():
                    if num_set == letter_set:
                        string_number += str(entry)


            count += int(string_number)

        return count


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'solution': Solution()})

    solution = Solution()
    solution.read_input("input_08.txt", "string")
    solution.print_answers(8, 421, 986163)
