import maze

class MazeAgent:
    def __init__(self, m):
        self.pos = [0, 0]
        self.prev_pos = [0, 0]
        self.M = m
        self.numMoves = 0
        self.visited = set()
        self.visited.add((0, 0))

    def moveDown(self):
        self.numMoves += 1
        if self.pos[0] < self.M.N - 1 and self.canMoveDown():
            self.prev_pos = [self.pos[0], self.pos[1]]
            self.pos[0] += 1
            self.visited.add((self.pos[0], self.pos[1]))
        else:
            print("INVALID MOVE")

    def moveUp(self):
        self.numMoves += 1
        if self.pos[0] > 0 and self.canMoveUp():
            self.prev_pos = [self.pos[0], self.pos[1]]
            self.pos[0] -= 1
            self.visited.add((self.pos[0], self.pos[1]))
        else:
            print("INVALID MOVE")

    def moveLeft(self):
        self.numMoves += 1
        if self.pos[1] > 0 and self.canMoveLeft():
            self.prev_pos = [self.pos[0], self.pos[1]]
            self.pos[1] -= 1
            self.visited.add((self.pos[0], self.pos[1]))
        else:
            print("INVALID MOVE")

    def moveRight(self):
        self.numMoves += 1
        if self.pos[1] < self.M.N - 1 and self.canMoveRight():
            self.prev_pos = [self.pos[0], self.pos[1]]
            self.pos[1] += 1
            self.visited.add((self.pos[0], self.pos[1]))
        else:
            print("INVALID MOVE")

    def canMoveUp(self):
        return self.M.grid[self.pos[0]][self.pos[1]][0]

    def canMoveDown(self):
        return self.M.grid[self.pos[0]][self.pos[1]][1]

    def canMoveLeft(self):
        return self.M.grid[self.pos[0]][self.pos[1]][2]

    def canMoveRight(self):
        return self.M.grid[self.pos[0]][self.pos[1]][3]

    def visitedUp(self):
        return (self.pos[0]-1, self.pos[1]) in self.visited

    def visitedDown(self):
        return (self.pos[0]+1, self.pos[1]) in self.visited

    def visitedLeft(self):
        return (self.pos[0], self.pos[1]-1) in self.visited

    def visitedRight(self):
        return (self.pos[0], self.pos[1]+1) in self.visited

    def didNotMove(self):
        return self.pos == self.prev_pos

    def dump(self):
        for i in range(len(self.M.grid)):
            top_buffer = ""
            mid_buffer = ""
            low_buffer = ""
            for j in range(len(self.M.grid[i])):
                if self.M.grid[i][j][0]:
                    top_buffer += "#   #"
                else:
                    top_buffer += "#####"

                if self.M.grid[i][j][1]:
                    low_buffer += "#   #"
                else:
                    low_buffer += "#####"

                if i == 0 and j == 0:
                    if self.pos[0] == i and self.pos[1] == j:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  O  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# O  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  O #"
                        else:
                            mid_buffer += "# O #"
                    else:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  S  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# S  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  S #"
                        else:
                            mid_buffer += "# S #"
                elif i == self.M.N - 1 and j == self.M.N - 1:
                    if self.pos[0] == i and self.pos[1] == j:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  O  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# O  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  O #"
                        else:
                            mid_buffer += "# O #"
                    else:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  E  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# E  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  E #"
                        else:
                            mid_buffer += "# E #"
                else:
                    if self.pos[0] == i and self.pos[1] == j:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  O  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# O  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  O #"
                        else:
                            mid_buffer += "# O #"
                    else:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  .  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# .  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  . #"
                        else:
                            mid_buffer += "# . #"
            print(top_buffer)
            print(mid_buffer)
            print(low_buffer)
        print("Num Moves:", self.numMoves)

    def dump_to_file(self, filename):
        fh = open(filename, 'w')
        for i in range(len(self.M.grid)):
            top_buffer = ""
            mid_buffer = ""
            low_buffer = ""
            for j in range(len(self.M.grid[i])):
                if self.M.grid[i][j][0]:
                    top_buffer += "#   #"
                else:
                    top_buffer += "#####"

                if self.M.grid[i][j][1]:
                    low_buffer += "#   #"
                else:
                    low_buffer += "#####"

                if i == 0 and j == 0:
                    if self.pos[0] == i and self.pos[1] == j:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  O  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# O  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  O #"
                        else:
                            mid_buffer += "# O #"
                    else:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  S  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# S  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  S #"
                        else:
                            mid_buffer += "# S #"
                elif i == self.M.N - 1 and j == self.M.N - 1:
                    if self.pos[0] == i and self.pos[1] == j:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  O  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# O  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  O #"
                        else:
                            mid_buffer += "# O #"
                    else:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  E  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# E  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  E #"
                        else:
                            mid_buffer += "# E #"
                else:
                    if self.pos[0] == i and self.pos[1] == j:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  O  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# O  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  O #"
                        else:
                            mid_buffer += "# O #"
                    else:
                        if self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "  .  "
                        elif not self.M.grid[i][j][2] and self.M.grid[i][j][3]:
                            mid_buffer += "# .  "
                        elif self.M.grid[i][j][2] and not self.M.grid[i][j][3]:
                            mid_buffer += "  . #"
                        else:
                            mid_buffer += "# . #"
            fh.write(top_buffer + '\n')
            fh.write(mid_buffer + '\n')
            fh.write(low_buffer + '\n')
        print("Num Moves:", self.numMoves)

    def position(self):
        return self.pos

    def isSolved(self):
        return self.pos[0] == self.M.N - 1 and self.pos[1] == self.M.N - 1

    def move(self):
        if self.canMoveDown() and not self.visitedDown():
            self.moveDown()
        elif self.canMoveRight() and not self.visitedRight():
            self.moveRight()
        elif self.canMoveUp():
            self.moveUp()
        elif self.canMoveLeft():
            self.moveLeft()

def main():
    s = input("Evaulation mode?(Y/N)")
    if s.lower() == 'n':
        s = input("Input name of maze file:")
        M = maze.Maze(0)
        M.maze_import(s)
        agent = MazeAgent(M)
        agent.dump()
        while not agent.isSolved():
            s = input("Hit enter for next step:")
            agent.move()
            agent.dump()
    else:
        total = 0
        files = ['maze1.txt', 'maze2.txt', 'maze3.txt', 'maze4.txt', 'maze5.txt']
        for filename in files:
            M = maze.Maze(0)
            M.maze_import(filename)
            agent = MazeAgent(M)
            pos_prev = [agent.pos[0], agent.pos[1]]
            while not agent.isSolved():
                agent.move()
                if agent.pos == pos_prev:
                    print("Agent did not make forward progress on:", filename)
                    agent.dump_to_file('error.txt')
                    exit()
                if agent.numMoves > 1000:
                    print("Agent took over 1000 moves to solve on:", filename,  "(likely in infinite loop)")
                    exit()
                pos_prev = [agent.pos[0], agent.pos[1]]
            total += agent.numMoves
        print("Success! Score:", total)
        print("Optimal score is 66")

if __name__ == '__main__':
    main()
