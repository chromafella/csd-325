"""
sitka_high_low_bmc.py

Changes & Notes (Module 4 requirements):
- Added a startup menu with instructions: choose Highs, Lows, or Exit.
- Program loops until the user selects Exit.
- When 'Highs' is selected, plot daily high temperatures in RED.
- When 'Lows' is selected, plot daily low temperatures in BLUE.
- Uses sys.exit() to terminate cleanly with a friendly exit message.
- Reuses elements from earlier programs:
  * csv reading
  * datetime parsing for dates
  * matplotlib plotting and formatting
- Added robust CSV parsing with try/except to skip bad rows and warn the user.
- Encapsulated logic in functions for clarity and maintainability.

Assumptions:
- CSV file is 'sitka_weather_2018_simple.csv' and columns are:
  date at index 2 (YYYY-MM-DD), high at index 5, low at index 6
  (matches the "simple" dataset from Python Crash Course).
"""

import sys
import csv
from datetime import datetime
from random import choice

from matplotlib import pyplot as plt

FILENAME = 'sitka_weather_2018_simple.csv'

def load_weather(filename):
    """Load dates, highs, and lows from the CSV;
    skip rows with missing/invalid data."""
    dates, highs, lows = [], [], []
    skipped = 0

    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            header_row = next(reader, None)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    high = int(row[5])
                    low = int(row[6])
                except Exception:
                    skipped += 1
                    continue

                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    except FileNotFoundError:
        print(f'[ERROR] File: {filename} not found.')
        sys.exit(1)

    if skipped:
        print(f'[WARNING] Skipped {skipped} row(s) with missing data')

    return dates, highs, lows

def plot_series(dates, values, series_label, color, ylabel="Temperature (F)"):
    fig, ax = plt.subplots()
    ax.plot(dates, values, c=color, linewidth=1.5, label=series_label)

    #format
    plt.title(f"Daily {series_label} Temperatures - 2018", fontsize=16)
    plt.xlabel("")
    fig.autofmt_xdate()
    plt.ylabel(ylabel, fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)

    ax.legend()
    plt.show()


def print_menu():
    print("\n=============== Sitka Weather (2018) ===============")
    print("Choose an option:")
    print("   [H] Highs   - Show daily high temperatures in Red")
    print("   [L] Lows   - Show daily low temperatures in Blue")
    print("   [E] Exit   - Quit")
    print("\n====================================================")

def main():
    dates, highs, lows = load_weather(FILENAME)

    while True:
        print_menu()
        choice = input("Enter H, L, or E: ").strip().lower()

        if choice in ('h', 'high', 'highs'):
            plot_series(dates, highs, "High", color='red')
        elif choice in ('l', 'low', 'lows'):
            plot_series(dates, lows, "Low", color='blue')
        elif choice in ('e', 'exit', 'q', 'quit'):
            print("Thanks for using Sitka Weather Viewer. Goodbye!")
            sys.exit(0)
        else:
            print("[ERROR] Invalid choice. Please enter H, L, or E.")

if __name__ == '__main__':
    main()