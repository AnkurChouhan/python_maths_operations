# Basic Mathematical Operations
def main():
    try:
        # Input two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2

        # Handle division by zero
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Undefined (cannot divide by zero)"

        # Results
        print(f"\nResults:")
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
