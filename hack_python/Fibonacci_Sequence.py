def generate_fibonacci(n):

    # Start the sequence with the first two terms
    fibonacci_sequence = [0, 1]

    # Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.  
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

# Ask the user to input the number of terms, n
n = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci_sequence = generate_fibonacci(n)

# Print the generated Fibonacci sequence.
print(f"The Fibonacci sequence up to the {n}th term is:", fibonacci_sequence)

