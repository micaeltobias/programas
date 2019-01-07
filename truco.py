import random
import getch
import time
import os

# ------------- VARS GLOBAL -------------------------------------

card = ['Q', 'J', 'K', 'A', '2', '3']
naipe = ['o', 'e', 'd', 'r']

# ------------- MAKE --------------------------------------------

def makeHandPlayer():
    hand = []
    check = True
    while check == True:
        for i in range(3):
            temp = []
            cd = random.randint(0, 5)
            np = random.randint(0, 3)
            temp.append(card[cd])
            temp.append(naipe[np])
            hand.append(temp)
        check = checkHand(hand)
        if check == True:
            hand.clear()
    else:
        return hand

def makeHandOpponent(hand_player):
    hand = []
    check = True
    while (check == True):
        for i in range(3):
            temp = []
            cd = random.randint(0, 5)
            np = random.randint(0, 3)
            temp.append(card[cd])
            temp.append(naipe[np])
            hand.append(temp)
        check = checkHandOpponent(hand, hand_player)
        if check == True:
            hand.clear()
    else:
        return hand

def makeTable(mao):
    table = []
    for x in range(22):
        temp = []
        for y in range(76):
            if (x == 0) or (x == 21):
                if (y == 0) or (y == 75):
                    temp.append("|")
                else:
                    if (y == 0) or (y == 75):
                        temp.append("|")
                    else:
                        temp.append("-")
            else:
                if (y == 0) or (y == 75):
                    temp.append("|")
                else:
                    temp.append(" ")
        table.append(temp)
    return table

def makeVira(maoPlayer, maoOpponent):
    vira = []
    check = True
    while check == True:
        cd = random.randint(0, 5)
        np = random.randint(0, 3)
        vira.append(card[cd])
        vira.append(naipe[np])
        check = checkVira(vira, maoPlayer, maoOpponent)
        if check == True:
            vira.clear()
    else:
        return vira

# ------------- CHECK --------------------------------------------

def checkHand(mao):
    equal = False
    if (mao[1] == mao[0]) or (mao[2] == mao[0]) or (mao[2] == mao[1]):
        equal = True
        return equal
    else:
        return equal

def checkHandOpponent(mao, maoPlayer):
    equal = False
    if (mao[0] == maoPlayer[0]) or (mao[0] == maoPlayer[1]) or (mao[0] == maoPlayer[2]):
        equal = True
        return equal
    elif (mao[1] == maoPlayer[0]) or (mao[1] == maoPlayer[1]) or (mao[1] == maoPlayer[2]):
        equal = True
        return equal
    elif (mao[2] == maoPlayer[0]) or (mao[2] == maoPlayer[1]) or (mao[2] == maoPlayer[2]):
        equal = True
        return equal
    elif (mao[1] == mao[0]) or (mao[2] == mao[0]) or (mao[2] == mao[1]):
        equal = True
        return equal
    else:
        return equal

def checkVira(vira, maoPlayer, maoOpponent):
    if (vira == maoPlayer[0]) or (vira == maoPlayer[1]) or (vira == maoPlayer[2]):
        return True
    elif (vira == maoOpponent[0]) or (vira == maoOpponent[1]) or (vira == maoOpponent[2]):
        return True
    else:
        return False

def checkWinPlayerTurn(vira, cardPlayer, cardOpponent):
    # CHECAR SE TEM MANILHA
    if (card.index(cardPlayer[0]) == card.index(vira[0])+1):
        manilhaPlayer = True
    else:
        manilhaPlayer = False
    if (card.index(cardOpponent[0]) == card.index(vira[0])+1):
        manilhaOpponent = True
    else:
        manilhaOpponent = False

    if (cardPlayer[0] == "Q") and (vira[0] == "3"):
        manilhaPlayer = True

    if (cardOpponent[0] == "Q") and (vira[0] == "3"):
        manilhaOpponent = True
    # ----------------------------------------------------------
    if (manilhaPlayer == True) and (manilhaOpponent == False):
        return "player"
    elif (manilhaPlayer == False) and (manilhaOpponent == True):
        return "opponent"
    elif (manilhaPlayer == True) and (manilhaOpponent == True):
        if (naipe.index(cardPlayer[1]) > naipe.index(cardOpponent[1])):
            return "player"
        else:
            return "opponent"
    else:
        if (card.index(cardPlayer[0]) > card.index(cardOpponent[0])):
            return "player"
        elif (card.index(cardPlayer[0]) < card.index(cardOpponent[0])):
            return "opponent"
        elif (card.index(cardPlayer[0]) == card.index(cardOpponent[0])):
            return "draw"
