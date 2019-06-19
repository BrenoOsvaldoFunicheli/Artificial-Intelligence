from random import randint


class Maze:

    def __init__(self, mlen=2):
        """
        :type mlen: valor da matriz que será utilizada para constui a matrix
        """
        self.maze_len = mlen
        self.maze = []
        self.agent = None
        # There is method for call function that was declared before of function
        self.init_maze()

    def init_maze(self):
        """
        :argument:This Function Implements the init of matrix of maze
        """
        for i in range(0, self.maze_len):
            line = []
            for j in range(0, self.maze_len):
                line.append("D")
            self.maze.append(line)

    @staticmethod
    def random_value(value):
        """
        :param value: It's param for server of control for translate of number to valid states of maze
        :return: return a consistent state
        """
        if value == 0:
            return 'C'
        elif value > 0:
            return 'D'

    def __str__(self):
        self.update_pos()
        value =""
        for i in self.maze:
            for j in i:
                value += "|"+j+"|"
            value +="\n"

        return value

    def get_pos_maze(self, movent):
        return self.maze[movent.x][movent.y]

    def set_agent(self, agent):
        self.agent = agent

    def update_pos(self):
        if self.agent is not None:
            pos_agen = self.agent.pos
            self.maze[pos_agen.x][pos_agen.y] = "*"

    def clean(self):
        pos = self.agent.get_pos()
        self.maze[pos.x][pos.y] = "C"

    # @property
    # def maze_len(self):
    #     return self.maze_len
    #
    # @maze_len.setter
    # def maze_len(self, nlen):
    #     self.maze_len = nlen


if __name__ == '__main__':
    m = Maze(3)
    print(m)
