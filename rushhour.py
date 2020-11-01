import sys
import random
import copy
import time
import queue

responseList2 = []
responseList = []

standardboard = "  o aa|  o   |xxo   |ppp  q|     q|     q"


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.gameState = []

    def cloneState(self):
        return copy.deepcopy(self)

    def createBoard(self, boardinString):
        array = boardinString.split("|")
        if array:
            array.insert(0, " ")
            array.insert(len(array) + 1, " ")
            temp = len(array)
            for i in range(len(array) - 2):
                if ("xx" in array[i + 1]):
                    for j in range(len(array[i + 1])):
                        array[0] = array[0] + "-"
                        array[temp - 1] = array[temp - 1] + "-"
                    array[0] = array[0] + " "
                    array[temp - 1] = array[temp - 1] + " "
                    array[i + 1] = "|" + array[i + 1] + "*"
                else:
                    array[i + 1] = "|" + array[i + 1] + "|"
            self.width = len(array[0])
            self.height = len(array)
            # print(array)
            for i in range(len(array)):
                chars = []
                for c in array[i]:
                    chars.append(c)
                self.gameState.insert(i, chars)
        return self.gameState

    def printBoardFromString(self, boardinString):
        board = self.createBoard(boardinString)
        # self.printBoard()
        # print(self.gameState)

    def printBoard(self):
        for i in range(len(self.gameState)):
            for j in range(len(self.gameState[i])):
                if '*' in self.gameState[i][j]:
                    print(" ", end='')
                else:
                    print(self.gameState[i][j], end='')
            print()

    def done(self, goal):
        if goal is None:
            print(False)
        else:
            if goal == " oaa | o | o xx| pppq| q| q":
                print(True)

    def isNotCar(self, str):
        if str == ' ' or str == '|' or str == '-' or str == '*':
            return True
        else:
            return False

    def movecar(self, clone, car, direction):
        if ('l' in direction):
            for i in range(1, len(clone.gameState) - 2):
                for j in range(1, len(clone.gameState[1]) - 1):

                    if clone.gameState[i][j] == car:

                        if direction == 'l':
                            clone.gameState[i][j - 1] = car
                            clone.gameState[i][j] = car
                            clone.gameState[i][j + 1] = ' '
                            if ((j + 2 < len(clone.gameState[i])) and (clone.gameState[i][j + 2] == car)):
                                clone.gameState[i][j + 1] = car;
                                clone.gameState[i][j + 2] = ' '
                        elif direction == 'll':
                            clone.gameState[i][j - 2] = car;
                            clone.gameState[i][j - 1] = car
                            clone.gameState[i][j] = ' '
                            clone.gameState[i][j + 1] = ' '
                            if ((j + 2 < len(clone.gameState[i])) and (clone.gameState[i][j + 2] == car)):
                                clone.gameState[i][j] = car;
                                clone.gameState[i][j + 2] = ' '
                        elif direction == 'lll':
                            clone.gameState[i][j - 3] = car;
                            clone.gameState[i][j - 2] = car;
                            clone.gameState[i][j - 1] = ' ';
                            clone.gameState[i][j] = ' '
                            clone.gameState[i][j + 1] = ' '
                            if ((j + 2 < len(clone.gameState[i])) and (clone.gameState[i][j + 2] == car)):
                                clone.gameState[i][j - 1] = car;
                                clone.gameState[i][j + 2] = ' '
        elif ('u' in direction):
            for i in range(2, len(clone.gameState) - 2):
                for j in range(1, len(clone.gameState[1]) - 1):

                    if clone.gameState[i][j] == car:
                        if direction == 'u':
                            clone.gameState[i - 1][j] = car
                            clone.gameState[i][j] = car
                            clone.gameState[i + 1][j] = ' '
                            if ((i + 2 < len(clone.gameState)) and (clone.gameState[i + 2][j] == car)):
                                clone.gameState[i + 1][j] = car;
                                clone.gameState[i + 2][j] = ' '
                        elif direction == 'uu':
                            clone.gameState[i - 2][j] = car;
                            clone.gameState[i - 1][j] = car
                            clone.gameState[i][j] = ' '
                            clone.gameState[i + 1][j] = ' '
                            if ((i + 2 < len(clone.gameState)) and (clone.gameState[i + 2][j] == car)):
                                clone.gameState[i][j] = car;
                                clone.gameState[i + 2][j] = ' '
                        elif direction == 'uuu':
                            clone.gameState[i - 3][j] = car;
                            clone.gameState[i - 2][j] = car;
                            clone.gameState[i - 1][j] = ' ';
                            clone.gameState[i][j] = ' '
                            clone.gameState[i + 1][j] = ' '
                            if ((i + 2 < len(clone.gameState)) and (clone.gameState[i + 2][j] == car)):
                                clone.gameState[i - 1][j] = car;
                                clone.gameState[i + 2][j] = ' '
        elif ('r' in direction):
            for i in range(1, len(clone.gameState) - 2):

                j = len(clone.gameState[i]) - 2

                while j > 1:
                    if clone.gameState[i][j] == car:
                        if direction == 'r':
                            clone.gameState[i][j + 1] = car;
                            clone.gameState[i][j - 1] = ' '
                            if ((j - 2 > 0) and clone.gameState[i][j - 2] == car):
                                clone.gameState[i][j - 1] = car;
                                clone.gameState[i][j - 2] = ' '
                        elif direction == 'rr':
                            clone.gameState[i][j + 2] = car;
                            clone.gameState[i][j + 1] = car;
                            clone.gameState[i][j] = ' ';
                            clone.gameState[i][j - 1] = ' '
                            if ((j - 2 > 0) and clone.gameState[i][j - 2] == car):
                                clone.gameState[i][j] = car;
                                clone.gameState[i][j - 2] = ' '
                        elif direction == 'rrr':
                            clone.gameState[i][j + 3] = car;
                            clone.gameState[i][j + 2] = car;
                            clone.gameState[i][j + 1] = ' '
                            clone.gameState[i][j] = ' '
                            clone.gameState[i][j - 1] = ' '
                            if ((j - 2 > 0) and clone.gameState[i][j - 2] == car):
                                clone.gameState[i][j + 1] = car;
                                clone.gameState[i][j - 2] = ' '

                    j = j - 1

        elif ('d' in direction):
            i = len(clone.gameState) - 1
            while i > 1:
                j = len(clone.gameState[i]) - 2

                while j > 1:
                    if clone.gameState[i][j] == car:
                        if direction == 'd':
                            clone.gameState[i + 1][j] = car;
                            clone.gameState[i][j] = car;
                            clone.gameState[i - 1][j] = ' '
                            if ((i - 2 > 0) and clone.gameState[i - 2][j] == car):
                                clone.gameState[i - 1][j] = car;
                                clone.gameState[i - 2][j] = ' '
                        elif direction == 'dd':
                            clone.gameState[i + 2][j] = car;
                            clone.gameState[i + 1][j] = car;
                            clone.gameState[i][j] = ' ';
                            clone.gameState[i - 1][j] = ' '
                            if ((i - 2 > 0) and clone.gameState[i - 2][j] == car):
                                clone.gameState[i][j] = car;
                                clone.gameState[i - 2][j] = ' '
                        elif direction == 'ddd':
                            clone.gameState[i + 3][j] = car;
                            clone.gameState[i + 2][j] = car;
                            clone.gameState[i + 1][j] = ' '
                            clone.gameState[i][j] = ' '
                            clone.gameState[i - 1][j] = ' '
                            if ((i - 2 > 0) and clone.gameState[i - 2][j] == car):
                                clone.gameState[i + 1][j] = car;
                                clone.gameState[i - 2][j] = ' '
                    j = j - 1
                i = i - 1
        return clone.gameState

    def isDone(self):
        for i in range(len(self.gameState)):
            for j in range(len(self.gameState[i])):
                if (self.gameState[i][j] == '*' and self.gameState[i][j - 1] == 'x' and self.gameState[i][
                    j - 2] == 'x'):
                    return True
        return False

    def allPossibleMoves(self):
        cars = []
        carsPossiblemoves = []
        currentCarMoveList = []

        for i in range(1, len(self.gameState) - 1):
            for j in range(1, len(self.gameState[i]) - 1):
                car = self.gameState[i][j]
                if self.isNotCar(car):
                    continue
                else:
                    if (self.gameState[i][j] not in cars):
                        currentCarMoveList = self.next_for_car(self.gameState[i][j])
                        if len(currentCarMoveList) != 0:
                            cars.append(self.gameState[i][j])
                            carsPossiblemoves.append([self.gameState[i][j], currentCarMoveList])
        return carsPossiblemoves

    def next_for_car(self, piece):
        moveList = []
        upMove = True
        downMove = True
        leftMove = True
        rightMove = True

        for j in range(1, len(self.gameState[1]) - 1):
            for i in range(1, len(self.gameState) - 1):
                if ('l' in moveList) or leftMove == False:
                    break

                if (self.gameState[i][j] == piece) and ((j - 1 > 0) and self.gameState[i][j - 1] == ' '):
                    if self.gameState[i + 1][j] == piece:
                        leftMove == False
                        break
                    elif self.gameState[i][j + 1] == piece:
                        moveList.append('l')
                        if ((j - 2 > 0) and (self.gameState[i][j - 2] == ' ')):
                            moveList.append('ll')
                            if ((j - 3 > 0) and (self.gameState[i][j - 3] == ' ')):
                                moveList.append('lll')

        for j in range(1, len(self.gameState[1]) - 1):
            for i in range(1, len(self.gameState) - 2):
                if ('r' in moveList) or rightMove == False:
                    break

                if (self.gameState[i][j] == piece):
                    if self.gameState[i + 1][j] == piece:
                        rightMove == False
                        break
                    elif self.gameState[i][j - 1] == piece:
                        if (self.gameState[i][j + 1] == ' '):
                            moveList.append('r')
                            if ((j + 2 < len(self.gameState[1])) and (self.gameState[i][j + 2] == ' ')):
                                moveList.append('rr')
                                if ((j + 3 < len(self.gameState[1])) and (self.gameState[i][j + 3] == ' ')):
                                    moveList.append('rrr')

        for i in range(1, len(self.gameState) - 2):
            for j in range(1, len(self.gameState[1]) - 1):
                if ('u' in moveList) or upMove == False:
                    break

                if (self.gameState[i][j] == piece) and ((i - 1 > 0) and self.gameState[i - 1][j] == ' '):
                    if self.gameState[i][j + 1] == piece:
                        upMove == False
                        break
                    elif self.gameState[i + 1][j] == piece:
                        moveList.append('u')
                        if ((i - 2 > 0) and (self.gameState[i - 2][j] == ' ')):
                            moveList.append('uu')
                            if ((i - 3 > 0) and (self.gameState[i - 3][j] == ' ')):
                                moveList.append('uuu')

        for i in range(1, len(self.gameState) - 2):
            for j in range(1, len(self.gameState[1]) - 1):
                if ('d' in moveList) or downMove == False:
                    break

                if (self.gameState[i][j] == piece) and (self.gameState[i + 1][j] == ' '):
                    if self.gameState[i][j + 1] == piece:
                        downMove == False
                        break
                    elif self.gameState[i - 1][j] == piece:
                        moveList.append('d')
                        if ((i + 2 < len(self.gameState)) and (self.gameState[i + 2][j] == ' ')):
                            moveList.append('dd')
                            if ((i + 3 < len(self.gameState)) and (self.gameState[i + 3][j] == ' ')):
                                moveList.append('ddd')
        return moveList


