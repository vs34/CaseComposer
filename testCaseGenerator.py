# SAMPLE TEST CASE GENERATOR

# import random

# def generate_test_cases(t: int):
#     print(t)
#     total_n = 0
#     MAX_N = 2 * 10 # Maximum allowed sum of n
#     MAX_SINGLE_N = 10  # Maximum n in a single test case

#     for _ in range(t):
#         remaining_n = MAX_N - total_n  # Calculate remaining `n` that can be used
#         if remaining_n <= 0:  # Stop generating if the total limit is reached
#             break

#         upper_bound = min(remaining_n, MAX_SINGLE_N)  # Ensure upper bound is valid
#         n = random.randint(1, upper_bound) if upper_bound >= 1 else 1  # Avoid invalid range
#         m = 1  # Always 1 as per problem constraints
#         total_n += n
        
#         a = [random.randint(1, 10) for _ in range(n)]
#         b = [random.randint(1, 10) for _ in range(m)]
        
#         print(n, m)
#         print(" ".join(map(str, a)))
#         print(" ".join(map(str, b)))

# # Example usage: Generate up to 100 test cases
# generate_test_cases(1)
