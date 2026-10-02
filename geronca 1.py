geronca_grades = input("Enter GPA: ")

match geronca_grades:
    case "4.0":
        print("Your grade is 96-100.")
    case "3.5":
        print("Your grade is 90-95.")
    case "3.0":
        print("Your grade is 84-89.")
    case "2.5":
        print("Your grade is 78-83.")
    case "2.0":
        print("Your grade is 72-77.")
    case "1.5":
        print("Your grade is 66-71.")
    case "1.0":
        print("Your grade is 60-65.")
    case "R":
        print("Your grade is 59 and below.")
    case _:
        print("Invalid Input")
