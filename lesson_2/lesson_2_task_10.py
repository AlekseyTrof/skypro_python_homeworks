def bank(x, y):
    balance = x
    for i in range(y):
        balance = balance * 1.1 # увеличиваем баланс на 10% каждый год
    return balance

x =float(input('Введите сумму вклада: '))
y = int(input('Введите срок вклада в годах: '))

result = bank(x, y)

# Округление до целых

# if (result % 1 != 0):
#     result = int(result) +1

print("Ваша сумма:", result)