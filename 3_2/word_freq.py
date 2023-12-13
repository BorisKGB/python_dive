#!/usr/bin/env python3

import argparse
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s: %(name)s - %(levelname)s - %(message)s",
                    style='%'
                    )
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Часто встречающиеся слова")
    parser.add_argument('file', type=str, help="Путь до файла для проверки")
    parser.add_argument('-top', metavar="N", type=int, help="Вывести только N самых популярных", default=0)
    args = parser.parse_args()

    words_counter: dict[str:int] = dict()

    try:
        with open(args.file, "r") as file:
            word = ""
            char = file.read(1)
            while char:
                if char in ",.!'-\n\"":
                    char = " "
                elif char.isupper():
                    char = char.lower()
                if char == " ":
                    if len(word) > 0:
                        if word in words_counter:
                            words_counter[word] += 1
                        else:
                            words_counter[word] = 1
                        word = ""
                else:
                    word += char
                char = file.read(1)
    except FileNotFoundError as e:
        logger.error(f"Ошибка доступа к файлу, подробнее -> {e}")

    logger.debug(f"Из файла прочитано {len(words_counter.keys())} уникальных слов")
    result = [(word, words_counter[word]) for word in words_counter.keys()]
    result.sort(key=lambda x: (x[1]), reverse=True)
    if args.top > 0:
        print(result[:args.top])
    else:
        print(result)
