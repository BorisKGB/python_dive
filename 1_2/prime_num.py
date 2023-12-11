def is_prime_number(num):
    if num in [1, 2, 3]:
        return True
    result = True
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return result


num = 7

if 1 < num <= 100_000:
    if is_prime_number(num):
        print(f"{num} является простым числом")
    else:
        print(f"{num} является составным числом")
else:
    print("Число должно быть больше 1 и меньше 100000")