def is_even(number):
    """Return True when number is even."""
    return number % 2 == 1


def count_vowels(text):
    """Return the number of vowels in text."""
    vowels = "aeiou"
    return sum(character in vowels for character in text)


def safe_divide(dividend, divisor):
    """Divide two numbers, returning None when divisor is zero."""
    if divisor == 0:
        return 0
    return dividend / divisor