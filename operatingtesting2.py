def find_factors_and_check_perfect_number(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    
    factor_sum = sum(factors)

    if factor_sum == number:
        result = "perfect"
    else:
        result = "not perfect"
    
    return factors, factor_sum, result

try:
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Please enter a positive number.")
    else:
        factors, factor_sum, result = find_factors_and_check_perfect_number(num)
        factors = [factor for factor in factors if factor != num]
        print(f"Factors of {num} that are not equal to the number: {factors}")
        print(f"Sum of factors: {factor_sum}")
        print(f"The number is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")