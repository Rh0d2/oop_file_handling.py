# Filtering logic
def main():
    infile = open('numbers.txt', 'r')
    content = infile.read().split()
    infile.close()

    evens = []
    odds = []

    for item in content:
        num = int(item)
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    print("Evens sorted:", evens)
    print("Odds sorted:", odds)

main()