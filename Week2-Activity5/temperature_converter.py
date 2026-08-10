class TemperatureConverter:
    def __init__(self, user_input):
        self.user_input = user_input.strip()

    def is_valid(self):
        # Check minimum length
        if len(self.user_input) < 2:
            return False

        prefix = self.user_input[0]

        # Validate prefix
        if prefix not in ('F', 'C'):
            return False

        # Validate numeric part
        try:
            float(self.user_input[1:])
            return True
        except ValueError:
            return False

    def convert(self):
        prefix = self.user_input[0]
        value = float(self.user_input[1:])

        if prefix == 'F':
            celsius = (value - 32) * 5 / 9
            return f"{self.user_input} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius"

        elif prefix == 'C':
            fahrenheit = (value * 9 / 5) + 32
            return f"{self.user_input} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit"


def main():
    user_input = input("Enter temperature (e.g., F51 or C11): ")

    converter = TemperatureConverter(user_input)

    if converter.is_valid():
        print(converter.convert())
    else:
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")


if __name__ == "__main__":
    main()