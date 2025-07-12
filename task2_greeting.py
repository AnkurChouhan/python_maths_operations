# Personalized Greeting
def main():
    # Take user's first and last name
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    # Concatenate full name
    full_name = f"{first_name} {last_name}"

    # Print greeting
    print(f"Hello, {full_name}! Welcome to the Python world.")

if __name__ == "__main__":
    main()
