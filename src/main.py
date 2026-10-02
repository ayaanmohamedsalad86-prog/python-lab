from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        user_input = input("Enter a number: ")
        num = float(user_input)

        display_num = int(num) if num.is_integer() else num

        print(f"Square of {display_num}: {square(num)}")
        print(f"Even or Odd: {display_num} is {'Even' if is_even(num) else 'Odd'}")
        print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(num)}°F")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
