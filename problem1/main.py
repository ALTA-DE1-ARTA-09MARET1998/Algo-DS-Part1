def remove_duplicates(array):
    if not array:
        return 0
    
    my_list = set()
    unique_index = 0

    for num in array:
        if num not in my_list:
            my_list.add(num)
            array[unique_index] = num
            unique_index += 1

    return unique_index

if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9]))  # 6
    print(remove_duplicates([2, 2, 2, 11]))          # 2
    print(remove_duplicates([2, 2, 2, 11]))          # 2
    print(remove_duplicates([1, 2, 3, 11, 11]))      # 4