"""Компания друзей собралась пойти в поход. Забот и затрат
при подготовке похода оказалось много: кто-то закупал еду, кто-то брал в
аренду снаряжение, кто-то заказывал транспорт. Когда всё было готово, друзья
решили подсчитать, кто сколько денег потратил и, соответственно, кто кому
сколько денег должен перевести. Статей расходов оказалось очень много,
участников похода было тоже много, поэтому сделать все расчеты вручную
оказалось затруднительно.
Напишите программу, которая по информации о том, кто сколько денег
потратил, определит: кто, кому и сколько денег должен перевести, чтобы
расходы всех участников похода оказались одинаковыми (с точностью до
копейки). Количество переводов при этом должно быть как можно меньше."""
names = input().split()
expenses = {name: 0 for name in names}
# количество покупок
n = int(input())

# Учет покупок
for _ in range(n):
    name, amount = input().split()
    expenses[name] += int(amount)

# Вычисляем общую сумму всех расходов
total_spent = sum(expenses.values())
# Вычисляем сколько каждый должен потратить (среднее)
average = total_spent / len(names)

receivers = []  # Те, кто потратил меньше среднего (должны получить)
payers = []     # Те, кто потратил больше среднего (должны отдать)

for name in names:
    balance = expenses[name] - average  # Разница от идеала
    if balance < -0.01:  # Потратил меньше (должен получить)
        receivers.append((name, -balance))  # Сохраняем положительное число долга
    elif balance > 0.01:  # Потратил больше (должен отдать)
        payers.append((name, balance))

receivers.sort(key=lambda x: x[1], reverse=True)
payers.sort(key=lambda x: x[1], reverse=True)

# Список для хранения переводов
transactions = []

# Распределяем долги
i = j = 0
while i < len(receivers) and j < len(payers):
    receiver, receive_amount = receivers[i]  # Тот, кто должен получить
    payer, pay_amount = payers[j]           # Тот, кто должен отдать

    # Вычисляем сумму перевода (минимальная из двух сумм)
    amount = min(receive_amount, pay_amount)

    # Добавляем перевод в результат
    transactions.append((payer, receiver, round(amount, 2)))

    # Уменьшаем оставшиеся суммы
    receive_amount -= amount
    pay_amount -= amount

    # Обновляем списки
    if receive_amount < 0.01:  # Деньги получены полностью
        i += 1
    else:
        receivers[i] = (receiver, receive_amount) # Обноовляем сумму

    if pay_amount < 0.01:  # Долг отдан полностью
        j += 1
    else:
        payers[j] = (payer, pay_amount)

print(len(transactions))
for payer, receiver, amount in transactions:
    print(f"{payer} {receiver} {amount:.2f}")