# 8_2assignment.py
# Loads student.json, prints original list, appends my record,
# prints updated list, then writes it back.

import json
from pathlib import Path

JSON_PATH = Path(__file__).parent / "student.json"

def load_students(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f) 
    if not isinstance(data, list):
        raise ValueError("student.json must contain a JSON array.")
    return data

def print_students(students):
    for s in students:
        # Example: Ripley, Ellen : ID = 45604 , Email = eripley@gmail.com
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")

def save_students(path: Path, students):
    with path.open("w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)
        f.write("\n")

def main():
    students = load_students(JSON_PATH)

    print("=== Original Student List ===")
    print_students(students)
    print()

    my_record = {
        "F_Name": "Brennan",
        "L_Name": "Cheatwood",
        "Student_ID": 99901,               # fictional ID
        "Email": "bcheatwood@example.com" 
    }
    students.append(my_record)

    print("=== Updated Student List (after append) ===")
    print_students(students)
    print()

    save_students(JSON_PATH, students)
    print(f"{JSON_PATH.name} has been updated.")

if __name__ == "__main__":
    main()
