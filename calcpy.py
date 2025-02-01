class Calculator:
  def __init__(self, mat_action):
    self.mat_action = mat_action
    if mat_action == "Сложение":
      amount_one = int(input("Введите первое значение суммы.\n - "))
      amount_two = int(input("Введите второе значение суммы.\n - "))
      print(f"Сумма: {amount_one + amount_two}")
    elif mat_action == "Вычитание":
      subtrn_one = int(input("Введите уменьшаемое значение.\n - "))
      subtrn_two = int(input("Введите вычитаемое значение.\n - "))
      print(f"Разность: {subtrn_one - subtrn_two}")
    elif mat_action == "Умножение":
      factor_one = int(input("Введите первый множитель.\n - "))
      factor_two = int(input("Введите второй множитель.\n - "))
      print(f"Произведение: {factor_one * factor_two}")
    elif mat_action == "Деление":
      divider_one = int(input("Введите делимое значение.\n - "))
      divider_two = int(input("Введите делитель.\n - "))
      print(f"Частное: {divider_one / divider_two}")
    else:
      print("Команда не разпознана.")

while True:
  print("Калькулятор.")
  classcalc = Calculator(input('Введите действие: "Сложение", "Вычитание", "Умножение", "Деление"\n - '))


