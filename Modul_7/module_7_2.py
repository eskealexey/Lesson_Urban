def custom_write(file_name: str, strings: list) -> dict:
    dict_ = {}
    count = 0
    with open(file=file_name, mode='w', encoding='utf-8') as f:
        for str_ in strings:
            count += 1
            position = f.tell()
            tupl_ = count, position
            f.write('{}\n'.format(str_))
            dict_[tupl_] = str_
    return dict_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
