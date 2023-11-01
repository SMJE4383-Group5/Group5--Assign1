def get_factors_sum(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors, sum(factors)

def main():
    try:
        num = int(input("Please enter a number: "))
        factors, factor_sum = get_factors_sum(num)
        if factor_sum == num:
            result = "perfect"
        else:
            result = "not perfect"
        print(f"Factors of {num}: {factors}")
        print(f"Sum of factors: {factor_sum}")
        print(f"The number is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()