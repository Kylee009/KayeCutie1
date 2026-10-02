geronca_students = {
    "Ana": [90, 85, 82],
    "Kirk": [72, 73, 78],
    "RobertJoshRas": [91, 92, 93],
    "ShemJudeAlexisSoriano": [90, 91, 92],
    "CaesarKennethDeGuia": [92, 93, 94],
    "JosiahDatrellQuistadio": [90, 91, 94]
}

geronca_highest = 0
geronca_namehighest = ""
geronca_name75 = []
geronca_tally = 0

for geronca_name, geronca_grade in geronca_students.items():
    geronca_average = sum(geronca_grade) / len(geronca_grade)
    print(geronca_name, *geronca_grade, "- Average:", round(geronca_average, 2))

    if geronca_average > geronca_highest:
        geronca_highest = geronca_average
        geronca_namehighest = geronca_name

    for geronca_g in geronca_grade:
        if geronca_g < 75:
            geronca_tally = geronca_tally + 1
            if geronca_name not in geronca_name75:
                geronca_name75.append(geronca_name)

print()
print("Highest average is", round(geronca_highest, 2))
print(f"Congratulations, {geronca_namehighest}!")
print(f"There are {geronca_tally} grades below 75. Owned by {', '.join(geronca_name75)}.")
