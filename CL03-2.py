limit_str = input("Range is 1 to input:")
limit_int = int(limit_str)
count_int = 1
sum_int = 0 

# Use the correct condition in the while loop
while count_int <= limit_int:
    sum_int = sum_int + count_int
    count_int = count_int + 1

average = float(sum_int) / (count_int - 1)

# Print the result
print(f"The sum of integers in the range 1 to {limit_int} is {sum_int}.")
print(f"The average of the sum is {average}.")
