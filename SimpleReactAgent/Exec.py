from SimpleReactAgent.Agent import Agent
from SimpleReactAgent.Maze import Maze
import time

m = Maze(3)
print(m)

a = Agent(m)

while a.is_cleaning():
    a.do_empty()
    a.move()
    print(m)
    time.sleep(1.5)
