def max_sequence(arr):
    # if not (arr):
    #     return arr

    max_sum = 0
    current_sum = 0

    for i in arr:
        current_sum = current_sum + i
        if current_sum < 0:
            current_sum = 0
        if max_sum < current_sum:
            max_sum = current_sum
    return max_sum 

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12