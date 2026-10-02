print("exe | jpg | pdf | docx | txt | png")

geronca_file_extension = input("File Extension: ").lower()
geronca_file_sizeinmb = float(input("MB Size: "))
geronca_file_deleted = input("File Deleted?(Yes/ No): ").lower()
geronca_evidence_folder = input("Inside Evidence Folder(Yes/No): ").lower()
geronca_recently_modified = input("Recently Modified (Yes/No): ").lower()

match geronca_file_extension:
    case "exe":
        if geronca_file_deleted == "yes":
            geronca_classification = "RECOVERY REQUIRED"
            geronca_recommended_action = "Attempt forensic recovery while preserving the original evidence."
        elif geronca_file_sizeinmb >= 100 or geronca_recently_modified == "yes":
            geronca_classification = "CRITICAL ALERT"
            geronca_recommended_action = "Immediately preserve and isolate the file for detailed forensic examination."
        else:
            geronca_classification = "ROUTINE EXAMINATION"
            geronca_recommended_action = "Include the file in the standard forensic examination process."

    case "jpg" | "png":
        if geronca_file_deleted == "yes" or (
            geronca_evidence_folder == "yes" and
            geronca_recently_modified == "yes"
        ):
            geronca_classification = "HIGH-PRIORITY EVIDENCE"
            geronca_recommended_action = "Preserve the file and examine its metadata and file history."
        else:
            geronca_classification = "ROUTINE EXAMINATION"
            geronca_recommended_action = "Include the file in the standard forensic examination process."

    case "pdf" | "docx" | "txt":
        if geronca_file_deleted == "yes":
            geronca_classification = "RECOVERY REQUIRED"
            geronca_recommended_action = "Attempt forensic recovery while preserving the original evidence."
        else:
            geronca_classification = "ROUTINE EXAMINATION"
            geronca_recommended_action = "Include the file in the standard forensic examination process."

    case _:
        print("Invalid")
        geronca_classification = "INVALID"
        geronca_recommended_action = "Please enter a valid file extension."

print("--- DIGITAL FORENSIC ASSESSMENT ---")
print(f"Classification: {geronca_classification.upper()}")
print(f"Recommended Action: {geronca_recommended_action}")
