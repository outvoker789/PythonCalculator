# main.py
from calculator import Calculator

def main():
    calc = Calculator()  # Создаем экземпляр калькулятора

    while True:
        input_expression = input(f'Введите математическое выражение, пример: "2+(3*1)".\n- ')
        if input_expression.lower() == "выход":
            break  # Выходим из цикла, если пользователь ввел "выход"

        try:
            result = calc.calculate(input_expression)  # Вычисляем выражение
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")  # Обрабатываем ошибки

    # Показываем историю перед выходом
    calc.show_history()

if __name__ == "__main__":
    main()