# ------------- SHOW ---------------------------------------------

def showTable(table):
    for x in range(len(table)):
        for y in range(len(table[0])):
            print(table[x][y], end="")
        print("")

def showCardsPlayer(table, mao, cardOne, cardTwo, cardThree):
    # PRIMEIRA CARTA
    if (cardOne == True):
        for x in range(15, 21):
            for y in range(20, 27):
                if (x == 15) or (x == 20):
                    if (y == 20) or (y == 26):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 15) and ((y == 20) or (y == 26)):
                    table[x][y] = "|"

                if (x == 16) and (y == 21):
                    table[x][y] = mao[0][1]

                if (x == 18) and (y == 23):
                    table[x][y] = mao[0][0]

                if (x == 20) and (y == 25):
                    table[x][y] = mao[0][1]
    else:
        for x in range(15, 21):
            for y in range(20, 27):
                if (x == 15) or (x == 20):
                    if (y == 20) or (y == 26):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 15) and ((y == 20) or (y == 26)):
                    table[x][y] = " "

                if (x == 16) and (y == 21):
                    table[x][y] = " "

                if (x == 18) and (y == 23):
                    table[x][y] = " "

                if (x == 20) and (y == 25):
                    table[x][y] = " "
    # SEGUNDA CARTA
    if (cardTwo == True):
        for x in range(15, 21):
            for y in range(29, 36):
                if (x == 15) or (x == 20):
                    if (y == 29) or (y == 35):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 15) and ((y == 29) or (y == 35)):
                    table[x][y] = "|"

                if (x == 16) and (y == 30):
                    table[x][y] = mao[1][1]

                if (x == 18) and (y == 32):
                    table[x][y] = mao[1][0]

                if (x == 20) and (y == 34):
                    table[x][y] = mao[1][1]
    else:
        for x in range(15, 21):
            for y in range(29, 36):
                if (x == 15) or (x == 20):
                    if (y == 29) or (y == 35):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 15) and ((y == 29) or (y == 35)):
                    table[x][y] = " "

                if (x == 16) and (y == 30):
                    table[x][y] = " "

                if (x == 18) and (y == 32):
                    table[x][y] = " "

                if (x == 20) and (y == 34):
                    table[x][y] = " "
    # TERCEIRA CARTA
    if (cardThree == True):
        for x in range(15, 21):
            for y in range(38, 45):
                if (x == 15) or (x == 20):
                    if (y == 38) or (y == 44):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 15) and ((y == 38) or (y == 44)):
                    table[x][y] = "|"

                if (x == 16) and (y == 39):
                    table[x][y] = mao[2][1]

                if (x == 18) and (y == 41):
                    table[x][y] = mao[2][0]

                if (x == 20) and (y == 43):
                    table[x][y] = mao[2][1]
    else:
        for x in range(15, 21):
            for y in range(38, 45):
                if (x == 15) or (x == 20):
                    if (y == 38) or (y == 44):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 15) and ((y == 38) or (y == 44)):
                    table[x][y] = " "

                if (x == 16) and (y == 39):
                    table[x][y] = " "

                if (x == 18) and (y == 41):
                    table[x][y] = " "

                if (x == 20) and (y == 43):
                    table[x][y] = " "

