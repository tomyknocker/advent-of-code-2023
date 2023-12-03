
with open('./Day3/input', mode='r') as f:
    dataf = f.read()
    schematic = dataf.splitlines()
    # PART 1
    solution1 = 0

    number_str = ''
    parts_number_list = []
    schematic_size_x = len(schematic[0])-1
    schematic_size_y = len(schematic)-1
    # Get all numbers from schematic and their positions
    for line_no, schema_line in enumerate(schematic):
        line_partnumber_list = []
        for char_no, character in enumerate(schema_line):
            if character.isnumeric():
                if number_str == '':
                    number_str = character
                    num_start = char_no
                else:
                    number_str += character
            else:   
                if number_str != '':
                    num_end = char_no-1
                    line_partnumber_list.append((int(number_str),num_start,num_end))
                    number_str = ''

            if char_no == schematic_size_x:
                if number_str != '':
                    num_end = char_no
                    line_partnumber_list.append((int(number_str),num_start,num_end))
                    number_str = ''  

        parts_number_list.append(line_partnumber_list)
        # print (schema_line)
        # print(parts_number_list[line_no])

    # check if number is adjectent to part (symbol char in chematic file)

    for line_no, part_num_line in enumerate(parts_number_list):
        # dealing with 1st and last line of schematic
        if line_no == 0:
            lines_to_check = {0,1}  
        elif line_no == schematic_size_y:
            lines_to_check = {line_no, line_no-1}
        else:            
            lines_to_check = {line_no, line_no-1, line_no+1}

        for part in part_num_line:
            start_pos = part[1]-1 if part[1] > 0 else 0
            end_pos = part[2]+2 if part[2] < schematic_size_x else part[2]+1
            surround = ''.join((schematic[line][start_pos:end_pos] for line in lines_to_check))
            if any(not(x.isnumeric() or x == '.') for x in surround):
                solution1 = solution1 + part[0]
            #     print (f"FOUND {line_no=} {part=} {surround=}")
            # else:
            #     print (f"NOT   {line_no=} {part=} {surround=}")

    # PART 2
    solution2 = 0
    #  get all gears
    gear_list = []
    for line_no, schema_line in enumerate(schematic):
        if line_no == 0:
            lines_to_check = [0,1]  
        elif line_no == schematic_size_y:
            lines_to_check = [line_no-1, line_no]
        else:            
            lines_to_check = [line_no-1, line_no, line_no+1] 

        for char_no, character in enumerate(schema_line):
            if character == '*':
                gear_numbers=[]
                for part in [item for sublist in parts_number_list[lines_to_check[0]:lines_to_check[-1]+1] for item in sublist]:
                    if (part[1]-1) <= char_no <= (part[2]+1):
                        # print (f'Gear:{line_no=}-{char_no=} - {part=}')
                        gear_numbers.append(part[0])

                if len(gear_numbers)==2:
                    solution2 = solution2 + gear_numbers[0]*gear_numbers[1]




print(f"Solution Part 1: {solution1}")
print(f"Solution Part 2: {solution2}")
