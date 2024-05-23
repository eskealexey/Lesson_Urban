# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.


def all_variants(text: str) -> str:
    length = len(text)
    for st in range(length):
        for end in range(st + 1, length + 1):
            yield text[st:end]

a = all_variants('abc')
for i in a:
    print(i)