def showCardsOpponent(table, mao, cardOne, cardTwo, cardThree):
    # PRIMEIRA CARTA
    if (cardOne == True):
        for x in range(1, 7):
            for y in range(20, 27):
                if (x == 1) or (x == 6):
                    if (y == 20) or (y == 26):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 1) and ((y == 20) or (y == 26)):
                    table[x][y] = "|"
    else:
        for x in range(1, 7):
            for y in range(20, 27):
                if (x == 1) or (x == 6):
                    if (y == 20) or (y == 26):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 1) and ((y == 20) or (y == 26)):
                    table[x][y] = " "

    # SEGUNDA CARTA
    if (cardTwo == True):
        for x in range(1, 7):
            for y in range(29, 36):
                if (x == 1) or (x == 6):
                    if (y == 29) or (y == 35):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 1) and ((y == 29) or (y == 35)):
                    table[x][y] = "|"
    else:
        for x in range(1, 7):
            for y in range(29, 36):
                if (x == 1) or (x == 6):
                    if (y == 29) or (y == 35):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 1) and ((y == 29) or (y == 35)):
                    table[x][y] = " "


    # TERCEIRA CARTA
    if (cardThree == True):
        for x in range(1, 7):
            for y in range(38, 45):
                if (x == 1) or (x == 6):
                    if (y == 38) or (y == 44):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 1) and ((y == 38) or (y == 44)):
                    table[x][y] = "|"
    else:
        for x in range(1, 7):
            for y in range(38, 45):
                if (x == 1) or (x == 6):
                    if (y == 38) or (y == 44):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 1) and ((y == 38) or (y == 44)):
                    table[x][y] = " "

def showVira(table, vira, show):
    if (show == True):
        for x in range(8, 14):
            for y in range(64, 71):
                if (x == 8) or (x == 13):
                    if (y == 64) or (y == 70):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 8) and ((y == 64) or (y == 70)):
                    table[x][y] = "|"

                if (x == 9) and (y == 65):
                    table[x][y] = vira[1]

                if (x == 11) and (y == 67):
                    table[x][y] = vira[0]

                if (x == 13) and (y == 69):
                    table[x][y] = vira[1]
    else:
        for x in range(8, 14):
            for y in range(64, 71):
                if (x == 8) or (x == 13):
                    if (y == 64) or (y == 70):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 8) and ((y == 64) or (y == 70)):
                    table[x][y] = " "

                if (x == 9) and (y == 65):
                    table[x][y] = " "

                if (x == 11) and (y == 67):
                    table[x][y] = " "

                if (x == 13) and (y == 69):
                    table[x][y] = " "

def showCardPlayerInTable(card, table, show):
    if (show == True):
        for x in range(8, 14):
            for y in range(38, 45):
                if (x == 8) or (x == 13):
                    if (y == 38) or (y == 44):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 8) and ((y == 38) or (y == 44)):
                    table[x][y] = "|"

                if (x == 9) and (y == 39):
                    table[x][y] = card[1]

                if (x == 11) and (y == 41):
                    table[x][y] = card[0]

                if (x == 13) and (y == 43):
                    table[x][y] = card[1]
    else:
        for x in range(8, 14):
            for y in range(38, 45):
                if (x == 8) or (x == 13):
                    if (y == 38) or (y == 44):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 8) and ((y == 38) or (y == 44)):
                    table[x][y] = " "

                if (x == 9) and (y == 39):
                    table[x][y] = " "

                if (x == 11) and (y == 41):
                    table[x][y] = " "

                if (x == 13) and (y == 43):
                    table[x][y] = " "

def showCardOpponentInTable(card, table, show):
    if (show == True):
        for x in range(8, 14):
            for y in range(20, 27):
                if (x == 8) or (x == 13):
                    if (y == 20) or (y == 26):
                        table[x][y] = " "
                    else:
                        table[x][y] = "_"

                if (x != 8) and ((y == 20) or (y == 26)):
                    table[x][y] = "|"

                if (x == 9) and (y == 21):
                    table[x][y] = card[1]

                if (x == 11) and (y == 23):
                    table[x][y] = card[0]

                if (x == 13) and (y == 25):
                    table[x][y] = card[1]
    else:
        for x in range(8, 14):
            for y in range(20, 27):
                if (x == 8) or (x == 13):
                    if (y == 20) or (y == 26):
                        table[x][y] = " "
                    else:
                        table[x][y] = " "

                if (x != 8) and ((y == 20) or (y == 26)):
                    table[x][y] = " "

                if (x == 9) and (y == 21):
                    table[x][y] = " "

                if (x == 11) and (y == 23):
                    table[x][y] = " "

                if (x == 13) and (y == 25):
                    table[x][y] = " "


