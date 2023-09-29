def primeX(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def primeX(n):
    count = 0
    num = 2

    while True:
        if primeX(num):
            count += 1
            if count == n:
                return num
        num += 1
n = primeX

    # if x <= 1:
    #     return False
    # elif x <= 3:
    #     return True
    # elif x % 2 == 0 or x % 3 == 0:
    #     return False
    
    # i = 5
    # while i * i <= x:
    #     if x % i == 0 or x % (i + 2) == 0:
    #         return False
    # i = 5
    # while i * i <= x:
    #     if x % i == 0 or x % (i + 2) == 0:
    #         return False
    #     i += 6
    #     return True
    
    # def primeX(x):
    #     count = 0
    #     num = x
    

    #     while True:
    #         if primeX(num):
    #             count += 1
    #             if count == x:
    #                 return num
    #             num += 1

#     prime = True
#     for i in range(2, x):
#         if(x % i == 0):
#             prime = False
#             break
#     return prime

# min = 2
# max = 29
# for i in range(min, max + 1):
#     if primeX(i):
#         return primeX

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29