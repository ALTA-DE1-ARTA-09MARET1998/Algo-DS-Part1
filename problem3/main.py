def fibonacci(number):
    a = 0
    b = 1
    count = 0 

    if number <= 0:
        return 0
    for i in range(0, number):
        a = b
        b = count
        count = a + b
    return count

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144

    #problem 3