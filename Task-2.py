#classify a range of numbers with respect to perfect, adundant or deficient 
#unless otherwise stated, variables are assumed to be of type int. Rule 4
top_num_str = input ("What is the upper number for the range:")
top_num= int(top_num_str)
number=15
while number <= top_num:
#sum up the divisors
 divisor = 2
 sum_of_divisors = 0 
 while divisor < number:
     if number % divisor == 0:    # divisor evenly divides the Num
          sum_of_divisors = sum_of_divisors + divisor
          divisor = divisor + 1
# # classify the number based on its divisor sum
number = float(input("What is the number?"))
sum_of_divisors = float(input("What is the sum of divisors?"))
if number == sum_of_divisors:
     print (number, "is perfect")
if number < sum_of_divisors: 
     print (number, "is abundant")
if number > sum_of_divisors:
     print (number, "is deficient")
     number += 1

