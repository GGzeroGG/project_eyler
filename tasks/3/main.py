number = 600851475143
divisor_max = 0

while number == 1:
    for supposed_divisor in (2, number + 1):
        if (number % supposed_divisor) == 0:
            if divisor_max < supposed_divisor:
                divisor_max = supposed_divisor
            number = number / supposed_divisor
            break

print(divisor_max)