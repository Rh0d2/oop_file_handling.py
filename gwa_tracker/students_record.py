# Stage 1: Reading student data
print("RUNNING THIS FILE!!!")

def main():
    # Open the student data file
    # Format in txt: Name GWA (e.g., Rod 1.25)
    infile = open('students_gwa.txt', 'r')
    
    for line in infile:
        # split() separates the Name from the GWA
        data = line.split()
        print(f"Reading: {data}")
        
    infile.close()

main()