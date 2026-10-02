print(f"{'GERONCA STUDENT PROGRAM FILTER':=^40}")

geronca_students = [
    ("Jonah Perez", "BSCS", 1),
    ("Alex Santos", "BSMT", 1),
    ("Micah Mendoza", "BSCS", 1),
    ("Allen Torres", "BSMT", 1),
    ("Cheijay Paul Loberiza", "BSCS", 3),
    ("Dean MisaBustamante", "BSMT", 3),
    ("Datrell Quistadio", "BSCS", 4),
    ("Cat Dela Cruz", "BSMT", 4)
]

print("Student Information")
for geronca_student in geronca_students:
    print("Name: ", geronca_student[0])
    print("Program: ", geronca_student[1])
    print("Year Level: ", geronca_student[2])
    print()

geronca_program = input("Search program: ")
print("Students in ", geronca_program.upper(), " program: ")

geronca_found = False

for geronca_student in geronca_students:
    if geronca_program.lower() == geronca_student[1].lower():
        print("Name: ", geronca_student[0])
        print("Program: ", geronca_student[1])
        print("Year Level: ", geronca_student[2])
        print()
        geronca_found = True

if not geronca_found:
    print("No students.")
