from src.headers import *
import sys

rows = 15
cols = 121
grid = np.zeros((rows, cols), dtype = int)

class Queen:

    def __init__(self, name, point1, point2, x, y, z):
        # setting up the name and dimensions of the village
        self.name = name
        self.x_coordinate = point1
        self.y_coordinate = point2
        self.damage = x 
        self.health = y
        self.movement_speed = z
    
    def show_Health(self, i, total, text):
        size = 100
        j = i/total
        sys.stdout.write('\r')
        if(self.health>=500):
            sys.stdout.write(f"{Back.GREEN}[{'=' * int(size * j):{size}s}] {int(100 * j)}%  {text}")
        elif(self.health>=200 and self.health<500):
            sys.stdout.write(f"{Back.YELLOW}[{'=' * int(size * j):{size}s}] {int(100 * j)}%  {text}")
        elif(self.health>0) :
            sys.stdout.write(f"{Back.RED}[{'=' * int(size * j):{size}s}] {int(100 * j)}%  {text}")
        elif(self.health==0) :
            sys.stdout.write(f"{Back.LIGHTWHITE_EX + Fore.BLACK}THE QUEEN IS DEAD, LONG LIVE THE QUEEN")
        sys.stdout.flush()