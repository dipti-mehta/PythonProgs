def sum_of_sq(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)
    return sm


n = 4
print(sum_of_sq(n))

# -----------using list comprehension

# Take input from user
N = 5

# Use list comprehension to create list of squares
squares_list = [i*i for i in range(1, N+1)]

# Find sum of squares using sum() function
sum_of_squares = sum(squares_list)

# Print the result
print("Sum of squares of first", N, "natural numbers is", sum_of_squares)
