def is_year_leap(number):
    if number % 4 == 0 and (number % 100 != 0 or number % 400 == 0):
        return True
    else:
        return False


num = int(input("Введите год: "))
print(f"Год {num} — {is_year_leap(num)}")