# ------------- MAIN ---------------------------------------------
def main():
    pointsPlayer = 0
    pointsOpponent = 0
    while (pointsPlayer < 12) and (pointsOpponent < 12):
        # DECLARAÇÃO DAS VARIÁVEIS
        cardEsc = [0, 1, 2]
        handPlayer = makeHandPlayer()
        handOpponent = makeHandOpponent(handPlayer)
        vira = makeVira(handPlayer, handOpponent)
        table = makeTable(handPlayer)
        showOnePlayer, showTwoPlayer, showThreePlayer = True, True, True
        showOneOpponent, showTwoOpponent, showThreeOpponent = True, True, True
        showPlayerCardInTable, showOpponentCardInTable = True, True
        shifts = []

        # O QUE APARACERÁ AO USÚARIO
        for i in range(3):
            os.system("clear")
            showCardsPlayer(table, handPlayer, showOnePlayer, showTwoPlayer, showThreePlayer)
            showCardsOpponent(table, handPlayer, showOneOpponent, showTwoOpponent, showThreeOpponent)
            showVira(table, vira, True)
            showTable(table)
            print("{:>7}: {} {:>61}: {}" .format("Player", pointsPlayer, "Oponente", pointsOpponent))
            esc = int(getch.getch())
            if esc == 1:
                showOnePlayer = False
                n = random.randint(0, len(cardEsc)-1)
                if (cardEsc[n] == 0):
                    showOneOpponent = False
                elif (cardEsc[n] == 1):
                    showTwoOpponent = False
                elif (cardEsc[n] == 2):
                    showThreeOpponent = False
            elif esc == 2:
                showTwoPlayer = False
                n = random.randint(0, len(cardEsc)-1)
                if (cardEsc[n] == 0):
                    showOneOpponent = False
                elif (cardEsc[n] == 1):
                    showTwoOpponent = False
                elif (cardEsc[n] == 2):
                    showThreeOpponent = False
            elif esc == 3:
                showThreePlayer = False
                n = random.randint(0, len(cardEsc)-1)
                if (cardEsc[n] == 0):
                    showOneOpponent = False
                elif (cardEsc[n] == 1):
                    showTwoOpponent = False
                elif (cardEsc[n] == 2):
                    showThreeOpponent = False
            os.system("clear")
            showCardsPlayer(table, handPlayer, showOnePlayer, showTwoPlayer, showThreePlayer)
            showCardsOpponent(table, handPlayer, showOneOpponent, showTwoOpponent, showThreeOpponent)
            showVira(table, vira, True)
            showCardPlayerInTable(handPlayer[esc-1], table, showPlayerCardInTable)
            showCardOpponentInTable(handOpponent[cardEsc[n]], table, showOpponentCardInTable)
            showTable(table)
            winner = checkWinPlayerTurn(vira, handPlayer[esc-1], handOpponent[cardEsc[n]])
            del cardEsc[n]
            if (winner == "player"):
                shifts.append("player")
            elif (winner == "opponent"):
                shifts.append("opponent")
            elif (winner == "draw"):
                if (i == 0):
                    shifts.append("draw")
                else:
                    if (shifts[0] == "player"):
                        pointsPlayer += 1
                        break
                    elif (shifts[0] == "opponent"):
                        pointsOpponent += 1
                        break
            if shifts.count("player") == 2:
                pointsPlayer += 1
                break
            if shifts.count("opponent") == 2:
                pointsOpponent += 1
                break


        time.sleep(2)

main()
