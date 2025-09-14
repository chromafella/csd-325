#Brennan Cheatwood
#Module 1.3 Assignment - On the Wall

def bottles_fmt(n: int) -> str:
    return f"{n} bottle(s)"

def main():
    try:
        n = int(input("Enter number of bottles: "))
    except ValueError:
        print("That's not a number...")
        return

    #start
    bottles = max(0, n)

    #While loop
    while bottles > 0:
        print(f"{bottles_fmt(bottles)} of beer on the wall, {bottles_fmt(bottles)} of beer.")
        bottles -= 1
        print(f"Take one down and pass it around, {bottles_fmt(bottles)} of beer on the wall.\n")

    #end
    print("Time to buy more bottles of beer.")

if __name__ == "__main__":
    main()