print('Сумма ряда\n')

# Дано натуральное число N.
# Программа для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 

number = int(input('Введите натуральное число N: '))

divider = 1 
summa = 1

for term in range(1, number): 
  divider *= -2
  summa += 1/divider

print('S =', summa)