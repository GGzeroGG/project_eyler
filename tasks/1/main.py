amount = 0

for number in range(1, 1000):
    """
    Запускаю цикл от 1-999 чтобы найти среди них кратные 3 или 5
    """
    if (number % 3 == 0) or (number % 5 == 0):
        amount += number

print(amount)
