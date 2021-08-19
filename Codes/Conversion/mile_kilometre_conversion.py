# Taking kilometers input from the user
def km_mile(choice):
    # conversion factor
    conversion_fac = 0.621371

    if choice == 1:
        kilometers = float(input("Enter value in kilometers: "))
        # calculate miles
        miles = kilometers * conversion_fac
        print("%0.2f kilometers is equal to %0.2f miles" % (kilometers, miles))
    elif choice == 2:
        miles = float(input("Enter value in kilometers: "))
        # calculate kilometres
        kilometers = miles // conversion_fac
        print("%0.2f miles is equal to %0.2f miles" % (miles, kilometers))
    else:
        print("Wrong Choice!")
        quit()


if __name__ == "__main__":
    km_mile(
        int(
            input(
                "Enter your choice \n1) Kilometres to Miles: \n2) Miles to Kilometres: "
            )
        )
    )
