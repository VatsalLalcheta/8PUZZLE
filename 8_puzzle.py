import copy

def getInvCount(State):
    invCount = 0
    global rows
    for i in range(rows):
        for j in range(rows):
            if State[i][j] != '-' and State[j][i] != '-':
                if 0 < int(State[i][j]) < int(State[j][i]):
                    invCount += 1

    return invCount


def isSolvable(State):
    invCount = getInvCount(State)

    return invCount % 2 == 0


def makeCopy(State):
    Copied = []
    for i in State:
        Copied.append(copy.copy(i))
    return Copied


def CalculatePossibleMoves(index):
    PossibleMoves = []
    rowIndex = index[0]
    colIndex = index[1]
    if rowIndex - 1 >= 0:
        PossibleMoves.append('UP')
    if rowIndex + 1 <= 2:
        PossibleMoves.append('DOWN')
    if colIndex - 1 >= 0:
        PossibleMoves.append('LEFT')
    if colIndex + 1 <= 2:
        PossibleMoves.append('RIGHT')

    return PossibleMoves


def FindIndex(x, State):
    for i in range(len(State)):
        for j in range(len(State[i])):
            if State[i][j] == x:
                return (i, j)


def CalculateMissPlaced(Start_state, Final_state):
    missplaced = 0
    for i in range(len(Start_state)):
        for j in range(len(Start_state[i])):
            index = FindIndex(Start_state[i][j], Final_state)
            if index[0] != i or index[1] != j:
                missplaced += 1
    return missplaced


def main():
    Start_state = []

    Final_state = [['1', '2', '3'],
                   ['4', '5', '6'],
                   ['7', '8', '-']]

    global rows
    rows = len(Final_state)

    print("Enter the starting state in the format of 2D Matrix")

    for i in range(rows):
        Start_state.append(input().split(" "))

    if isSolvable(Start_state):

        missplaced_tiles = CalculateMissPlaced(Start_state, Final_state)
        previous_move = 'NO_MOVES_SO_FAR'

        while missplaced_tiles != 0:
            index_of_blank = FindIndex('-', Start_state)
            PossibleMoves = CalculatePossibleMoves(index_of_blank)

            for i in range(len(Start_state)):
                if i == 0:
                    print(previous_move + " --> ", end="")
                spaces = " " * len(previous_move + " --> ")
                if i != 0:
                    print(spaces, end="")
                for j in range(len(Start_state[i])):
                    print(Start_state[i][j] + " ", end="")
                print()

            print()

            rowIndex = index_of_blank[0]
            colIndex = index_of_blank[1]

            if previous_move == 'UP':
                PossibleMoves.remove('DOWN')
            if previous_move == 'DOWN':
                PossibleMoves.remove('UP')
            if previous_move == 'RIGHT':
                PossibleMoves.remove('LEFT')
            if previous_move == 'LEFT':
                PossibleMoves.remove('RIGHT')

            for i in PossibleMoves:
                if i == 'UP':
                    TempState = makeCopy(Start_state)
                    TempState[rowIndex][colIndex], TempState[rowIndex - 1][colIndex] = TempState[rowIndex - 1][
                                                                                           colIndex], \
                                                                                       TempState[rowIndex][colIndex]
                    if CalculateMissPlaced(TempState, Final_state) < missplaced_tiles:
                        missplaced_tiles = CalculateMissPlaced(TempState, Final_state)
                        previous_move = 'UP'

                if i == 'DOWN':
                    TempState = makeCopy(Start_state)
                    TempState[rowIndex][colIndex], TempState[rowIndex + 1][colIndex] = TempState[rowIndex + 1][
                                                                                           colIndex], \
                                                                                       TempState[rowIndex][colIndex]
                    if CalculateMissPlaced(TempState, Final_state) < missplaced_tiles:
                        missplaced_tiles = CalculateMissPlaced(TempState, Final_state)
                        previous_move = 'DOWN'

                if i == 'LEFT':
                    TempState = makeCopy(Start_state)
                    TempState[rowIndex][colIndex], TempState[rowIndex][colIndex - 1] = TempState[rowIndex][
                                                                                           colIndex - 1], \
                                                                                       TempState[rowIndex][colIndex]
                    if CalculateMissPlaced(TempState, Final_state) < missplaced_tiles:
                        missplaced_tiles = CalculateMissPlaced(TempState, Final_state)
                        previous_move = 'LEFT'

                if i == 'RIGHT':
                    TempState = makeCopy(Start_state)
                    TempState[rowIndex][colIndex], TempState[rowIndex][colIndex + 1] = TempState[rowIndex][
                                                                                           colIndex + 1], \
                                                                                       TempState[rowIndex][colIndex]
                    if CalculateMissPlaced(TempState, Final_state) < missplaced_tiles:
                        missplaced_tiles = CalculateMissPlaced(TempState, Final_state)
                        previous_move = 'RIGHT'

            if previous_move == 'UP':
                Start_state[rowIndex][colIndex], Start_state[rowIndex - 1][colIndex] = Start_state[rowIndex - 1][
                                                                                           colIndex], \
                                                                                       Start_state[rowIndex][colIndex]

            if previous_move == 'DOWN':
                Start_state[rowIndex][colIndex], Start_state[rowIndex + 1][colIndex] = Start_state[rowIndex + 1][
                                                                                           colIndex], \
                                                                                       Start_state[rowIndex][colIndex]

            if previous_move == 'LEFT':
                Start_state[rowIndex][colIndex], Start_state[rowIndex][colIndex - 1] = Start_state[rowIndex][
                                                                                           colIndex - 1], \
                                                                                       Start_state[rowIndex][colIndex]

            if previous_move == 'RIGHT':
                Start_state[rowIndex][colIndex], Start_state[rowIndex][colIndex + 1] = Start_state[rowIndex][
                                                                                           colIndex + 1], \
                                                                                       Start_state[rowIndex][colIndex]
        for i in range(len(Start_state)):
            if i == 0:
                print(previous_move + " --> ", end="")
            spaces = " " * len(previous_move + " --> ")
            if i != 0:
                print(spaces, end="")
            for j in range(len(Start_state[i])):
                print(Start_state[i][j] + " ", end="")
            print()



    else:
        print("The given puzzle is not solvable")


if __name__ == '__main__':
    rows = 0
    main()
