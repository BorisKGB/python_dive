#!/usr/bin/env python3

import argparse
import logging


def triangle_exist(side_a: int, side_b: int, side_c: int) -> bool:
    logger = logging.getLogger(__name__)
    logger.debug("method start")
    result = True
    sides = [side_a, side_b, side_c]
    for side in sides:
        other_sides = sides.copy()
        other_sides.remove(side)
        if side > sum(other_sides):
            logger.info("Found an impossible triangle")
            result = False
            break
    logger.debug(f"Check finish, {result = } for {sides}")
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Проверка треугольника")
    parser.add_argument('side_a', metavar='a', type=int, help="одна из сторон треугольника")
    parser.add_argument('side_b', metavar='b', type=int, help="одна из сторон треугольника")
    parser.add_argument('side_c', metavar='c', type=int, help="одна из сторон треугольника")
    parser.add_argument('--log-to-file', action='store_true',
                        help="Включить логирование в файл log.log")
    parser.add_argument('-v', action='count', default=0, dest='verbosity',
                        help="Уровень подробности, можно указать несколько раз, максимум 2")
    args: argparse.Namespace = parser.parse_args()

    log_params = {
        "level": logging.INFO
    }

    if args.verbosity > 1:
        log_params["level"] = logging.NOTSET
    elif args.verbosity == 1:
        log_params["level"] = logging.DEBUG
    del args.verbosity

    if args.log_to_file:
        log_params["filename"] = "log.log"
        log_params["filemode"] = "a"
        log_params["encoding"] = "utf-8"
    del args.log_to_file

    logging.basicConfig(**log_params)

    a = args.side_a
    b = args.side_b
    c = args.side_c

    # print(triangle_exist(**args.__dict__))
    if triangle_exist(a, b, c):
        print("Треугольник существует")
        if a == b == c:
            print("Треугольник равносторонний")
        elif a == b or a == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Треугольник не существует")