class Node:
    def __init__(self, state):
        self.state = state
        self.parent = 0
        self.move = []
        self.depth = 0


class Move:
    def __init__(self, piece, direction):
        self.piece = piece
        self.direction = direction

    def move(self, currentPiece, currentDirection):
        self.piece = currentPiece
        self.direction = currentDirection
        return self

    def getPieceNumber(self):
        return self.piece

    def getMoveDirection(self):
        return self.direction


def movecar(clone, car, direction):
    if ('l' in direction):
        for i in range(1, len(clone.gameState) - 2):
            for j in range(1, len(clone.gameState[1]) - 1):

                if clone.gameState[i][j] == car:

                    if direction == 'l':
                        clone.gameState[i][j - 1] = car
                        clone.gameState[i][j] = car
                        clone.gameState[i][j + 1] = ' '
                        if ((j + 2 < len(clone.gameState[i])) and (clone.gameState[i][j + 2] == car)):
                            clone.gameState[i][j + 1] = car;
                            clone.gameState[i][j + 2] = ' '
                    elif direction == 'll':
                        clone.gameState[i][j - 2] = car;
                        clone.gameState[i][j - 1] = car
                        clone.gameState[i][j] = ' '
                        clone.gameState[i][j + 1] = ' '
                        if ((j + 2 < len(clone.gameState[i])) and (clone.gameState[i][j + 2] == car)):
                            clone.gameState[i][j] = car;
                            clone.gameState[i][j + 2] = ' '
                    elif direction == 'lll':
                        clone.gameState[i][j - 3] = car;
                        clone.gameState[i][j - 2] = car;
                        clone.gameState[i][j - 1] = ' ';
                        clone.gameState[i][j] = ' '
                        clone.gameState[i][j + 1] = ' '
                        if ((j + 2 < len(clone.gameState[i])) and (clone.gameState[i][j + 2] == car)):
                            clone.gameState[i][j - 1] = car;
                            clone.gameState[i][j + 2] = ' '
    elif ('u' in direction):
        for i in range(2, len(clone.gameState) - 2):
            for j in range(1, len(clone.gameState[1]) - 1):

                if clone.gameState[i][j] == car:
                    if direction == 'u':
                        clone.gameState[i - 1][j] = car
                        clone.gameState[i][j] = car
                        clone.gameState[i + 1][j] = ' '
                        if ((i + 2 < len(clone.gameState)) and (clone.gameState[i + 2][j] == car)):
                            clone.gameState[i + 1][j] = car;
                            clone.gameState[i + 2][j] = ' '
                    elif direction == 'uu':
                        clone.gameState[i - 2][j] = car;
                        clone.gameState[i - 1][j] = car
                        clone.gameState[i][j] = ' '
                        clone.gameState[i + 1][j] = ' '
                        if ((i + 2 < len(clone.gameState)) and (clone.gameState[i + 2][j] == car)):
                            clone.gameState[i][j] = car;
                            clone.gameState[i + 2][j] = ' '
                    elif direction == 'uuu':
                        clone.gameState[i - 3][j] = car;
                        clone.gameState[i - 2][j] = car;
                        clone.gameState[i - 1][j] = ' ';
                        clone.gameState[i][j] = ' '
                        clone.gameState[i + 1][j] = ' '
                        if ((i + 2 < len(clone.gameState)) and (clone.gameState[i + 2][j] == car)):
                            clone.gameState[i - 1][j] = car;
                            clone.gameState[i + 2][j] = ' '
    elif ('r' in direction):
        for i in range(1, len(clone.gameState) - 2):

            j = len(clone.gameState[i]) - 2

            while j > 1:
                if clone.gameState[i][j] == car:
                    if direction == 'r':
                        clone.gameState[i][j + 1] = car;
                        clone.gameState[i][j - 1] = ' '
                        if ((j - 2 > 0) and clone.gameState[i][j - 2] == car):
                            clone.gameState[i][j - 1] = car;
                            clone.gameState[i][j - 2] = ' '
                    elif direction == 'rr':
                        clone.gameState[i][j + 2] = car;
                        clone.gameState[i][j + 1] = car;
                        clone.gameState[i][j] = ' ';
                        clone.gameState[i][j - 1] = ' '
                        if ((j - 2 > 0) and clone.gameState[i][j - 2] == car):
                            clone.gameState[i][j] = car;
                            clone.gameState[i][j - 2] = ' '
                    elif direction == 'rrr':
                        clone.gameState[i][j + 3] = car;
                        clone.gameState[i][j + 2] = car;
                        clone.gameState[i][j + 1] = ' '
                        clone.gameState[i][j] = ' '
                        clone.gameState[i][j - 1] = ' '
                        if ((j - 2 > 0) and clone.gameState[i][j - 2] == car):
                            clone.gameState[i][j + 1] = car;
                            clone.gameState[i][j - 2] = ' '

                j = j - 1

    elif ('d' in direction):
        i = len(clone.gameState) - 1
        while i > 1:
            j = len(clone.gameState[i]) - 2

            while j > 1:
                if clone.gameState[i][j] == car:
                    if direction == 'd':
                        clone.gameState[i + 1][j] = car;
                        clone.gameState[i][j] = car;
                        clone.gameState[i - 1][j] = ' '
                        if ((i - 2 > 0) and clone.gameState[i - 2][j] == car):
                            clone.gameState[i - 1][j] = car;
                            clone.gameState[i - 2][j] = ' '
                    elif direction == 'dd':
                        clone.gameState[i + 2][j] = car;
                        clone.gameState[i + 1][j] = car;
                        clone.gameState[i][j] = ' ';
                        clone.gameState[i - 1][j] = ' '
                        if ((i - 2 > 0) and clone.gameState[i - 2][j] == car):
                            clone.gameState[i][j] = car;
                            clone.gameState[i - 2][j] = ' '
                    elif direction == 'ddd':
                        clone.gameState[i + 3][j] = car;
                        clone.gameState[i + 2][j] = car;
                        clone.gameState[i + 1][j] = ' '
                        clone.gameState[i][j] = ' '
                        clone.gameState[i - 1][j] = ' '
                        if ((i - 2 > 0) and clone.gameState[i - 2][j] == car):
                            clone.gameState[i + 1][j] = car;
                            clone.gameState[i - 2][j] = ' '
                j = j - 1
            i = i - 1
    return clone


