def month_to_season(s):
    if (s < 3) and (s > 11):
        print("Зима")
    elif (s > 2) and (s < 6):
        print("Весна")
    elif (s > 5) and (s < 9):
        print("Лето")
    else:
        (s > 8) and (s < 12),
        print("Осень")


season = int(input("Введите число: "))
result = month_to_season(season)
