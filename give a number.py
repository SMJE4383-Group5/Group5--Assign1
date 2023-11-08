number = int(input("Give a number:"))
count, sum = 1, 0 # Initialize variables 'count' for counting and 'sum' for accumulating the sum
# Loop from 1 to 'number', accumulating the sum of numbers
while count <= number:
    sum = sum + count # Add 'count' to 'sum' to accumulate the sum
    count = count + 1 # Increment 'count' by 1 to move to the next number
# Print the values of 'number', 'count', and 'sum' to show their final values
print("number:", number)
print("count:", count)
print("sum:", sum)
print("Result:", float(sum) / count - 1) # Calculate the average by dividing 'sum' (sum) by 'count' (count) and subtracting 1
