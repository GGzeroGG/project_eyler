maximum_palindrome = 0

for multiplied in range(100, 999 + 1):
    """
    Берем все 3-х значные числа для умножаемого
    """
    for factor in range(multiplied, 999 + 1):
        """
        Берем все 3-х значные множители исключая те что мы уже умножали
        """
        # Умножаем числа получем произведение
        composition = multiplied * factor
        if str(composition) == str(composition)[::-1] and composition > maximum_palindrome:
            """
            Если произведение полиндром и оно болье текущего самого большого
            полиндрома то меняим их местами
            """
            maximum_palindrome = composition

print(maximum_palindrome)
