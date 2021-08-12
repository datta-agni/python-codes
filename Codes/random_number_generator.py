# Program to generate a random number between 0 and 9
# importing the random module
import random


def randomization_generators(
    low=int(input("Enter the starting point of generation: ")),
    high=int(input("Enter the end point for the generation: ")),
    mean=int(
        input(
            "Enter the mean for generating random numbers from a probability distribution: "
        )
    ),
    sigma=int(
        input(
            "Enter the standard deviation for generating random numbers from a probability distribution: "
        )
    ),
):
    print("Return a random integer N such that a <= N <= b")
    print(random.randint(low, high), "\n")

    print("Generate n random bytes.")
    print(
        random.randbytes(int(input("Enter the size for random byte generator: "))), "\n"
    )

    print(
        "Returns a non-negative Python integer with k random bits. This method is supplied with the MersenneTwister Generator."
    )
    print(
        random.getrandbits(int(input("Enter the number of bits for generation: "))),
        "\n",
    )

    print(
        "Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a. The end-point value b may or may not be included in the range depending on floating-point rounding in the equation a + (b-a) * random()."
    )
    print(random.uniform(low, high), "\n")

    print(
        "Gaussian distribution. mu is the mean, and sigma is the standard deviation. This is slightly faster than the normalvariate() function defined below."
    )
    print(random.gauss(mean, sigma), "\n")

    print(
        "Log normal distribution. If you take the natural logarithm of this distribution, you’ll get a normal distribution with mean mu and standard deviation sigma. mu can have any value, and sigma must be greater than zero."
    )
    print(random.lognormvariate(mean, sigma), "\n")

    print("Normal distribution. mu is the mean, and sigma is the standard deviation.")
    print(random.normalvariate(mean, sigma))


if __name__ == "__main__":
    randomization_generators()
