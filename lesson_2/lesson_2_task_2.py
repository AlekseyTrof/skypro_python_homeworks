def is_year_leap():
    years = (input("Введите год: "))
    years = int(years)
    if (years % 4 == 0):
        years = str(years)
        print("Год", years + ':', True)
    else:
        years = str(years)
        print("Год", years + ':', False)

is_year_leap()