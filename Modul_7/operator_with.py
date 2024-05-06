file_ = 'file1.txt'
with open(file_, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')