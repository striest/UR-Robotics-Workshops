import random

class Maze:
    '''
    Maze class for UR Robotics coding workshop
    Start in square 1 ([0][0]). Goal is to navigate to square n^2([n][n]). Essentially, get from top left to bottom right
    '''

    def __init__(self, n):
        self.grid = list()
        self.N = n
        for i in range(n):
            self.grid.append(list())
        for i in range(n):
            for j in range(n):
                self.grid[i].append([False, False, False, False])

            #representing adjacencies as four bools (True=next cell reachable)
            #[Up, Down, Left, Right]

    def maze_gen(self):
        # union-find: keep removing walls and add pointers in data structure until square [0] and [n^2] are in the same set.
        sets = list()
        for i in range(self.N):
            sets.append(list())
            for j in range(self.N):
                sets[i].append((i, j))

        while not self.same_set(0, 0, self.N - 1, self.N - 1, sets):
            # for i in sets:
            #     for j in i:
            #         print(j, end='')
            #     print()
            # print()
            d_i = random.randint(0, self.N-1)
            d_j = random.randint(0, self.N-1)
            d_w = [0, 1, 2, 3]
            #check edges
            if d_i == 0: #i=0 -> no up
                d_w.remove(0)
            if d_i == self.N - 1: #i=N-1 -> no down
                d_w.remove(1)
            if d_j == 0: #j=0 -> no left
                d_w.remove(2)
            if d_j == self.N - 1: #j=N-1 -> no right
                d_w.remove(3)

            if len(d_w) == 0:
                continue

            d_w = random.choice(d_w)


            #remove wall as specified
            self.grid[d_i][d_j][d_w] = True

            # update tree
            if d_w == 0: # connect up,
                sets[d_i][d_j] = (d_i-1, d_j)
                self.grid[d_i-1][d_j][1] = True
            elif d_w == 1: # connect down
                sets[d_i+1][d_j] = (d_i, d_j)
                self.grid[d_i+1][d_j][0] = True
            elif d_w == 2: # connect left
                sets[d_i][d_j] = (d_i, d_j-1)
                self.grid[d_i][d_j-1][3] = True
            elif d_w == 3: # connect right
                sets[d_i][d_j+1] = (d_i, d_j)
                self.grid[d_i][d_j+1][2] = True

    def same_set(self, i1, j1, i2, j2, arr):
        i_root = self.root_find(i1, j1, arr)
        j_root = self.root_find(i2, j2, arr)

        return i_root == j_root

    def root_find(self, i, j, arr):
        i_new, j_new = arr[i][j]
        if i == i_new and j == j_new:
            return i, j
        else:
            return self.root_find(i_new, j_new, arr)


    def dump_2(self):
        for i in self.grid:
            for j in i:
                for v in j:
                    if v:
                        print("T", end='')
                    else:
                        print("F", end='')
                print(' ', end='')
            print()

    def dump(self):
        for i in self.grid:
            top_buffer = ""
            mid_buffer = ""
            low_buffer = ""
            for j in i:
                if j[0]:
                    top_buffer += "#   #"
                else:
                    top_buffer += "#####"

                if j[1]:
                    low_buffer += "#   #"
                else:
                    low_buffer += "#####"

                if j[2] and j[3]:
                    mid_buffer += "  .  "
                elif not j[2] and j[3]:
                    mid_buffer += "# .  "
                elif j[2] and not j[3]:
                    mid_buffer += "  . #"
                else:
                    mid_buffer += "# . #"
            print(top_buffer)
            print(mid_buffer)
            print(low_buffer)

    def maze_export(self, filename):
        fh = open(filename, 'w')
        fh.write(str(self.N) + '\n')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                fh.write(str(i) + '\t' + str(j) + '\t' + str(self.grid[i][j][0]) +
                         '\t' + str(self.grid[i][j][1]) + '\t' + str(self.grid[i][j][2]) +
                         '\t' + str(self.grid[i][j][3]) + '\n')
        fh.close()

    def maze_import(self, filename):
        fh = open(filename, 'r')
        s = fh.readline()
        n = int(s)
        self.N = n
        self.grid = list()
        for i in range(n):
            self.grid.append(list())
        for i in range(n):
            for j in range(n):
                self.grid[i].append([False, False, False, False])

        for line in fh:
            s = line.strip('\n').split('\t')
            i = int(s[0])
            j = int(s[1])
            up = s[2]== 'True'
            down = s[3] == 'True'
            left = s[4] == 'True'
            right = s[5] == 'True'
            self.grid[i][j][0] = up
            self.grid[i][j][1] = down
            self.grid[i][j][2] = left
            self.grid[i][j][3] = right
        fh.close()


def main():
    m = Maze(15)
    m.maze_gen()
    m.maze_export("maze5.txt")
    #m.dump_2()
    #print("dlfahsldkfjhads")
    m.dump()

if __name__ == '__main__':
    main();