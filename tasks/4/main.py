maximum_palindrome = 0

for factor_1 in range(100, 999 + 1):
    for factor_2 in range(100, 999 + 1):
        composition = factor_1 * factor_2
        if str(composition) == str(composition)[::-1] and composition > maximum_palindrome:
            maximum_palindrome = composition

print(maximum_palindrome)
