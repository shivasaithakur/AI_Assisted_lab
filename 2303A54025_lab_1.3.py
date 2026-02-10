#TASK1
# Fibonacci Sequence - Non-modularized approach
n = int(input("Enter the number of terms for the Fibonacci sequence: "))
a, b = 0, 1

print(f"Fibonacci sequence ({n} terms):")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()  # New line at the end
print("Fibonacci sequence generated successfully!")

#TASK 2
from typing import List
# Fibonacci Sequence - Non-modularized approach
n = int(input("Enter the number of terms for the Fibonacci sequence: "))
a, b = 0, 1

print(f"Fibonacci sequence ({n} terms):")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

def fibonacci_sequence(n: int) -> List[int]:
    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == '__main__':
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    print(f"Fibonacci sequence ({n} terms): {fibonacci_sequence(n)}")

print()  # New line at the end
print("Fibonacci sequence generated successfully!")

#TASK3
def fibonacci(n):

    # Initialize the sequence with the first two Fibon
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Start with the first two numbers in the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate remaining Fibonacci numbers by summing the previous two
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    
    return fib_sequence


# Main program: Get user input and display
if __name__ == "__main__":
    # Prompt the user to enter the number of terms they want
    num_terms = int(input("Enter the number of Fibonacci terms: "))
    
    # Call the function and store the result
    result = fibonacci(num_terms)
    
    # Print the Fibonacci sequence
    print(f"Fibonacci sequence ({num_terms} terms): {result}")


#TASK4
"""
Comparative Analysis: Procedural vs Modular Fibonacci Implementation
======================================================================
"""

# ============================================================================
# COMPARISON TABLE
# ============================================================================

comparison_data = {
    "Criteria": [
        "Code Clarity",
        "Reusability",
        "Debugging Ease",
        "Maintainability",
        "Scalability",
        "Testing",
        "Documentation",
        "Performance Overhead"
    ],
    "Procedural (Without Functions)": [
        "Medium - Sequential logic, harder to follow",
        "Low - Cannot reuse code easily",
        "Medium - Errors mixed with main logic",
        "Low - Changes require modifying entire block",
        "Poor - Difficult to extend functionality",
        "Hard - Cannot isolate test cases",
        "Implicit - Logic embedded in code",
        "None - Direct execution"
    ],
    "Modular (With Functions)": [
        "High - Clear function names explain intent",
        "High - Functions can be called multiple times",
        "High - Isolated functions easier to debug",
        "High - Update single function vs entire code",
        "Excellent - Easy to add new features",
        "Easy - Test individual functions separately",
        "Explicit - Docstrings explain behavior",
        "Minimal - Function call overhead"
    ]
}

# ============================================================================
# ANALYSIS REPORT
# ============================================================================

analysis_report = """
EXECUTIVE SUMMARY
-----------------
The modular approach with functions is superior for professional development,
while procedural code may be acceptable for simple one-time scripts.

DETAILED ANALYSIS
-----------------

1. CODE CLARITY ★★★★★ (Modular Wins)
   - Procedural: Logic scattered throughout
   - Modular: Self-documenting function names (fibonacci_recursive, fibonacci_iterative)

2. REUSABILITY ★★★★★ (Modular Wins)
   - Procedural: Copy-paste entire code block
   - Modular: Import and call function anywhere

3. DEBUGGING EASE ★★★★☆ (Modular Wins)
   - Procedural: Print statements throughout code
   - Modular: Use debugger on specific function, unit tests isolate issues

4. MAINTAINABILITY ★★★★★ (Modular Wins)
   - Procedural: Bug fix requires modifying one monolithic block
   - Modular: Fix single function in isolation

5. SCALABILITY ★★★★★ (Modular Wins)
   - Procedural: Adding memoization requires rewriting
   - Modular: Create new function, keep old ones for comparison

6. TESTING ★★★★★ (Modular Wins)
   - Procedural: Cannot write unit tests
   - Modular: Easy pytest/unittest coverage

RECOMMENDATION
---------------
Use MODULAR approach for:
  ✓ Production code
  ✓ Team projects
  ✓ Code that will be maintained
  ✓ Any system with >100 lines

Use PROCEDURAL approach for:
  ✓ Quick scripts
  ✓ One-time analysis
  ✓ Learning/exploration
  ✓ Interactive notebooks (Jupyter)

CONCLUSION
----------
Modular code requires slightly more initial effort but pays dividends
in maintainability, testability, and scalability. Best practice: 
Always prefer functions unless writing disposable code.
"""

# ============================================================================
# DISPLAY RESULTS
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("COMPARATIVE ANALYSIS: FIBONACCI IMPLEMENTATIONS")
    print("=" * 80)
    print()
    
    # Print table header
    print(f"{'Criteria':<25} | {'Procedural':<30} | {'Modular':<30}")
    print("-" * 88)
    
    # Print table rows
    for i in range(len(comparison_data["Criteria"])):
        print(f"{comparison_data['Criteria'][i]:<25} | "
              f"{comparison_data['Procedural (Without Functions)'][i]:<30} | "
              f"{comparison_data['Modular (With Functions)'][i]:<30}")
    
    print()
    print(analysis_report)

 #TASK 5
import time
# ITERATIVE FIBONACCI
def fibonacci_iterative(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
# RECURSIVE FIBONACCI
def fibonacci_recursive(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# OPTIMIZED RECURSIVE (with memoization)
def fibonacci_memoized(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]
# COMPARISON & TESTING
if __name__ == "__main__":
    n = 35
    # Iterative Test
    start = time.time()
    result_iter = fibonacci_iterative(n)
    time_iter = time.time() - start
    print(f"Iterative (n={n}): {result_iter} | Time: {time_iter:.6f}s")
    # Recursive Test (safe limit)
    if n <= 30:
        start = time.time()
        result_rec = fibonacci_recursive(n)
        time_rec = time.time() - start
        print(f"Recursive (n={n}): {result_rec} | Time: {time_rec:.6f}s")
    else:
        print(f"Recursive: Skipped (too slow for n={n})")
    # Memoized Test
    start = time.time()
    result_memo = fibonacci_memoized(n)
    time_memo = time.time() - start
    print(f"Memoized (n={n}): {result_memo} | Time: {time_memo:.6f}s")


"""
COMPARISON SUMMARY:
═════════════════════════════════════════════════════════════════

┌─────────────────┬──────────────┬──────────────┬─────────────┐
│ Approach        │ Time         │ Space        │ Best For    │
├─────────────────┼──────────────┼──────────────┼─────────────┤
│ Iterative       │ O(n)         │ O(1)         │ Large n     │
│ Recursive       │ O(2^n)       │ O(n)         │ Small n     │
│ Memoized        │ O(n)         │ O(n)         │ Balanced    │
└─────────────────┴──────────────┴──────────────┴─────────────┘

WHEN TO AVOID RECURSION:
• Large input values (exponential growth makes it impractical)
• Without memoization/caching mechanism
• When stack overflow risk is high (deep call stacks)
• In performance-critical code

PERFORMANCE FOR LARGE N:
• Iterative: Handles n=1,000,000+ instantly
• Recursive: Becomes unusable beyond n=35-40
• Memoized: Handles large n efficiently with extra space
"""
