from smartphone import Smartphone

catalog = [[], [], [], [], []]

# Список смартфонов
iphone = Smartphone("Iphone", "7+", "7 910 123 93 94")
xiaomi = Smartphone("Xiaomi", "Poco", "7 920 321 93 92")
samsung = Smartphone("Samsung", "S24", "7 925 432 94 32")
huawei = Smartphone("Huawei", "Nova", "7 930 943 95 56")
honor = Smartphone("Honor", "5X", "7 930 432 54 67")

# Сохранение смартфонов в каталог и сразу выводит список
catalog[0].append(iphone.info())
catalog[1].append(xiaomi.info())
catalog[2].append(samsung.info())
catalog[3].append(huawei.info())
catalog[4].append(honor.info())
