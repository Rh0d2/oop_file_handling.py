# Reading the file
def main():
    # Open the file
    infile = open('numbers.txt', 'r')
    
    # Read the data and split it into a list
    content = infile.read().split()
    
    # Show the numbers in the terminal
    print("Numbers found:", content)
    
    # Close the file
    infile.close()

main()
