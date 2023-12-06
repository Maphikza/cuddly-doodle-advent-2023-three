import re

def is_adjacent_to_symbol(schema, line, index, symbol_set):
    # Check 8 directions: top-left, top, top-right, left, right, bottom-left, bottom, bottom-right
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dy, dx in directions:
        new_line = line + dy
        new_index = index + dx
        if 0 <= new_line < len(schema) and 0 <= new_index < len(schema[new_line]):
            if schema[new_line][new_index] in symbol_set:
                return True
    return False

def calculate_sum_of_parts(schema, symbol_set):
    total = 0
    for line_num, line in enumerate(schema):
        for match in re.finditer(r'\d+', line):
            number = int(match.group())
            start, end = match.span()
            # Check if any part of the number is adjacent to a symbol
            if any(is_adjacent_to_symbol(schema, line_num, i, symbol_set) for i in range(start, end)):
                total += number
    return total

# Load the engine schematic from a file
with open("engine_scheme.txt", "r") as file:
    engine_schema_list = file.read().split("\n")

# Define possible symbols
possible_symbols = set("!#$%&()*+,-/:;<=>?@[\\]^_`{|}~")

# Calculate the total
total = calculate_sum_of_parts(engine_schema_list, possible_symbols)
print(total)
        