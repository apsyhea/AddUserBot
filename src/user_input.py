def get_invite_count():
    while True:
        try:
            invite_count = int(input("Введите количество приглашений: "))
            return invite_count
        except ValueError:
            print("Ошибка: Введите корректное число.")
