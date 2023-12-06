import re

def extract_full_number(schema, line, index):
    # Move left in the line until a non-digit is found or the line starts
    while index > 0 and schema[line][index - 1].isdigit():
        index -= 1

    # Extract and return the full number starting at the new index
    match = re.match(r'\d+', schema[line][index:])
    return int(match.group()) if match else None

def find_adjacent_numbers(schema, line, index):
    # Check all 8 adjacent positions
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    numbers = set()

    for dy, dx in directions:
        new_line = line + dy
        new_index = index + dx
        if 0 <= new_line < len(schema) and 0 <= new_index < len(schema[new_line]):
            if schema[new_line][new_index].isdigit():
                number = extract_full_number(schema, new_line, new_index)
                numbers.add(number)

    return numbers

def calculate_gear_ratios(schema):
    total_gear_ratio = 0

    for line_num, line in enumerate(schema):
        for index, char in enumerate(line):
            if char == '*':
                adjacent_numbers = find_adjacent_numbers(schema, line_num, index)
                if len(adjacent_numbers) == 2:
                    gear_ratio = 1
                    for number in adjacent_numbers:
                        gear_ratio *= number
                    total_gear_ratio += gear_ratio

    return total_gear_ratio

# Load the engine schematic from a file
with open("engine_scheme.txt", "r") as file:
    engine_schema_list = file.read().split("\n")

# Calculate the total gear ratio sum
total_gear_ratio_sum = calculate_gear_ratios(engine_schema_list)
print(total_gear_ratio_sum)


