def banner():
	print('''
          Калькулятор
████████████████████████████████
████░░██░░░░██░░████████████████
██░░██░░████░░██░░██████████████
░░██░░██░░░░██░░██░░████████████
░░██░░████░░██░░██░░░░██████████
██░░░░░░░░██░░░░░░░░██░░████████
██████░░██░░████░░██░░██░░██████
████░░██░░░░██████░░░░██░░██████
████░░████████████████░░████████
██████░░██░░░░░░░░░░██░░████████
████████░░░░██████░░░░██████████
██░░░░████░░░░░░░░░░████████████
██░░██░░████████████████████████
██░░░░██████░░████░░░░░░████████
██░░██░░██░░██░░████░░██████████
██░░░░██████░░██████░░██████████
Чтобы закончить, напишите "stop"
#------------------------------#''')
banner(); 

while True:
    try:
        Example_sign = input('Введите знак между X и N: ')
        if Example_sign == 'stop':
            break
        print('Пример: ' + 'X ' + Example_sign + ' N')
        if Example_sign in ('+', '-', '*', '/'):
            print('')
            Example_1 = float(input('Введите число X: '))
            if Example_1%1 == 0:

                print('Пример: ', Example_1, Example_sign, 'N')
                print('')
                Example_2 = float(input('Введите число N: '))
                if Example_2%1 == 0:
                    print('Пример: ', Example_1, Example_sign, Example_2)
                    if Example_sign == '+':
                        Result = Example_1 + Example_2
                    elif Example_sign == '-':
                        Result = Example_1 - Example_2
                    elif Example_sign == '*':
                        Result = Example_1 * Example_2
                    elif Example_sign == '/':
                        Result = Example_1 / Example_2
                else:
                    print('Вводите целое число!')
            else:
                print('Вводите целое число!')
    except ValueError:
        print('Ошибка в числе.')
    print('Результат: ', Result)
    print('')
    print('#------------------------------#')
    print('')
