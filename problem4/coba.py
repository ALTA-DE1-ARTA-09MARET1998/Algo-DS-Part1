def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_grid(height, width, start):
    prime_grid = []

    num = start
    for _ in range(height):
        row = []
        for _ in range(width):
            while not is_prime(num):
                num += 1
            row.append(num)
            num += 1
        prime_grid.append(row)

    return prime_grid

height = 2  # Ganti dengan tinggi segiempat yang diinginkan
width = 5   # Ganti dengan lebar segiempat yang diinginkan
start = 1   # Ganti dengan bilangan prima pertama yang Anda inginkan

prime_square = generate_prime_grid(height, width, start)

# Menampilkan segiempat bilangan prima
for row in prime_square:
    print(row)