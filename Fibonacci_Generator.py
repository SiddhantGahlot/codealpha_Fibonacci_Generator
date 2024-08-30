def generate_fibonacci(n):
    fib_sequence = [0, 1]
    if n <= 0:
        return "The number of terms must be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    else:
        for i in range(2, n):
            next_value = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_value)
        return fib_sequence

# Input: Number of terms
n = int(input("Enter the number of terms: "))

# Generate Fibonacci series
fibonacci_series = generate_fibonacci(n)

# Output the series
print("Fibonacci Series:", fibonacci_series)
