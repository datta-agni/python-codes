# program to convert temperature in celsius to fahrenheit


def temperature_conversion(
    choice=int(
        input(
            "Enter your choice:\n1) Fahrenheit to Celsius: \n2) Celsius to Fahrenheit:  "
        )
    ),
):
    if choice == 1:
        # change this value for a different result
        celsius = float(input("Enter the temperature in Celsius: "))
        # calculate fahrenheit
        fahrenheit = (celsius * 1.8) + 32
        print(
            "%0.1f degree Celsius is equal to %0.1f degree Fahrenheit"
            % (celsius, fahrenheit)
        )
    elif choice == 2:
        # change this value for a different result
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        # calculate fahrenheit
        celsius = (fahrenheit - 32) // 1.8
        print(
            "%0.1f Fahrenheit is equal to %0.1f degree degree Celsius"
            % (fahrenheit, celsius)
        )
    else:
        print("Wrong Choice!")
        quit()


if __name__ == "__main__":
    temperature_conversion()
