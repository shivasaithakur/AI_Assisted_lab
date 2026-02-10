'''1 def generate_palindrome(text):
    """Generate a palindrome by mirroring the input text."""
    return text + text[::-1]

# Example usage
result = generate_palindrome("hello")
print(result)  # Output: hellolleh
print(generate_palindrome("world"))  # Output: worlddlrow
print(generate_palindrome("python"))  # Output: pythonhcytop'''


'''2
def factorial(n):
    """Calculate the factorial of a given number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    input_num = int(input("Enter a number: "))
    print(factorial(input_num))'''

'''3
def is_armstrong_number(n):
        """Check whether a given number is an Armstrong number."""
        num_str = str(n)
        num_digits = len(num_str)
        sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
        return sum_of_powers == n

    # Example usage
if __name__ == "__main__":
        test_numbers = [153, 370, 123]
        for num in test_numbers:
            if is_armstrong_number(num):
                print(f"{num}: Armstrong Number")
            else:
                print(f"{num}: Not an Armstrong Number")'''
'''4
def is_perfect_number(n):
 """Check whether a given number is a perfect number."""
 if n <= 0:
     return False  
     sum_of_divisors = 0
     for i in range(1, n):
         if n % i == 0:
            sum_of_divisors += i
            return sum_of_divisors == n
# Example usage
if __name__ == "__main__":
    test_numbers = [6, 28, 496, 8128, 100]
    for num in test_numbers:
        if is_perfect_number(num):
            print(f"{num}: Perfect Number")
        else:
            print(f"{num}: Not a Perfect Number")'''

'''5
def is_perfect_number(n):
    """Check whether a given number is a perfect number."""
    if n <= 0:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n
# Example usage
if __name__ == "__main__":
    test_numbers = [6, 28, 496, 8128, 100, 1, -5, 0]
    for num in test_numbers:
        if is_perfect_number(num):
            print(f"{num}: Perfect Number")
        else:
            print(f"{num}: Not a Perfect Number")'''
            
def is_even_or_odd(n):
    """Check whether a given number is even or odd."""
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Example usage
if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        num = int(user_input)
        result = is_even_or_odd(num)
        print(f"{num}: {result}")
    except ValueError:
        print("Error: Please enter a valid integer.")


            
