#!/usr/bin/env python3

import argparse
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s: %(name)s - %(levelname)s - %(message)s",
                    style='%'
                    )
logger = logging.getLogger(__name__)


def is_prime_number(num):
    dbg_counter = 1
    if num in [1, 2, 3]:
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(f"Number {num} validated in {dbg_counter} steps")
        return True
    result = True
    for i in range(2, (num//2)+1):
        if logger.isEnabledFor(logging.DEBUG):
            dbg_counter += 1
        if num % i == 0:
            result = False
            break
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(f"Number {num} validated in {dbg_counter} steps")
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Простое число")
    parser.add_argument('num', type=int, help="Число для проверки")
    args = parser.parse_args()

    number = args.num
    logger.debug(f"Got {number = }")

    if 1 < number <= 100_000:
        if is_prime_number(number):
            logger.info(f"{number} является простым числом")
        else:
            logger.info(f"{number} является составным числом")
    else:
        logger.info("Число должно быть больше 1 и меньше 100000")