def randomwalk(str):
    # self.printBoardFromString(boardinString)
    printablearray = []
    startTime = time.time()
    b = Board(0, 0)
    b.createBoard(str)
    clone = copy.deepcopy(b)
    for i in range(500):
        allPossibleMoves2 = clone.allPossibleMoves()
        # print(allPossibleMoves2)
        carIdx = random.randint(0, len(allPossibleMoves2) - 1)
        directionIdx = random.randint(0, len(allPossibleMoves2[carIdx][1]) - 1)
        # print(allPossibleMoves2[carIdx][0] + "------>" + allPossibleMoves2[carIdx][1][directionIdx])
        updated = movecar(clone, allPossibleMoves2[carIdx][0], allPossibleMoves2[carIdx][1][directionIdx])
        printablearray.append(copy.deepcopy(updated))
        if updated.isDone():
            print('finished')
            stopTime = time.time()
            print("Search time: %.4fs" % (stopTime - startTime))
            break
    printArray(printablearray)


def done(str):
    board = Board(0, 0)
    board.createBoard(str)

    return board.isDone()


# Implement applyMove but for a cloned game state
def applyMoveCloning(currentState, nextMove):
    newState = currentState.cloneState()
    # print("car" + nextMove.getPieceNumber() + "direction " + nextMove.getMoveDirection())
    return movecar(newState, nextMove.getPieceNumber(), nextMove.getMoveDirection())


