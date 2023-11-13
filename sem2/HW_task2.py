# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать
# сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

number1 = input('Введите дробь вида “a/b”: ')
number2 = input('Введите вторую дробь: ')
a = Fraction(number1)
b = Fraction(number2)
print(a + b)
print(a * b)
