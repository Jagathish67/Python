def fibonacci(n):
    fib_series = [0, 1]
    for _ in range(n - 2): 
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]


num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print(" Please enter a positive number.")
else:
    print("Fibonacci Series:", fibonacci(num_terms))
