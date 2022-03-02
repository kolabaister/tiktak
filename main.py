def doska_draw(doska):

    print("      1   2   3 ")
    print("    _____________")
    for i in range(len(doska)):
        print(str(i+1) + "  ( ", " | ".join(doska[i]), " )")
        #print(" | ".join(doska[i]))
        if i == len(doska) - 1:
            break
    print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾")



def vvod_hoda():
    while True:
        koord=input("Введите вместе номер строки и столбца, например 11 или 31: ")

        row = int(koord[0]) - 1
        col = int(koord[-1]) - 1
        if (0 <= row <= 2) or (0 <= col <= 2):
            break
        else:
            print("Номер строки или столбца может быть от 1 до 3")

    print("Ваш ход: ", hod[-1], " на строку",  row+1, " и столбец ", col+1)
    return row, col


def pobeditel(player, doska):

    cols = any([
        [doska[i][0] for i in range(3)].count(player) == 3,
        [doska[i][1] for i in range(3)].count(player) == 3,
        [doska[i][2] for i in range(3)].count(player) == 3,
    ])

    rows = any([
        doska[0].count(player) == 3,
        doska[1].count(player) == 3,
        doska[2].count(player) == 3,
    ])

    check_cols_and_rows = all([
        doska[0][0] == player,
        doska[1][1] == player,
        doska[2][2] == player,
    ])

    check_45 = all([
        doska[0][2] == player,
        doska[1][1] == player,
        doska[2][0] == player,
    ])

    return any([rows, cols, check_cols_and_rows, check_45])





global doska, svobodno, hod
doska = [[' ', ' ', ' '] for i in range(3)]
svobodno = [(i, j) for i in range(3) for j in range(3)]
hod = 'X'

doska = [
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' '],
            ]

svobodno = [(i, j) for i in range(3) for j in range(3)]

while True:
    doska_draw(doska)


    print("Ход " , hod)

    cell = vvod_hoda()

    if cell in svobodno:
        doska[cell[0]][cell[1]] = hod
        svobodno.remove(cell)
    else:
        print("Клетка занята")
        continue

    if pobeditel(hod, doska):
        doska_draw(doska)
        print(hod, " победили")
    
        break

    if not svobodno:
        doska_draw(doska)
        print("Ничья")
    
        break

    if hod == 'O':
        hod = 'X'
    else:
        hod = 'O'
