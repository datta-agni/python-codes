# A python program to create a basic calculator.


def operator(ch):
    switcher = {
        1: add(a, b),
        2: sub(a, b),
        3: mul(a, b),
        4: div(a, b),
        5: exp(a, b),
    }
    func = switcher.get(ch)
    print("\n", "    Your Answer is:    ", func)


def add(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def div(a, b):
    c = a / b
    return c


def mul(a, b):
    c = a * b
    return c


def exp(a, b):
    c = a ** b
    return c


if __name__ == "__main__":
    print(
        """
            \nChoose the operator
            \n1.) Addition
            \n2.) Subtraction
            \n3.) Multiplication
            \n4.) Division
            \n5.) Exponents
            \n"""
    )

    ch = int(input("Enter your choice: "))
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operator(ch)
