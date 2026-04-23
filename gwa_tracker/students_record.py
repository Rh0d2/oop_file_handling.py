# Finding all students with the highest GWA
def main():
    infile = open('students_gwa.txt', 'r')
    
    best_gwa = 5.0
    # Change to a list to store multiple names
    best_students = []

    for line in infile:
        data = line.split()
        if len(data) >= 2:
            name = " ".join(data[:-1])
            gwa = float(data[-1])

            # Found a NEW best grade (lower than current)
            if gwa < best_gwa:
                best_gwa = gwa
                # Clear the list and add the new leader
                best_students = [name]
            
            # Found someone who TIED the current best grade
            elif gwa == best_gwa:
                best_students.append(name)
    
    infile.close()

    print("--- Highest GWA Result ---")
    print(f"Top GWA: {best_gwa}")
    print("Students:")
    for student in best_students:
        print(f"- {student}")

main()