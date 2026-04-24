def process_integers():
    # Basic file reading and verification
    with open('integers.txt', 'r') as infile:
        for line in infile:
            print(f"Read value: {line.strip()}")

process_integers()