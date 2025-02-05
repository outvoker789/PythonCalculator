#Модуль регулярных выражений
import re

#Запрос математического выражения
input_expression = input(f'Введите матемамтическое выражение, пример: "2+(3*1)".\n- ')

#Все матиматические операторы и числа добавляем в список
expression = re.findall(r'\d+\.\d+|\d+|\+|\-|\*|\/|\(|\)', input_expression)

#Выходная строка, стек операторов и приоритеты операторов
output_string = []
operator_stack = []

print(expression)

prior_oper = {"+":1,"-":1,"*":2,"/":2} 

#Алгоритм создания обратной польской записи из инфиксной записи
#Цикл перебора всех елементов математического выражения
for element in expression:
#Перевод числа в флоат, если число оператор то выдаст ошибку и пойдёт дальше
    try:
        float(element)
        output_string.append(element)
    except ValueError:    
#Условие, если елемент это оператор
        if element in prior_oper:
#Цикл который достаёт елементы с стека в выходную строку с условием, либо если стек пустой добавляет в него елемент
            while operator_stack and operator_stack[-1] != "(" and prior_oper.get(operator_stack[-1], 0) >= prior_oper[element]:
                output_string.append(operator_stack.pop())
            operator_stack.append(element)
#Условие, если елемент это закрывающая скобка
        elif element == ")":
#Добавляет элемент из стека в выходную строку, пока верхний элемент не является открывающей скобкой  
            while operator_stack and operator_stack[-1] != "(":
                output_string.append(operator_stack.pop())
#Если в стеке осталась только скобка, удаляет её
            operator_stack.pop()
#Условие, если елемент это закрывающая скобка, то добавляем елемент в стек
        elif element == "(":
            operator_stack.append(element)

#Добавляем все оставшиеся елементы из стека в выходную строку
while operator_stack:
    output_string.append(operator_stack.pop())
    
#Создание стека обратной польской записи
reverse_polish = []

#Алгоритм решения обратной польской записи
#Перебираем все елементы в выходной строке из польской записи
for term in output_string:
#Условие если елемент это число то добавляем его в стек ОПЗ
    try:
        float(term)
        reverse_polish.append(term)
    except ValueError:
#Если нет то считаем количество елементов в стеке, если больше или равно 2, берём оттуда 2 числа и выполняем соотвествующее решение 
        if len(reverse_polish) >= 2:
            b = reverse_polish.pop()
            a = reverse_polish.pop()
            if term == "+":
                reverse_polish.append(a + b)
            elif term == "-":
                reverse_polish.append(a - b)
            elif term == "*":
                reverse_polish.append(a * b)
            
            elif term == "/":
                try:
                    reverse_polish.append(a) / b)
                except ZeroDivisionError:
                    print("Я тебя на ноль помножу мудила")
                    exit()


#Выводим конечное решение в стеке
print(reverse_polish)