def next(Str):
    b = Board(0, 0)
    b.createBoard(Str)
    allPossibleMoves2 = b.allPossibleMoves()
    # print(allPossibleMoves2)
    printablearray = []
    # clone = copy.deepcopy(b)
    for i in range(len(allPossibleMoves2)):
        for j in range(len(allPossibleMoves2[i][1])):
            clone = copy.deepcopy(b)
            # print(allPossibleMoves2[i][0])
            # print(allPossibleMoves2[i][1][j])
            updated = movecar(clone, allPossibleMoves2[i][0], allPossibleMoves2[i][1][j])
            printablearray.append(updated)
            # clone.printBoard()

    printArray(printablearray)




def breadthFirst(state, nextMove):
    clone = copy.deepcopy(state)
    rootNode = Node(state)
    bfs_Queue = queue.Queue()
    bfs_Queue.put(rootNode)
    graphTraversed = False
    visitedStates = []
    visitedStates.append(rootNode.state.gameState)
    nodeCount = 0

    while not graphTraversed:
        currentNode = bfs_Queue.get()
        nodeCount += 1
        if currentNode.state.isDone():
            path = [currentNode.move]
            parentNode = currentNode.parent
            while parentNode.move:
                path.append(parentNode.move)
                parentNode = parentNode.parent
            path.reverse()
            for node in path:
                # print ("(%s,%s)" % (node[0], node[1]))
                updated = movecar(clone, node[0], node[1])
                responseList2.append(copy.deepcopy(updated))
            # currentNode.state.printBoard()
            return len(path), nodeCount
        nextStates = []
        currentPossibleMoves = []
        for move in currentNode.state.allPossibleMoves():
            for direction in move[1]:
                possibleState = applyMoveCloning(currentNode.state, nextMove.move(move[0], direction))
                nextStates.append(possibleState)
                currentPossibleMoves.append([move[0], direction])
        for nextState in nextStates:
            if (nextState.gameState not in visitedStates):
                visitedStates.append(nextState.gameState)
                nextNode = Node(nextState)
                nextNode.parent = currentNode
                nextNode.move = currentPossibleMoves[nextStates.index(nextState)]
                nextNode.depth = nextNode.parent.depth + 1
                bfs_Queue.put(nextNode)
                responseList.append(copy.deepcopy(nextNode.state))


