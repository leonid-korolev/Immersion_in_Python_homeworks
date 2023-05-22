# Задачи с урока
'''
Задание №8
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
'''
while True:
    try:
        n = int(input('Сколько рядов у ёлки? - '))
        i = 1 
        for k in range (n):  
            print(" "*((n-k)), "*" * i) 
            i+=2
        break   
    except:
        print('Введите количество рядов цифрами.')
        


'''
Задание №9
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
'''
for i in range(2,11):
    for j in range(2,6):
        print(f'{j} * {i} ={i * j:4}\t', end=' ')
    print('')
print()
for i in range(2,11):
    for j in range(6,10):
        print(f'{j} * {i} ={i * j:4}\t', end=' ')
    print('')
        

# Домашнее задание.
'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого
отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше 
суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить 
является ли треугольник разносторонним, равнобедренным или равносторонним.
'''
while True:
    try:    
        print('Введите длину сторон треугольника: ')
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))

        if a + b <= c or a + c <= b or b + c <= a:
            print('Треугольник не существует')
        elif a != b and a != c and b != c:
            print('Треугольник разносторонний')
        elif a == b == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
        break
    except:
        print('Неверный ввод данных.')



'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''
MIN = 0
MAX = 100000
temp = False
while True:
    number = int(input('Введите число в диапозоне от 1 до 100000: ')) 
    if MIN < number <= MAX: 
        for i in range(2, number):
            if (number % i) == 0:
                temp = True
                break
        if(temp):
            print('Число составное')
        else:
            print('Число простое')
        break
    else:
        print('Недопустимое значение')

    

'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
number = None
count = 10

print('Угадайте число от 0 до 1000:' )
while number != num:
    number = input('Введите число: ')
    if not number.isdigit():
        print('Неверный ввод данных.')
    else:
        number = int(number)
        if number > UPPER_LIMIT:
            print('Число должно быть в диапазоне от 0 до 1000')
        elif number > num:
            print('Загаданное число меньше.')
        elif number < num:
            print('Загаданное число больше. ')
        elif number == num:
            print(f'Вы угадали! Загаданное число - {num} ')            
        count -= 1
        if count == 0:
            print("Попытки закончились")
            break

