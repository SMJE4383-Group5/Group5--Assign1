def square_root_newton(number, initial_guess, tolerance):
    guess = initial_guess
    iterations = 0

    while abs(guess**2 - number) > tolerance:
        guess = 0.5 * (guess + number / guess)
        iterations += 1

    return guess, iterations

# Take user inputs
number = int(input("Enter an integer number to find the square root of: "))
initial_guess = int(input("Enter an integer initial guess: "))
tolerance = float(input("Enter a floating-point tolerance: "))

# Apply the algorithm
result, num_iterations = square_root_newton(number, initial_guess, tolerance)

# Output the results
print(f"\nOriginal Conditions:")
print(f"Number: {number}")
print(f"Initial Guess: {initial_guess}")
print(f"Tolerance: {tolerance}")

print(f"\nResults:")
print(f"Square Root: {result}")
print(f"Number of Iterations: {num_iterations}")
