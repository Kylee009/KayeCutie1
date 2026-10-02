print(f"{'GERONCA STUDENT PROGRAM FILTER':=^40}")

geronca_students = [
    ("Jonah Perez", "BSCS", 1),
    ("Alex Santos", "BSMT", 1),
    ("Micah Mendoza", "BSCS", 1),
    ("Allen Torres", "BSMT", 1),
    ("Nino Salvana", "BSCS", 3),
    ("Kristana Sarabia", "BSMT", 3),
    ("Shirly Alaton", "BSCS", 4),
    ("Sundae Marie Cruz", "BSMT", 4)
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
