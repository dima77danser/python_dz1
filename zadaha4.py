#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

s = int(input('введите кол во журавлей: '))
if s % 6 ==0:
    print('Петя: ',s//6,'сережа:',s//6,'Катя:',(s//6)*4)
else:
    print('кол во журавлей нельзя поделить на детей')