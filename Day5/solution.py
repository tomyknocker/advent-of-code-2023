
def mymap(x:int, map_data:list)-> int:
    for map_range in map_data:
        if 0 <= (y := x-map_range[1]) < map_range[2]:
            return map_range[0] + y
    else:
        return x
    
    
with open('./Day5/input', mode='r') as f:
    dataf = f.read()
    data = dataf.splitlines()
    # PART 1
    solution1 = 0
    input_list = [int(x) for x in data[0][7:].split()]
    maps = []
    maps.append(map(lambda x: x, input_list))
    map_data = []
    ismap = False
    for line in data:
        if ismap and line:
            map_data.append(tuple([int(x) for x in line.split()]))
        if ismap and not line:
           if map_data:
                # print(input_list, map_data)    
                maps.append(map(lambda x: mymap(x, map_data), maps[-1]))  
                # input_list = list(x)
                # print(input_list)          
        if 'map' in line:
            print(line)
            ismap = True
            map_data = []
        if not line:
            ismap = False
    # print(input_list, map_data) 
    x = map(lambda x: mymap(x, map_data), maps[-1]) 
    # input_list = list(x)
    # print(list(input_list))
    solution1 = min(x)
    print(f"Solution Part 1: {solution1}\n\n")

    # PART 2
    input_list = [int(x) for x in data[0][7:].split()]
    input_ranges = list(zip(input_list[::2],input_list[1::2]))

    input_data = []
    for start_el, el_cnt in input_ranges:
        input_data.extend(list(range(start_el,start_el+el_cnt)))
    input_list=input_data
 
    
    map_data = []
    ismap = False
    for line in data:
        if ismap and line:
            map_data.append(tuple([int(x) for x in line.split()]))
        if ismap and not line:
           if map_data:
                # print(input_list, map_data)    
                x = map(lambda x: mymap(x, map_data), input_list)  
                input_list = list(x)
                # print(input_list)          
        if 'map' in line:
            print(line)
            ismap = True
            map_data = []
        if not line:
            ismap = False
    # print(input_list, map_data) 
    x = map(lambda x: mymap(x, map_data), input_list) 
    # input_list = list(x)
    # print(list(input_list))
    solution2 = min(x)
 




print(f"Solution Part 1: {solution1}")
print(f"Solution Part 2: {solution2}")
