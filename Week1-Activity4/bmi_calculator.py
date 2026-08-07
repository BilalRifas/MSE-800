# BMI Calculator CLI Application

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

 # introducing class
class BMICalculator:
   print("=== BMI Calculator CLI ===")
    
   # Validate input
   if weight <= 0 or height <= 0:
    print("Weight and height must be greater than 0.")


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

# Calculate BMI
bmi = calculate_bmi(weight, height)
    
# Get BMI category
category = get_bmi_category(bmi)
    
# Display result
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")    

# Main function
def main():

# Run the program
 if __name__ == "__main__":
     main()