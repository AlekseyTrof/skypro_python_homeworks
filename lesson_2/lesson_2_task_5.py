def month_to_season(x):
    
    if x in [1,2,12]:
        print("Зима")
    if x in [3,4,5]:
        print("Весна")
    if x in [6,7,8]:
        print("Лето")
    if x in [9,10,11]:
        print("Осень")
    if x >= 13 or x < 1:
        print(x)


month_to_season(11)