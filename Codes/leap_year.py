# program to check if year is a leap year or not


def is_leapyear(year):
    return year % 4 == 0 and (year % 100 != 0 and year % 400 == 0)


if __name__ == "__main__":
    # To get year (integer input) from the user
    year = int(input("Enter a year: "))
    if is_leapyear(year):
        print(year, " is a leap year.")
    else:
        print(year, " is not a leap year.")
