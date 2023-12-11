num=255
_num = num
base = 16
res = ""

while _num > 0:
    digit = _num % base
    if digit < 10:
        digit = str(digit)
    elif digit == 10:
        digit = "a"
    elif digit == 11:
        digit = "b"
    elif digit == 12:
        digit = "c"
    elif digit == 13:
        digit = "d"
    elif digit == 14:
        digit = "e"
    elif digit == 15:
        digit = "f"
    res = digit + res
    _num //= base

print(f"Шестнадцатеричное представление числа: {res.upper()}")
print(f"Проверка результата: {hex(num)}")
