# Generate a hailstone sequence 
number_str = input("Enter a positive integer: ")
number = int(number_str)
count = 0

print("Starting with number:", number)
print("Sequence is:", end=' ')

while number > 1:  # Stop when the sequence reaches 1
    if number % 2:  # Number is odd
        number = number * 3 + 1
    else:  # Number is even
        number = number // 2  # Use integer division to ensure the result is an integer
    print(number, end=', ')  # Add number to the sequence
    count += 1  # Add to the count

# After the loop, print the count and a newline for nicer output
print()
print("Sequence is", count, "numbers long")
