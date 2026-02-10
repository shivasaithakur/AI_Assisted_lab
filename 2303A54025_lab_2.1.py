#TASK1
import statistics
def analyze_numbers(numbers):
    """
    Calculates the mean, minimum, and maximum of a list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        tuple: A tuple containing (mean, minimum, maximum).
               Returns (None, None, None) if the list is empty.
    """
    if not numbers:
        return None, None, None

    mean_value = statistics.mean(numbers)
    min_value = min(numbers)
    max_value = max(numbers)

    return mean_value, min_value, max_value


data = [10, 20, 30, 40, 50]
mean, minimum, maximum = analyze_numbers(data)
print(f"List: {data}")
print(f"Mean: {mean}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")

data_empty = []
mean_empty, min_empty, max_empty = analyze_numbers(data_empty)
print(f"\nList: {data_empty}")
print(f"Mean: {mean_empty}")
print(f"Minimum: {min_empty}")
print(f"Maximum: {max_empty}")

#TASK2
#!/usr/bin/env python3
import argparse
import sys
def is_armstrong(n: int) -> bool:
    if n < 0:
        return False

    digits = [int(d) for d in str(n)]
    p = len(digits)
    return sum(d ** p for d in digits) == n
def main() -> None:
    parser = argparse.ArgumentParser(description="Check Armstrong numbers")
    parser.add_argument("number", nargs="?", type=int, help="integer to check")
    args = parser.parse_args()
    if args.number is None:
        try:
            s = input("Enter a non-negative integer: ").strip()
            num = int(s)
        except (EOFError, ValueError):
            print("Invalid input", file=sys.stderr)
            sys.exit(1)
    else:
        num = args.number
    print(num)
    print(is_armstrong(num))
if __name__ == "__main__":
    main()

#TASK3
year = int(input("Enter a year: ")) 
# A year is a leap year if: 
# - It is divisible by 4 AND 
#   - not divisible by 100, UNLESS 
#   - it is also divisible by 400 
if year % 400 == 0: 
    print(f"{year} is a leap year.") 
elif year % 100 == 0: 
    print(f"{year} is not a leap year.") 
elif year % 4 == 0: 
    print(f"{year} is a leap year.") 
else: 
    print(f"{year} is not a leap year.") 

#TASK4
t = (1, 2, 3, 4, 5, 6, 7)

even_sum = sum(i for i in t if i % 2 == 0)
odd_sum = sum(i for i in t if i % 2 != 0)

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
