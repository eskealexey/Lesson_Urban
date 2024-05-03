file1 = open('file1.txt', mode='r')
print(file1.read())
file1.close()

# Вывод построчно
file2 = open('file1.txt', mode='r')
for t in file2:
    print(t, end='')
file2.close()

