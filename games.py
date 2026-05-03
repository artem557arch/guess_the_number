import random
print('Добро пожаловать! Это игра "Угадай число" от 1 до 100 за 7 попыток.')
print("Правила таковы, я загадываю число, а ты отгадываешь.")
while True:
    secret = random.randint(1, 100)
    guesses = 0
    while guesses < 7:
        try:
            number = int(input("Введи число от 1 до 100: "))
        except ValueError:
            print("Видимо ты ввел не число. Попробуй ещё раз.")
            continue
        if number > 100 or number < 1:
            print("Число должно быть от 1 до 100")
            continue
        if number == secret:
            print("Ты выиграл! Число было", secret)
            break
        elif number > secret:
            print("Меньше")
            guesses += 1
            print("Попыток использовано", guesses, "из 7")
        elif number < secret:
            print("Больше")
            guesses += 1
            print("Попыток использовано", guesses, "из 7")
        if guesses == 7:
            print("Ты проиграл, попытки закончились((", end=" ")
            print("Число было", secret)
            break
    print("Хотите сыграть ещё раз?     Введи:  Да или Нет")
    while True:
        yes_or_no = input().lower()
        if yes_or_no == "нет" or yes_or_no == "no":
            exit()
        elif yes_or_no == "да" or yes_or_no == "yes":
            break
        else:
            print("Ты ввел некорректный ответ. Введи:  Да или Нет     Enter:  Yes or No")
            continue