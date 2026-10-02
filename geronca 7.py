while True:
    geronca_word = input("Enter a word: ")
    geronca_character = input("Enter a character to search for: ")

    geronca_found = False

    for geronca_letter in geronca_word:
        if geronca_letter.lower() == geronca_character.lower():
            geronca_found = True
            break

    if geronca_found:
        print("Character Found!")
    else:
        print("Character not found.")

    geronca_again = input("Try again? (Y/N): ")

    if geronca_again.upper() != "Y":
        break
