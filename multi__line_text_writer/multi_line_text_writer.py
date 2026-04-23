# Multi-line Text Writer
# Final implementation with interactive loop

def main():
    # 'with' handles closing the file automatically even if an error occurs
    with open("mylife.txt", "w") as my_file:
        while True:
            entry = input("Enter line: ")
            my_file.write(entry + "\n")
            
            choice = input("Are there more lines y/n? ").lower()
            if choice == 'n':
                break
                
    print("\nFile 'mylife.txt' has been updated with your entries.")

if __name__ == "__main__":
    main()