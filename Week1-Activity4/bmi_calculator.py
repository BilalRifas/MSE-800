# BMI Calculator CLI Application

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)


# Function to specify BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Main function
def main():
    print("=== BMI Calculator CLI ===")

    try:
        # Get user input
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Validate input
        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than 0.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Get BMI category
        category = get_bmi_category(bmi)

        # Display result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Input is not valid, Please enter numeric values only.")


# Run the program
if __name__ == "__main__":
    main()