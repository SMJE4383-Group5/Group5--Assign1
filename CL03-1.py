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