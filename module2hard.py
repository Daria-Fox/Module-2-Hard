all_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for n in all_numbers:
    print("В первой вставке возникло число: ", n)
    print('Пароль: ')
    for a in range(1, n):
        for b in range(a+1, n):
            if n % (a + b) == 0:
                key = f'{a}{b}'
                print(key, end='')
    print()

