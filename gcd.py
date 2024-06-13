#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

def gcd(x, y):
    """
    GCD function for two numbers using the Euclidean algorithm
    x = y*quotient + remainder
    gcd(x, y) == gcd(y, remainder)
    :param x: First number
    :param y: Second number
    :return: GCD
    """
    while y:
        z = x
        x = y
        y = z % y
    return x
print(f"GCD is {gcd(1680, 640)}")