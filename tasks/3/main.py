number = 600851475143
divisor_max = 0

while number > 1:
    """
    Цикл который идет пока число не дойдет до 1
    """
    for supposed_divisor in range(2, number + 1):
        """
        Цикл который выдает предпологаемый делитель
        """
        if (number % supposed_divisor) == 0:
            """
            Проверяем если число делится без остатка значит это наш делитель
            """
            # Делим число на простой делитель чтобы разкладывать его дальше
            number //= supposed_divisor
            if divisor_max < supposed_divisor:
                """
                Если наш делитель больше текущего максимального то меняем их 
                местами
                """
                divisor_max = supposed_divisor
            break

print(divisor_max)
