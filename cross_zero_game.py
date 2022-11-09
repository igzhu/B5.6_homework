a = ["", ".", ".", ".", "\n", ".", ".", ".", "\n", ".", ".", "."]  # поле игры,
#  a[1] = "", a[4] = "\n", a[8] = "\n" - нужны для отрисовки поля игры.
counter = 0  # счётчик ходов в пределах 1..9

# игровое поле
def play_field():
    play_map = "  ".join(map(str, a))
    print("Ваша игра:")
    print(play_map)


# сообщение-инструкция к игре
def help_field():
    help_info = ["", "1", "2", "3", "\n", "4", "5", "6", "\n", "7", "8", "9"]
    help_map = "  ".join(map(str, help_info))
    print('"КРЕСТИКИ-НОЛИКИ", Используйте цифровые клавиши для Ваших ходов в игре согласно этой расккладке:')
    print(help_map)


current_player = "X"  # текущий игрок
invite_str = f'Ваш ход, игрок "{current_player}": ' # текст приглашения сделать ход в игре

while True:
    help_field()
    print()
    play_field()
    player_move = input(invite_str)
    if not player_move.isdigit() or int(player_move) not in range(1, 10):
        invite_str = f' Неверный ход, игрок "{current_player}"!\n Жмите на цифровые клавиши незвнятых полей ещё раз:'
        continue
    elif int(player_move) in range(1, 4) and a[int(player_move)] not in ["O", "X"]:
        a[int(player_move)] = current_player
    elif int(player_move) in range(4, 7) and a[int(player_move) + 1] not in ["O", "X"]:
        a[int(player_move) + 1] = current_player
    elif int(player_move) in range(7, 10) and a[int(player_move) + 2] not in ["O", "X"]:
        a[int(player_move) + 2] = current_player
    else:
        invite_str = f'Неверный ход, игрок "{current_player}"! Это поле уже занято. Ходите заново: '
        continue
    # определение выигрыша: finish == True -- выигрыш, False -- нет
    finish = [a[1:4],       # закрыта строка 1
              a[5:8],       # закрыта строка 2
              a[9:],        # закрыта строка 3
              a[1::4],      # закрыт столбец 1
              a[2::4],      # закрыт столбец 2
              a[3::4],      # закрыт столбец 3
              a[1::5],      # закрыты диагорали
              a[3::3]].count([current_player for i in range(3)])  # какой игрок закрыл выигравшие поля
    counter += 1  # увеличен счётчик ходов
    if counter == 9 or finish:
        play_field()
        finish_str = f'Выиграл игрок "{current_player}".' if finish else 'Ничья.'
        print(f"Игра закончена. {finish_str}")
        break
    current_player = "O" if current_player == "X" else "X"  # смена игрока
    invite_str = f'Ваш ход, игрок "{current_player}": ' # текст  норм приглашения сделать ход в игре
