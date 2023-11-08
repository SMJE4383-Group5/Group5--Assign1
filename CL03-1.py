<<<<<<< HEAD
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
=======
# Input a number from the user
user_input = int(input("Enter a number: "))

# Initialize variables
counter = 1  # This will be equivalent to your previous 'b'
sum_result = 0  # This will be equivalent to your previous 'c'

# Calculate the sum of numbers from 1 to the user input
while counter <= user_input:
    sum_result = sum_result + counter
    counter = counter + 1

# Print the user input, the final value of 'counter', and the sum
print("User Input:", user_input)
print("Final Value of Counter:", counter)
print("Sum of Numbers from 1 to User Input:", sum_result)

# Calculate and print the result
result = float(sum_result) / counter - 1
print("Result:", result)
>>>>>>> 7eb5f8e4ef6796df46c08c7028bf2381b5e7fdf6
