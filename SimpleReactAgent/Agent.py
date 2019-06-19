from SimpleReactAgent.PosXY import PosXY


class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.maze.set_agent(self)
        self.pos = PosXY(0, 0)
        self.movement = 0
        self.stack = 0

    def move(self):
        if self.stack >= 4:
            return
        next_movement = self.return_move()
        value = self.maze.get_pos_maze(next_movement)
        self.do_move(value, next_movement)

    def increase_stack(self):
        self.stack += 1

    def do_move(self, value, nmove):
        if value == "C" or value == "*":
            self.next_move()
            self.increase_stack()
            self.move()
        else:
            self.maze.clean()
            self.pos = nmove

    def next_move(self):
        if 0 == self.movement:
            self.movement = 1
        elif 1 == self.movement:
            self.movement = 2
        elif 2 == self.movement:
            self.movement = 3
        elif 3 == self.movement:
            self.movement = 0

    def get_pos(self):
        return self.pos

    def return_move(self):
        pox = self.pos.x
        poy = self.pos.y

        if 0 == self.movement:
            if self.pos.x > 0:
                pox -= 1
        elif 1 == self.movement:
            if self.pos.x < self.maze.maze_len-1:
                pox += 1
        elif 2 == self.movement:
            if self.pos.y > 0:
                poy -= 1
        elif 3 == self.movement:
            if self.pos.y < self.maze.maze_len-1:
                poy += 1

        return PosXY(pox, poy)

    def is_cleaning(self):
        return self.stack < 4

    def do_empty(self):
        self.stack = 0


