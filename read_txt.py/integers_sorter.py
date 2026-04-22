# Program to separate integers into even.txt and odd.txt
def main():
    # Read the text file named numbers.txt
    infile = open('numbers.txt', 'r')
    content = infile.read().split()
    infile.close()

    # Create lists for sorting (matches your current logic)
    evens = []
    odds = []

    for item in content:
        num = int(item)
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    # Create the first text file named even.txt
    even_file = open('even.txt', 'w')
    for number in evens:
        even_file.write(str(number) + "\n")
    even_file.close()

    # Create the second text file named odd.txt
    odd_file = open('odd.txt', 'w')
    for number in odds:
        odd_file.write(str(number) + "\n")
    odd_file.close()

    print("Success! even.txt and odd.txt have been created.")

if __name__ == "__main__":
    main()