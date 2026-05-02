import random
print('Добро пожаловать! это игра "Угадай число" от 1 до 100')
while True:
    secret = random.randint(1, 100)
    guesses = 0
    while guesses <= 6:
        number = int(input("Введи число от 1 до 100: "))
        if number == secret:
            print("Ты выиграл число было", secret)
            break
        elif number > secret:
            print("Меньше")
            guesses += 1
        elif number < secret:
            print("Больше")
            guesses += 1
        if guesses == 6:
            print("Ты проиграл, закончились попытки((", end=" ")
            print("Число было", secret)
            break
    print("Хотите сыграть ещё раз?     Введи:  Да или Нет")
    yes_or_no = input().lower()
    if yes_or_no == "нет" or yes_or_no == "no" or yes_or_no == "ytn":
        break
    else:
        secret = random.randint(1, 100)
        guesses = 0
