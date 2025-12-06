import numpy as np

# warlock hints
# # must be even
# # odd digit id can never be invalid for part 1 rules

file_path = "input.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

def separateIds(lines):
    list_of_id_range = lines.split(",")
    return(list_of_id_range)

def makeSetOfIds(lower_bound, upper_bound):
    id_set = range(lower_bound, upper_bound+1, 1)
    # print(f"this is list of {id_set}")
    # print(f"the length of list is {len(id_set)}")
    # print(f"the first element of list is {id_set[0]}")
    # print(f"the length of first element of list is {len(str(id_set[0]))}")
    # print(f"the datatype is: {type(id_set)}")#
    return(id_set)

def findTheIvalid(range_class):
    if len(str(range_class[0]))%2 == 1 and len(str(range_class[-1]))%2 ==1:
        return("only valids", [])
    i = 0
    invalids_in_set = []
    for id in range_class:
        i += 1
        str_id = str(id)
        mid_point = int((len(str(id)))/2)
        # print(f"mid point is {mid_point}")
        # print(f"id.{i}={id}")
        left_half, right_half = str_id[:mid_point], str_id[mid_point:]
        # print(f"left half:{left_half}\nright half:{right_half}")
        if left_half == right_half:
            invalids_in_set.append(id)
    return("maybe invalids", invalids_in_set)

all_invalids = []
for line in lines:
    # print(separateIds(line))
    for id_range in separateIds(line):
        # print(f"_______{id_range}")
        l_bound, u_bound = int(id_range.split("-")[0]), int(id_range.split("-")[1])
        # print(f"lower bound: {l_bound}, upper bound: {u_bound}")
        current_id_set = makeSetOfIds(l_bound,u_bound)
        # print(findTheIvalid(current_id_set)[1])
        all_invalid_id_in_set = findTheIvalid(current_id_set)[1]
        all_invalids = np.concatenate((all_invalids, all_invalid_id_in_set))
print(sum(all_invalids))

