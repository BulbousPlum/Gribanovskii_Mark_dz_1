for num in range(100):
    num = num + 1
    if 11 <= num <= 19:
        print(num, 'процент')
    elif num % 10 == 1:
        print(num, 'процент')
    elif 2 <= num % 10 <= 4:
        print(num, 'процента')
    else:
        print(num, 'процентов')
