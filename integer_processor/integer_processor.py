def process_integers():
    with open('integers.txt', 'r') as infile:
        for line in infile:
            num = int(line.strip())
            # Logic: modulo 2 determines parity
            if num % 2 == 0:
                print(f"{num} is even")
            else:
                print(f"{num} is odd")

process_integers()