
with open('./Day2/input', mode='r') as f:
    dataf = f.read()
    data = dataf.splitlines()
    # PART 1
    # What is the sum of the IDs of feasible games with only 12 red cubes, 13 green cubes, and 14 blue cubes?
    # DATA:  Game 1: 1 red, 5 blue, 1 green; 16 blue, 3 red; 6 blue, 5 red; 4 red, 7 blue, 1 green

    max_cubes = {'red': 12, 'blue': 14, 'green': 13}
    solution1 = 0
    solution2 = 0
    for game in data:
        game_id, cube_sets = tuple(game.split(':'))
        game_id = int(game_id.split()[1])
        #  list of game sets, each set is a dict with color:cube_count
        gamesets =[{ccol:int(ccnt) for (ccnt,ccol) in [cubes1color.strip().split(' ') for cubes1color in cubeset.strip().split(',')]}
                    for cubeset in cube_sets.split(';')]
        # print(gamesets)
        #find for each color if max cube count exceeds cube count in gameset or does not exist in game set (cubes of this color were not preset)
        def find_if_cubes_cnt_possible(max_cubes, gameset) -> bool:
            possible = True
            for max_cube in max_cubes.items():
                possible &= max_cube[1] >= gameset.get(max_cube[0]) if max_cube[0] in gameset.keys() else True
            return possible
        
        #  If all game sets are possible, add game id to solution 
        if all(find_if_cubes_cnt_possible(max_cubes, gameset) for gameset in gamesets):
            solution1 = solution1 + game_id

        # PART 2
        #  what is the fewest number of cubes of each color that could have been in the bag to make the game possible
        game_power=1
        for color in max_cubes.keys():
            color_power = max([gameset.get(color,1) for gameset in gamesets])
            # print (f'{color=} {color_power=}')
            game_power = game_power * color_power

        solution2 =solution2 + game_power


print(f"Solution Part 1: {solution1}")
print(f"Solution Part 2: {solution2}")
