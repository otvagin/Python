from sys import argv
script_name, hours, tariff, bonus = argv
salary = (int(hours) * int(tariff)) + int(bonus)
print("Итоговая зарплата: ", salary)

