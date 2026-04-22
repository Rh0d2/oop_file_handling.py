# Finding the highest GWA
def main():
    infile = open('students_gwa.txt', 'r')
    
    # Start with a very low grade (high number)
    best_gwa = 5.0
    best_student = ""

    for line in infile:
        data = line.split()
        if len(data) == 2:
            name = data[0]
            gwa = float(data[1])

            # Logic: If this GWA is lower (better) than our current best
            if gwa < best_gwa:
                best_gwa = gwa
                best_student = name
    
    infile.close()

    print("--- Highest GWA Result ---")
    print(f"Student: {best_student}")
    print(f"GWA: {best_gwa}")

main()