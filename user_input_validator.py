def main():
    while True:
        try:
            age = int(input("Enter your age (1-120): "))
            if age < 1 or age > 120:
                raise ValueError("Age must be between 1 and 120")
            print(f"You are {age} years old")
            break
        except ValueError as e:
            print(f"Out of range. Please enter a valid age.")
            


if __name__ == "__main__":
    main()