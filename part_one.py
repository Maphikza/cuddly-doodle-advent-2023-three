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


# import re

# with open("engine_scheme_test.txt", "r") as file:
#     engine_schema_list = file.read().split("\n")

# # print(len(engine_schema_list))

# possible_symbols = "!#$%&()*+,-/:;<=>?@[\\]^_`{|}~"

# def check_top(full_engine_list: list, parts_line: int, line_number: int, num_start_index: int, num_end_index: int) -> bool:
#     # print(f"{parts_line} - Top")
#     if num_start_index == 0:
#         if any(i in possible_symbols for i in full_engine_list[line_number-1][num_start_index:num_end_index+2]):
#             print(f"{parts_line} top is: {full_engine_list[line_number-1][num_start_index:num_end_index+2]}")
#             return True
#     elif num_start_index > 0 and num_end_index != len(parts_line)-1:
#         if any(i in possible_symbols for i in full_engine_list[line_number-1][num_start_index-1:num_end_index+2]):
#             print(f"{parts_line} top is: {full_engine_list[line_number-1][num_start_index-1:num_end_index+2]}")
#             return True
#     else:
#         if any(i in possible_symbols for i in full_engine_list[line_number-1][num_start_index-1:num_end_index+1]):
#             print(f"{parts_line} top is: {full_engine_list[line_number-1][num_start_index-1:num_end_index+1]}")
#             return True
        
# def check_current_line(parts_line: int, num_start_index: int, num_end_index: int) -> bool:
#     if num_start_index == 0:
#         if parts_line[num_end_index+1] in possible_symbols:
#             print(f"{parts_line} next in line : {parts_line[num_end_index+1]}")
#             return True
#     elif num_start_index > 0 and num_end_index != len(parts_line)-1:
#         if parts_line[num_start_index-1] in possible_symbols or parts_line[num_end_index+1] in possible_symbols:
#             print(f"{parts_line} before : {parts_line[num_start_index-1]} after: {parts_line[num_end_index+1]}")
#             return True
#     else:
#         if parts_line[num_start_index-1] in possible_symbols:
#             print(f"{parts_line} before: {parts_line[num_start_index-1]}")
#             return True
        
# def check_bottom(full_engine_list: list, parts_line: int, line_number: int, num_start_index: int, num_end_index: int) -> bool:
#     print(full_engine_list[line_number+1][num_start_index:num_end_index+2])
#     if num_start_index == 0:
#         if any(i in possible_symbols for i in full_engine_list[line_number+1][num_start_index:num_end_index+2]):
#             print(f"{parts_line} - bottom {full_engine_list[line_number+1][num_start_index:num_end_index+2]}")
#             return True
#         elif num_start_index > 0 and num_end_index != len(parts_line)-1:
#             if any(i in possible_symbols for i in full_engine_list[line_number+1][num_start_index-1:num_end_index+2]):
#                 print(f"{parts_line} - bottom {full_engine_list[line_number+1][num_start_index-1:num_end_index+2]}")
#                 return True
#         else:
#             if any(i in possible_symbols for i in full_engine_list[line_number+1][num_start_index-1:num_end_index+1]):
#                 print(f"{parts_line} - bottom {full_engine_list[line_number+1][num_start_index-1:num_end_index+1]}")
#                 return True

# total = 0

# for line, parts in enumerate(engine_schema_list):
#     # print(parts)
#     # print(parts[len(parts)-1])
#     print(f"The line is: {line}")
#     matches = re.finditer(r'\d+', parts)

#     for match in matches:
#         unit = match.group()
#         unit_start = match.start()
#         unit_end = match.end() -1
#         # print(f"Number unit: {unit}, Index span: ({unit_start}, {unit_end})")
#         # print(unit_end == len(parts))
#         if line == 0:
#             current_line = check_current_line(parts, unit_start, unit_end)
#             bottom_line = check_bottom(engine_schema_list, parts, line, unit_start, unit_end)
#             if current_line or bottom_line:
#                 total += int(unit)
#                 print(f"unit: {unit} is a part.")
            
#         elif line > 0 and line != len(engine_schema_list)-1:
#             top_line = check_top(engine_schema_list, parts, line, unit_start, unit_end)
#             current_line = check_current_line(parts, unit_start, unit_end)
#             bottom_line = check_bottom(engine_schema_list, parts, line, unit_start, unit_end)
#             if top_line or current_line or bottom_line:
#                 total += int(unit)
#                 print(f"unit: {unit} is a part.")
#         else:
#             top_line = check_top(engine_schema_list, parts, line, unit_start, unit_end)
#             current_line = check_current_line(parts, unit_start, unit_end)
#             if top_line or current_line:
#                 total += int(unit)
#                 print(f"unit: {unit} is a part.")
        

# print(total)

                
        
                    


    


# print(engine_schema_list)
# print(len(engine_schema_list[0]))
# for line, parts in enumerate(engine_schema_list):
#     symbol_found = None 
#     index_list = [] 
#     line_number = 0
#     for symbol in possible_symbols:
#         if symbol in parts:
#             symbol_index = parts.index(symbol)
#             print(symbol_index)
#             symbol_found = True 
#             index_list.append(symbol_index) 
#             line_number = line
#     if symbol_found:
#         print(f"Symbol Indexes: {index_list}, line number: {line_number}")
#     else:
#         print("Line has no symbols.")
        