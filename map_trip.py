import random
import time

class Map:
    def __init__(self, size=5, history = True, gold_x = 0, gold_y = 0):
        self.map = []
        self.size = size
        for i in range(size):
            temp = []
            for j in range(size):
                temp.append(".")
            self.map.append(temp)
        self.current = [0,0]
        self.map[0][0] = "|"
        self.history_flag = history
        self.history = [0,0]
        self.gold = [gold_x, gold_y]
        while self.gold[0] == 0 and self.gold[1] == 0:
            self.gold = [random.randint(0, size - 1), random.randint(0, size - 1)]
        self.map[self.gold[0]][self.gold[1]] = "+"

    def printMap(self):
        for row in range(self.size):
            for col in range(self.size):
                print(self.map[row][col], end=" ")
            print("")
        print("-------------------")

    def previousDirection(self):
        if self.history_flag:
            if self.history[1] - self.current[1] == 1:
                return "RIGHT"
            elif self.history[1] - self.current[1] == -1:
                return "LEFT"
            elif self.history[0] - self.current[0] == -1:
                return "UP"
            elif self.history[0] - self.current[0] == 1:
                return "DOWN"
            else:
                print("Invalid Direction!")
                return "NO_DIRECTION"
        else:
            return "NO_HISTORY_FLAG"

    def possiblePositions(self):
        temp = []
        previous = self.previousDirection()
        if self.current[1] > 0 and previous != "LEFT":
            temp.append("LEFT")
        if self.current[1] < self.size - 1 and previous != "RIGHT":
            temp.append("RIGHT")
        if self.current[0] > 0 and previous != "UP":
            temp.append("UP")
        if self.current[0] < self.size - 1 and previous != "DOWN":
            temp.append("DOWN")
        return temp, previous

    def move(self, direction):
        direction = str(direction).upper()
        flag = 0
        if direction == "UP":
            if self.current[0] > 0:
                self.map[self.current[0]][self.current[1]] = "."
                if self.history_flag:
                    self.history[0] = self.current[0]
                    self.history[1] = self.current[1]
                self.current[0] = self.current[0] - 1
                self.map[self.current[0]][self.current[1]] = "|"
                if self.current[0] == self.gold[0] and self.current[1] == self.gold[1]:
                    print("Found the Gold!")
                    flag = 1
            else:
                print("Invalid Move!")
        elif direction == "DOWN":
            if self.current[0] < self.size - 1:
                self.map[self.current[0]][self.current[1]] = "."
                if self.history_flag:
                    self.history[0] = self.current[0]
                    self.history[1] = self.current[1]
                self.current[0] = self.current[0] + 1
                self.map[self.current[0]][self.current[1]] = "|"
                if self.current[0] == self.gold[0] and self.current[1] == self.gold[1]:
                    print("Found the Gold!")
                    flag = 1
            else:
                print("Invalid Move!")
        elif direction == "RIGHT":
            if self.current[1] < self.size - 1:
                self.map[self.current[0]][self.current[1]] = "."
                if self.history_flag:
                    self.history[0] = self.current[0]
                    self.history[1] = self.current[1]
                self.current[1] = self.current[1] + 1
                self.map[self.current[0]][self.current[1]] = "|"
                if self.current[0] == self.gold[0] and self.current[1] == self.gold[1]:
                    print("Found the Gold!")
                    flag = 1
            else:
                print("Invalid Move!")
        elif direction == "LEFT":
            if self.current[1] > 0:
                self.map[self.current[0]][self.current[1]] = "."
                if self.history_flag:
                    self.history[0] = self.current[0]
                    self.history[1] = self.current[1]
                self.current[1] = self.current[1] - 1
                self.map[self.current[0]][self.current[1]] = "|"
                if self.current[0] == self.gold[0] and self.current[1] == self.gold[1]:
                    print("Found the Gold!")
                    flag = 1
            else:
                print("Invalid Move!")
        else:
            print("Invalid Direction!")
        return flag



map = Map(10, history=True, gold_x=0, gold_y=0)
flag = 0
from timeit import default_timer as timer
start = timer()
while flag == 0:
    moves, previous = map.possiblePositions()
    print(moves)
    print("Previous: ", previous)
    move = moves[random.randint(0, len(moves)-1)]
    print("Move: ", move)
    flag = map.move(move)
    map.printMap()
    time.sleep(1)

end = timer()
print("Time: ", end - start, " s")