def printArray(arr):
    # print(len(arr), len(arr)//6, len(arr)%6)

    if len(arr) // 6 != 0:
        for x in range(len(arr) // 6):
            for i in range(len(arr[0].gameState)):
                for j in range(6):
                    if '*' in arr[j + x * 6].gameState[i]:
                        index = arr[j + x * 6].gameState[i].index("*")
                        arr[j + x * 6].gameState[i][index] = ' '

                    # print(arr[j+x*6].gameState[i], end= ' ')
                    print(''.join(arr[j + x * 6].gameState[i]), end=' ')
                print()

    if len(arr) % 6 != 0:
        for i in range(len(arr[0].gameState)):
            for j in range(len(arr) % 6):
                if '*' in arr[j + len(arr) // 6 * 6].gameState[i]:
                    index = arr[j + len(arr) // 6 * 6].gameState[i].index("*")
                    arr[j + len(arr) // 6 * 6].gameState[i][index] = ' '
                print(''.join(arr[j + len(arr) // 6 * 6].gameState[i]), end=' ')
            print()

    print()


def bfs(str):
    b = Board(0, 0)
    b.createBoard(str)
    move = Move(0, 0)
    print("BFS Strategy")
    startTime = time.time()
    numMovesBFS, numNodesBFS = breadthFirst(b, move)
    stopTime = time.time()
    print("Number of nodes visited: %d" % numNodesBFS)
    print("Search time: %.4fs" % (stopTime - startTime))
    print("Length of solution: %d" % numMovesBFS)
    print('****************************************************************************************************')
    printArray(responseList2)
    print('****************************************************************************************************')
    printArray(responseList)


def aster(str):
    b = Board(0, 0)
    b.createBoard(str)
    move = Move(0, 0)
    print(" Aster search starting")
    startTime = time.time()
    moves = asterSearch(b, move)
    print(moves)
    stopTime = time.time()
    print("Aster search completed ")
    print("Search time: %.4fs" % (stopTime - startTime))


def heuristic(b):
    # calcuate distance between the xx car and the exit gate.
    return 3


def asterSearch(b, move):
    b.width = 0;
    b.height = heuristic(b)
    OPEN = [b]
    CLOSED = []
    moves = []
    while len(OPEN) > 0:
        N = OPEN.pop()
        if N.isDone():
            return moves
        CLOSED.append(N)


def asterSearchPsudoCode(b, move):
    b.width = 0;
    b.height = heuristic(b)
    OPEN = [b]
    CLOSED = []
    moves = []
    queue = {}
    while len(OPEN) > 0:
        N = OPEN.pop()
        if N.isDone():
            return moves
        CLOSED.append(N)
    for best_boards in find_best_boards(queue):
        for best_board in best_boards:
            next_boards = best_board.allPossibleMoves2
            for move in next_boards:
                value = move
                if value not in queue:
                    queue[value] = [move]
                else:
                    queue[value].append(move)


def find_best_boards():
    minimum = min(queue.keys(), key=int)
    best_boards = queue[minimum]
    states_count = len(best_boards)
    del queue[minimum]
    return best_boards


def main():
    argList = sys.argv
    b = Board(0, 0)
    if len(argList) == 2:
        if argList[1] == "print":
            b.createBoard(standardboard)
            b.printBoard()
        elif argList[1] == "done":
            print(done(standardboard))
        elif argList[1] == "next":
            next(standardboard)
        elif argList[1] == 'random':
            randomwalk(standardboard)
        elif argList[1] == 'bfs':
            bfs(standardboard)
        else:
            aster(standardboard)
    elif len(argList) == 3:
        if argList[1] == "print":
            b.createBoard(argList[2])
            b.printBoard()
        elif argList[1] == "done":
            print(done(argList[2]))
        elif argList[1] == "next":
            next(argList[2])
        elif argList[1] == "random":
            randomwalk(argList[2])
        elif argList[1] == 'bfs':
            bfs(argList[2])
        else:
            aster(argList[2])


if __name__ == "__main__":
    main()