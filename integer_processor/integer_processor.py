def process_integers(source_file='integers.txt'):
    try:
        # Open the source file for reading and output files for writing
        # Using a 'with' block ensures all files are closed automatically
        with open(source_file, 'r') as infile, \
             open('double.txt', 'w') as even_file, \
             open('triple.txt', 'w') as odd_file:
            
            # Iterate through each line in the source integers.txt
            for line in infile:
                # Remove whitespace and ensure the line isn't empty
                if line.strip(): 
                    # Convert string input to an actual integer
                    num = int(line.strip())
                    
                    # Logic: If the number is divisible by 2, it is even
                    if num % 2 == 0:
                        # Write the square of the even integer to double.txt
                        even_file.write(f"{num ** 2}\n")
                    else:
                        # Write the cube of the odd integer to triple.txt
                        odd_file.write(f"{num ** 3}\n")
                        
        print("Success: double.txt and triple.txt generated.")
        
    except FileNotFoundError:
        # Handle cases where integers.txt is missing from the directory
        print(f"Error: {source_file} not found.")
    except ValueError:
        # Handle cases where the file contains letters or symbols instead of numbers
        print("Error: File contains invalid (non-integer) data.")

# Execute the processing method
process_integers()