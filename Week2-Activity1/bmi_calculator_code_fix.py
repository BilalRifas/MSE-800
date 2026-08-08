def check_number(value):
    """
    Checks whether the value can be converted
    into a floating-point number.
    """
    try:
        return float(value)
    except ValueError:
        return False


def get_number(message):
    """
    Keeps asking until a valid number is entered.
    """
    while True:
        number = check_number(input(message))

        if number is not False:
            return number

        print("Please enter a valid number.")


class BMICalculator:
    def __init__(self):
        self.weight = 0
        self.height = 0

    def get_data(self):
        """
        Gets weight in kilograms and height in centimetres.
        Height is converted into metres.
        """
        self.weight = get_number(
            "Enter your weight in kilograms: "
        )

        self.height = get_number(
            "Enter your height in centimetres: "
        ) / 100

    def calculate(self):
        """
        Calculates and returns the BMI.
        """
        return round(
            self.weight / (self.height ** 2),
            2
        )


def main():
    print("\n" + "=" * 42)
    print("Hello, let's calculate your BMI.")
    print("=" * 42)

    calculator = BMICalculator()
    print()
    calculator.get_data()
    bmi = calculator.calculate()
    print(f"Your BMI is {bmi}")
    print("\n" + "=" * 42)


if __name__ == "__main__":
    main()