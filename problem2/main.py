def is_prime(y):
    if y <= 1:
        return False
    elif y <= 3:
        return True
    elif y % 2 == 0 or y % 3 == 0:
        return False
    i = 5
    while i * i <= y:
        if y % i == 0 or y % (i + 2) == 0:
            return False
        i += 6
    return True

def primeX(x):
    count = 0
    num = 2 

    while True:
        if is_prime(num):
            count += 1
            if count == x:
                return num
        num += 1

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29