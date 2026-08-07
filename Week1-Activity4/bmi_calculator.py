# BMI Calculator CLI Application

 # introducing class
class BMICalculator:
   
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
  

# Run the program
if __name__ == "__main__":
     print("=== BMI Calculator CLI ===")
    
     weight = float(input("Enter your weight in kilograms: "))
     height = float(input("Enter your height in meters: "))
         
     # Validate input
     if weight <= 0 or height <= 0:
      print("Weight and height must be greater than 0.")
      
     # Calculate BMI
     bmi = BMICalculator.calculate_bmi(weight, height)
    
     # Get BMI category
     category = BMICalculator.get_bmi_category(bmi)
    
     # Display result
     print(f"\nYour BMI is: {bmi:.2f}")
     print(f"Category: {category}")   