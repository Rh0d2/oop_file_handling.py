def process_integers():
    with open('integers.txt', 'r') as infile, \
         open('double.txt', 'w') as even_file, \
         open('triple.txt', 'w') as odd_file:
            
        for line in infile:
            num = int(line.strip())
            if num % 2 == 0:
                even_file.write(f"{num ** 2}\n") # Square of even
            else:
                odd_file.write(f"{num ** 3}\n") # Cube of odd

process_integers()