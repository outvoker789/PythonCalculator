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
  if mat_action == "Сложение":
    addition()
  elif mat_action == "Вычитание":
    subtraction()
  elif mat_action == "Умножение":
    multiplication()
  elif mat_action == "Деление":
    division()
  else:
    print("Команда не разпознана.")

