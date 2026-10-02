geronca_students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 78,
    "Diana": 95
}

print("STUDENT GRADES")
print("==============")
print("Ana:", geronca_students["Ana"])
print("Ben:", geronca_students["Ben"])

geronca_students["Ella"] = 88
geronca_students["Carlo"] = 82
geronca_students["Diana"] = 91

geronca_name1 = input("Enter student name: ")
geronca_grade1 = int(input("Enter student grade: "))
geronca_students[geronca_name1] = geronca_grade1

print(geronca_students)

print("\nUpdated Student Grades")
print("======================")
for geronca_name, geronca_grade in geronca_students.items():
    print(geronca_name, ":", geronca_grade)

geronca_search = input("\nEnter student name to search: ")

if geronca_search in geronca_students:
    print(geronca_search, "has a grade of", geronca_students[geronca_search])
else:
    print("Student not found.")

print()

geronca_lowest_student = min(geronca_students, key=geronca_students.get)
geronca_lowest_grade = geronca_students[geronca_lowest_student]
print(geronca_lowest_student)

geronca_highest_student = max(geronca_students, key=geronca_students.get)
geronca_highest_grade = geronca_students[geronca_highest_student]
print(geronca_highest_student)

geronca_difference = geronca_highest_grade - geronca_lowest_grade
print(geronca_difference)

geronca_average = sum(geronca_students.values()) / len(geronca_students)
print(geronca_average)
