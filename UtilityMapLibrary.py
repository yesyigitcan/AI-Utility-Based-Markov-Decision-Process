class UtilityMap:
    def __init__(self, map, alpha = 1, rs = -0.03):
        self.alpha = alpha
        self.rs = rs
        self.utility = []
        self.map = map
        self.rowlen = len(self.map)
        self.collen = len(self.map[0])
        for i in range(self.rowlen):
            temp = []
            for j in range(self.collen):
                temp.append(0)
            self.utility.append(temp)
            for j in range(self.collen):
                if self.map[i][j] == "+1":
                    self.utility[i][j] = 1
                elif self.map[i][j] == "-1":
                    self.utility[i][j] = -1

    def getUtilityMatrix(self, i, j):
        utility_scores = []
        # up
        temp = 0.0
        if i - 1 > -1:
            temp += 0.8 * self.utility[i - 1][j]
        if j + 1 < self.collen:
            temp += 0.1 * self.utility[i][j + 1]
        if j - 1 > -1:
            temp += 0.1 * self.utility[i][j - 1]
        utility_scores.append(temp)
        # down
        temp = 0.0
        if i + 1 < self.rowlen:
            temp += 0.8 * self.utility[i + 1][j]
        if j + 1 < self.collen:
            temp += 0.1 * self.utility[i][j + 1]
        if j - 1 > -1:
            temp += 0.1 * self.utility[i][j - 1]
        utility_scores.append(temp)
        # right
        temp = 0.0
        if j + 1 < self.collen:
            temp += 0.8 * self.utility[i][j + 1]
        if i - 1 > -1:
            temp += 0.1 * self.utility[i - 1][j]
        if i + 1 < self.rowlen:
            temp += 0.1 * self.utility[i + 1][j]
        utility_scores.append(temp)
        # left
        temp = 0.0
        if j - 1 > -1:
            temp += 0.8 * self.utility[i][j - 1]
        if i - 1 > -1:
            temp += 0.1 * self.utility[i - 1][j]
        if i + 1 < self.rowlen:
            temp += 0.1 * self.utility[i + 1][j]
        utility_scores.append(temp)
        return utility_scores

    def getUtilityCalculatedMap(self):
        utility_arrows = ["UP","DOWN","RIGHT","LEFT"]
        for i in range(self.rowlen):
            for j in range(self.collen):
                if self.map[i][j] in utility_arrows:
                    self.map[i][j] = "."

        for i in range(self.rowlen):
            for j in range(self.collen):
                j = self.collen - j - 1
                if self.map[i][j] == ".":
                    utility_matrix = self.getUtilityMatrix(i, j)
                    max_index = utility_matrix.index(max(utility_matrix))
                    self.map[i][j] = utility_arrows[max_index]
                    self.utility[i][j] = utility_matrix[max_index] + self.rs
        return self.map

    def printArrowMap(self):
        for i in range(self.rowlen):
            for j in range(self.collen):
                print(self.map[i][j], end=" ")
            print("")

    def printUtilityMap(self):
        for i in range(self.rowlen):
            for j in range(self.collen):
                print("{0:.4f}".format(self.utility[i][j]), end=" ")
            print("")




