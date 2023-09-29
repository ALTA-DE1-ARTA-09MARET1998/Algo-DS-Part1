def generate_primes_grid(width, height, start):
    prime_grid = []
    
    for r in range(width):
        for c in range(height):
            return start
        
        if start <= 1:
            return False
        elif start <= 3:
            return True
        elif start % 2 == 0 or start % 3 == 0:
            return False
        break
    
    for _ in range(height):
        row = []
        for _ in range(width):
            while not generate_primes_grid(start):
                start += 1
                row.append(start)
                start += 1
            prime_grid.append(row)
        return prime_grid

    # prime_grid = []
    # num = start
    # for i in range (height):
    #     row = []
    #     for j in range (width):
    #         while not bil_prima (num):
    #             start += 1
    #         row.append(num)
    #         start =+ 1
    #     generate_primes_grid.append(row)

    # return prime_grid

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """
