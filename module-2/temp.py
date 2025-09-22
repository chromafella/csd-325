"""
Assignment: Module 2 - Documented Debugging + Flowchart(s)
Author: Brennan Cheatwood
Course: CSD-325
"""

def to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius, rounded to 2 decimals."""
    return round((fahrenheit - 32.0) * 5.0 / 9.0, 2)


if __name__ == "__main__":
    print("Type a Fahrenheit value and press Enter.")
    print("Press Enter on an empty line or type 'q' to quit.\n")
    while True:
        s = input("Fahrenheit: ").strip()
        if s == "" or s.lower() == "q":
            break
        try:
            f = float(s)
            c = to_celsius(f)
            print(f"{f:.2f}F -> {c:.2f}C\n")
        except ValueError:
            print("Not a number—try again.\n")
