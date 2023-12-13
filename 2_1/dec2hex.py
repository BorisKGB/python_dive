#!/usr/bin/env python3

import argparse
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s: %(name)s - %(levelname)s - %(message)s",
                    style='%'
                    )
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Перевод в шестнадцатеричный формат")
    parser.add_argument('num', type=int, help="Число для перевода")
    args = parser.parse_args()

    number = args.num
    logger.debug(f"Got {number = }")

    _num = number
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
        logger.debug(f"Calculated character {digit}")
        res = digit + res
        _num //= base

    logger.info(f"Шестнадцатеричное представление числа: {res.upper()}")
    logger.info(f"Проверка результата: {hex(number)}")
