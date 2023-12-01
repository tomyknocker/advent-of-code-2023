with open('./Day1/input', mode='r') as f:
    fdata = f.read()
    data = fdata.splitlines()
    
    # PART 1
    solution1 = 0
    for line in data:
        digits = [x for x in line if x in "0123456789"]
        calval = int(digits[0]+digits[-1])
        solution1 = solution1 + calval

    # PART 2
    solution2 = 0
    digits_map =['0', '1', '2','3', '4', '5', '6', '7', '8', '9', 
                 'zero', 'one', 'two','three', 'four','five','six','seven','eight','nine']
    
    for line in data:
        # print (f'{line=}  ') 
        data_len = len(line)   
        first_digit = (data_len, 0)
        last_digit = (data_len, 0)
        # for each digit (number or letters) find its place from the begining of line and 
        #  from end of line - find reversed digit in reversed line
        for idx,digit in enumerate(digits_map):
            left_idx= line.find(digit)
            right_idx= line[::-1].find(digit[::-1])
            if left_idx >= 0 and left_idx < first_digit[0]:
                first_digit = (left_idx, idx)
            if right_idx >= 0 and right_idx < last_digit[0]:
                last_digit = (right_idx, idx)
            
            # print(f'    {digit}    {lo=} {ro=}    {first_digit=}  {last_digit=} ')
            
        # assemble calibration value having indexes of found digit in digit_map    
        calval = ((first_digit[1] if first_digit[1] < 10 else first_digit[1]-10)*10 + 
                    (last_digit[1] if last_digit[1] < 10 else last_digit[1]-10))
        # print (f' {calval=}')
        solution2 = solution2 + calval

print(f"Solution Part 1: {solution1}")
print(f"Solution Part 2: {solution2}")
