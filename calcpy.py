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

#Цикл перебора всех елементов математического выражения
for element in expression:
#Условие, если елемент это число то сразу добавить его в выходную строку
    if element.isnumeric():
        output_string.append(element)
#Условие, если елемент это оператор
    elif element in prior_oper:
#Цикл который достаёт елементы с стека в выходную строку с условием, либо если стек пустой добавляет в него елемент
        while operator_stack and operator_stack[-1] != "(" and prior_oper.get(operator_stack[-1], 0) >= prior_oper[element]:
            output_string.append(operator_stack.pop())
        operator_stack.append(element)
    elif element == ")":
        while operator_stack and operator_stack[-1] != "(":
            output_string.append(operator_stack.pop())
        operator_stack.pop()
    elif element == "(":
        operator_stack.append(element)
while operator_stack:
    output_string.append(operator_stack.pop())
    
reverse_polish = []

for term in output_string:
    if term.isnumeric():
        reverse_polish.append(term)
    elif len(reverse_polish) >= 2:
        b = reverse_polish.pop()
        a = reverse_polish.pop()
        if term == "+":
            reverse_polish.append(float(a) + float(b))
        elif term == "-":
            reverse_polish.append(float(a) - float(b))
        elif term == "*":
            reverse_polish.append(float(a) * float(b))
        elif term == "/":
            reverse_polish.append(float(a) / float(b))
print(reverse_polish)