#!/usr/bin/env python3

import argparse
from os.path import dirname, splitext


def get_file_info(file_path):
    dir_path = dirname(file_path)
    file_name, file_ext = splitext(file_path)
    return dir_path, file_name, file_ext


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Инфо о файле")
    parser.add_argument('file', type=str, help="Путь до файла")
    args = parser.parse_args()
    print(get_file_info(args.file))
