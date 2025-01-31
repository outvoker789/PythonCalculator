class Calculator:

  def addition():
    amount_one = int(input("Введите первое значение суммы.\n - "))
    amount_two = int(input("Введите второе значение суммы.\n - "))
    print(f"Сумма: {amount_one + amount_two}")

  def subtraction():
    subtrn_one = int(input("Введите уменьшаемое значение.\n - "))
    subtrn_two = int(input("Введите вычитаемое значение.\n - "))
    print(f"Разность: {subtrn_one - subtrn_two}")

  def multiplication():
    factor_one = int(input("Введите первый множитель.\n - "))
    factor_two = int(input("Введите второй множитель.\n - "))
    print(f"Произведение: {factor_one * factor_two}")

  def division():
    divider_one = int(input("Введите делимое значение.\n - "))
    divider_two = int(input("Введите делитель.\n - "))
    print(f"Частное: {divider_one / divider_two}")

while True:
  print("Калькулятор.")
  mat_action = input('Введите действие: "Сложение", "Вычитание", "Умножение", "Деление"\n - ')
  if mat_action == "Сложение" or "Вычитание" or "Умножение" or "Деление":
    if mat_action == "Сложение":
      Calculator.addition()
    elif mat_action == "Вычитание":
      Calculator.subtraction()
    elif mat_action == "Умножение":
      Calculator.multiplication()
    elif mat_action == "Деление":
      Calculator.division()
  else:
    print("Команда не разпознана.")

