# Информация о файле

Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Реализовать получение пути до файла силами argparse

## Пример использования

На входе:

`app.py "C:/Users/User/Documents/example.txt"`

На выходе:

`('C:/Users/User/Documents/', 'example', '.txt')`

## Примеры запуска из консоли

**Запуск выполнялся из linux консоли, для этого в файле создан заголовок `#!/usr/bin/env python3`, в windows требуется явно указывать интерпретатор**

```
$ ./file_info.py /tmp/MarkdownNavigatorEnhanced-3.0.213.150.zip
('/tmp', '/tmp/MarkdownNavigatorEnhanced-3.0.213.150', '.zip')
$ ./file_info.py something.txt
('', 'something', '.txt')
```
