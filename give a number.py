a = int(input("Give a number:"))
b, sum = 1, 0 # Initialize variables 'b' for counting and 'c' for accumulating the sum
# Loop from 1 to 'a', accumulating the sum of numbers
while b <= a:
    sum = sum + b # Add 'b' to 'c' to accumulate the sum
    b = b + 1 # Increment 'b' by 1 to move to the next number
# Print the values of 'a', 'b', and 'c' to show their final values
print("a:", a)
print("b:", b)
print("sum:", sum)
print("Result:", float(sum) / b - 1) # Calculate the average by dividing 'c' (sum) by 'b' (count) and subtracting 1