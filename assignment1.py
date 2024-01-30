# Name: Sarah Chao
# OSU Email: Chaosa@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1 - Python Fundamentals Review
# Due Date: 01/29/2024
# Description:


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    TODO: Write this implementation
    """
    static_array_length = arr.length()
    min, max = arr[0], arr[0]
    for i in range(static_array_length):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return (min, max)
    
# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    ret = StaticArray(size=arr.length())
    for i in range(arr.length()):
        if arr[i] % 3 == 0 and arr[i] % 5 == 0:
            value = "fizzbuzz"
        elif arr[i] % 5 == 0:
            value = "buzz"
        elif arr[i] % 3 == 0:
            value = "fizz"
        else:
            value = arr[i]
        ret[i] = value
    return ret

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    """
    static_array_length = arr.length()
    for i in range(static_array_length // 2): 
        arr[i], arr[static_array_length-1-i] = arr[static_array_length-1-i], arr[i]

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    ret = StaticArray(size=arr.length())
    for i in range(arr.length()):
        ret[(i + steps) % arr.length()] = arr[i]
    return ret

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    if start > end: # 1
        interval = start-end+1 # 1
        ret = StaticArray(size=interval) # 1
        direction = -1 # 1
    else:
        interval = end-start+1 # 1
        ret = StaticArray(size=interval) # 1
        direction = 1 # 1
    for i, value in enumerate(range(start, end, direction)):
        ret[i] = value
    ret[interval-1] = end

    return ret

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    """
    if arr.length() == 1:
        return 1

    desc = 0
    asc = 0
    for i in range(arr.length() - 1):
        if arr[i] >= arr[i+1]:
            desc = -1
        else:
            asc = 1
    return asc + desc

            

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    TODO: Write this implementation
    """
    # current_val = arr[0]
    # current_val_count = 0
    mode = arr[0]
    frequency = 0
    i = 0 
    while i < arr.length():
        current_val = arr[i]
        current_val_count = 0
        while i < arr.length() and current_val == arr[i]:
            current_val_count += 1
            if current_val_count > frequency:
                frequency = current_val_count
                mode = current_val
            i += 1
# [1,1,1,2,2,5,5]
    return (mode, frequency)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # [1,1,4,4]
    # [1, 4]
    distinct_values = 1
    for i in range(arr.length() - 1): #O(n)
        if arr[i] == arr[i+1]:
            continue
        distinct_values += 1

    no_duplicates = StaticArray(distinct_values)

    i = 0
    j = 0 #no_duplicates index
    while i < arr.length():
        current_val = arr[i]
        no_duplicates[j] = current_val
        while i < arr.length() and current_val == arr[i]:
            i += 1
        j += 1
    return no_duplicates

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # get min and max to get range, create static-array for each value in range
    # itereate over range of values in n
    
    min, max = min_max(arr)

    value_counts = StaticArray(max-min+1)
    for i in range(max-min+1):
        value_counts[i] = 0
    
    for i in range(arr.length()):
        value = arr[i]
        value_counts_i = value - min
        value_counts[value_counts_i] += 1

    ret = StaticArray(arr.length())
    
    insert_at = 0
    max_offset = 0
    for i in range(value_counts.length()-1, -1, -1):
        number_of_values = value_counts[i]
        value = max - max_offset
        for _ in range(number_of_values):
            ret[insert_at] = value
            insert_at += 1
        max_offset += 1
    
    return ret

   

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """


    positives = StaticArray(arr.length())
    negatives = StaticArray(arr.length())
    ret = StaticArray(arr.length())

    p, n = 0, 0
    for i in range(arr.length()):
        if arr[i] >= 0:
            positives[p] = arr[i]**2
            p += 1
        else:
            negatives[n] = arr[i]**2
            n += 1

    reverse(negatives)

    p, n = 0, 0
    i = 0
    while n < arr.length() and negatives[n] == None: n += 1
    while p < arr.length() and positives[p] != None and n < arr.length():
        if positives[p] <= negatives[n]:
            ret[i] = positives[p]
            p += 1
        else:
            ret[i] = negatives[n]
            n += 1
        i += 1

    while p < arr.length() and positives[p] != None:
        ret[i] = positives[p]
        i += 1
        p += 1
    while n < arr.length():
        ret[i] = negatives[n]
        i += 1
        n += 1
    reverse(ret)
    return ret


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":


    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
