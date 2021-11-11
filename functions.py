from sympy import divisors

def find_index(num):
    # Get each of the factors from the current number
    factors = divisors(num)

    # Initialize the counter
    sum_of_factors = 0
    # and then add the factors together
    for factor in factors:
        sum_of_factors += factor

    # Calculate the index by dividing the sum of the factors by the number we're working on
    index = sum_of_factors / num

    return index, sum_of_factors, factors