def is_year_leap(number):
    return "Высокосный" if number % 4 == 0 else "Не высокосный"


num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"Год {num}: - {result}")
