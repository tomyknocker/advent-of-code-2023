from itertools import zip_longest

with open('./Day4/input', mode='r') as f:
    dataf = f.read()
    data = dataf.splitlines()
    # PART 1
    solution1 = 0
    for data_id,card_data in enumerate(data):
        winning_numbers = set.intersection(*tuple({int(y) for y in x.split()} for x in card_data[9:].split('|')))
        winning_numbers_cnt = len(winning_numbers)
        solution1 += 0 if winning_numbers_cnt == 0 else 2**(winning_numbers_cnt-1)
    
    # PART 2
    solution2 = 0
    additional_cards_to_take = [0]
    for data_id,card_data in enumerate(data):
        if additional_cards_to_take:
            multiply_res = additional_cards_to_take.pop(0)
        else:
            multiply_res=0
        winning_numbers = set.intersection(*tuple({int(y) for y in x.split()} for x in card_data[9:].split('|')))
        winning_numbers_cnt = len(winning_numbers)

        solution2 += 1+multiply_res
        additional_cards_to_take = [sum(n) for n in zip_longest(additional_cards_to_take, [1+multiply_res]*winning_numbers_cnt, fillvalue=0)]


print(f"Solution Part 1: {solution1}")
print(f"Solution Part 2: {solution2}")
