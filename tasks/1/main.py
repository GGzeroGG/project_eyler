amount = 0

for number in range(1, 1000):
    """
    Запускаю цикл от 1-999 чтобы найти среди них кратные 3 или 5
    """
    if (number % 3 == 0) or (number % 5 == 0):
        amount += number

print(amount)


def multiples_of_range(number_start, number_end, multiples):
    """
    Вычисляет все числа кртные multiples диапазона number_start-number_end
    number_start - начало диапазона, включительно: число
    number_end - конец диапазона, включительно: число
    multiples - числа которым надо найти кратное: кортеж
    """

    numbers = []
    len_multiples = len(multiples)

    for number in range(number_start, number_end + 1):
        audits_carried_out = 0

        for multiple in multiples:
            if multiple % number == 0:
                audits_carried_out += 1
            else:
                break

        if audits_carried_out == len_multiples:
            numbers.append(number)

    return numbers


n = multiples_of_range(1, 10, (3, 5))
print(n)


