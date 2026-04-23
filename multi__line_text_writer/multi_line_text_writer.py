# Multi-line Text Writer
# Basic file creation and write test

def main():
    # Check if the script can create and write to a file
    file_output = open("mylife.txt", "w")
    file_output.write("System: Initializing multi-line writer test...\n")
    file_output.close()
    print("Base file created successfully.")

if __name__ == "__main__":
    main()