from src.headers import *
import sys

rows = 15
cols = 121
grid = np.zeros((rows, cols), dtype = int)

class King:

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
            sys.stdout.write(f"{Back.LIGHTWHITE_EX + Fore.BLACK}THE KING IS DEAD, LONG LIVE THE KING")
        sys.stdout.flush()
        
class Barbarian(King):
    def barbarian_moves(self, new_x, new_y):
        if(new_x>=self.x_coordinate):
            if(new_y>=self.y_coordinate):
                del_x = new_x - self.x_coordinate
                del_y = new_y - self.y_coordinate
                if (del_x==0 and del_y==1) or (del_x==1 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==(rows-1)):
                        self.x_coordinate = self.x_coordinate
                    elif(grid[self.x_coordinate+self.movement_speed][self.y_coordinate]==0 or grid[self.x_coordinate+self.movement_speed][self.y_coordinate]==51) :
                        self.x_coordinate = self.x_coordinate+self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==(cols-2)):
                        self.y_coordinate = self.y_coordinate
                    elif(grid[self.x_coordinate][self.y_coordinate+(2*self.movement_speed)]==0 or grid[self.x_coordinate][self.y_coordinate+(2*self.movement_speed)]==51):
                        self.y_coordinate = self.y_coordinate+(2*self.movement_speed)
                del_x = new_x - self.x_coordinate
                del_y = new_y - self.y_coordinate
            else :
                del_x = new_x - self.x_coordinate
                del_y = self.y_coordinate - new_y

                if (del_x==0 and del_y==1) or (del_x==1 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==(rows-1)):
                        self.x_coordinate = self.x_coordinate
                    elif(grid[self.x_coordinate+self.movement_speed][self.y_coordinate]==0 or grid[self.x_coordinate+self.movement_speed][self.y_coordinate]==51) :
                        self.x_coordinate = self.x_coordinate+self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==1):
                        self.y_coordinate = self.y_coordinate
                    elif(grid[self.x_coordinate][self.y_coordinate-(2*self.movement_speed)]==0 or grid[self.x_coordinate][self.y_coordinate-(2*self.movement_speed)]==51):
                        self.y_coordinate = self.y_coordinate-(2*self.movement_speed)
                del_x = new_x - self.x_coordinate
                del_y = self.y_coordinate - new_y
                
        else :
            if(new_y>self.y_coordinate):
                del_x = self.x_coordinate - new_x
                del_y = new_y - self.y_coordinate

                if (del_x==0 and del_y==1) or (del_x==1 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==0):
                        self.x_coordinate = self.x_coordinate
                    elif(grid[self.x_coordinate-self.movement_speed][self.y_coordinate]==0 or grid[self.x_coordinate-self.movement_speed][self.y_coordinate]==51) :
                        self.x_coordinate = self.x_coordinate-self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==(cols-2)):
                        self.y_coordinate = self.y_coordinate
                    elif(grid[self.x_coordinate][self.y_coordinate+(2*self.movement_speed)]==0 or grid[self.x_coordinate][self.y_coordinate+(2*self.movement_speed)]==51):
                        self.y_coordinate = self.y_coordinate+(2*self.movement_speed)
                del_x = self.x_coordinate - new_x
                del_y = new_y - self.y_coordinate
            else :
                del_x = self.x_coordinate - new_x
                del_y = self.y_coordinate - new_y

                if (del_x==0 and del_y==1) or (del_x==1 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==0):
                        self.x_coordinate = self.x_coordinate
                    elif(grid[self.x_coordinate-self.movement_speed][self.y_coordinate]==0 or grid[self.x_coordinate-self.movement_speed][self.y_coordinate]==51) :
                        self.x_coordinate = self.x_coordinate-self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==1):
                        self.y_coordinate = self.y_coordinate
                    elif(grid[self.x_coordinate][self.y_coordinate-(2*self.movement_speed)]==0 or grid[self.x_coordinate][self.y_coordinate-(2*self.movement_speed)]==51):
                        self.y_coordinate = self.y_coordinate-(2*self.movement_speed)
                del_x = self.x_coordinate - new_x
                del_y = self.y_coordinate - new_y


class Archer(Barbarian):
    def __init__(self, name, point1, point2, x, y, z, range, attacking):
        Barbarian.__init__(self, name, point1, point2, x, y, z)
        self.damage = x/2
        self.health = y/2
        self.range = range
        self.attacking = attacking
        
        
    def archer_moves(self, new_x, new_y):
        if(new_x>=self.x_coordinate):
            if(new_y>=self.y_coordinate):
                del_x = new_x - self.x_coordinate
                del_y = new_y - self.y_coordinate
                if (del_x==0 and del_y==1) or (del_x==1 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==(rows-1)):
                        self.x_coordinate = self.x_coordinate
                    elif(grid[self.x_coordinate+self.movement_speed][self.y_coordinate]==0 or grid[self.x_coordinate+self.movement_speed][self.y_coordinate]==51) :
                        self.x_coordinate = self.x_coordinate+self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==(cols-2)):
                        self.y_coordinate = self.y_coordinate
                    elif(grid[self.x_coordinate][self.y_coordinate+(2*self.movement_speed)]==0 or grid[self.x_coordinate][self.y_coordinate+(2*self.movement_speed)]==51):
                        self.y_coordinate = self.y_coordinate+(2*self.movement_speed)
                del_x = new_x - self.x_coordinate
                del_y = new_y - self.y_coordinate
            else :
                del_x = new_x - self.x_coordinate
                del_y = self.y_coordinate - new_y

                if (del_x==0 and del_y==1) or (del_x==1 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==(rows-1)):
                        self.x_coordinate = self.x_coordinate
                    elif(grid[self.x_coordinate+self.movement_speed][self.y_coordinate]==0 or grid[self.x_coordinate+self.movement_speed][self.y_coordinate]==51) :
                        self.x_coordinate = self.x_coordinate+self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==1):
                        self.y_coordinate = self.y_coordinate
                    elif(grid[self.x_coordinate][self.y_coordinate-(2*self.movement_speed)]==0 or grid[self.x_coordinate][self.y_coordinate-(2*self.movement_speed)]==51):
                        self.y_coordinate = self.y_coordinate-(2*self.movement_speed)
                del_x = new_x - self.x_coordinate
                del_y = self.y_coordinate - new_y
                
        else :
            if(new_y>self.y_coordinate):
                del_x = self.x_coordinate - new_x
                del_y = new_y - self.y_coordinate

                if (del_x==0 and del_y==1) or (del_x==1 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==0):
                        self.x_coordinate = self.x_coordinate
                    elif(grid[self.x_coordinate-self.movement_speed][self.y_coordinate]==0 or grid[self.x_coordinate-self.movement_speed][self.y_coordinate]==51) :
                        self.x_coordinate = self.x_coordinate-self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==(cols-2)):
                        self.y_coordinate = self.y_coordinate
                    elif(grid[self.x_coordinate][self.y_coordinate+(2*self.movement_speed)]==0 or grid[self.x_coordinate][self.y_coordinate+(2*self.movement_speed)]==51):
                        self.y_coordinate = self.y_coordinate+(2*self.movement_speed)
                del_x = self.x_coordinate - new_x
                del_y = new_y - self.y_coordinate
            else :
                del_x = self.x_coordinate - new_x
                del_y = self.y_coordinate - new_y

                if (del_x==0 and del_y==1) or (del_x==1 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==0):
                        self.x_coordinate = self.x_coordinate
                    elif(grid[self.x_coordinate-self.movement_speed][self.y_coordinate]==0 or grid[self.x_coordinate-self.movement_speed][self.y_coordinate]==51) :
                        self.x_coordinate = self.x_coordinate-self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==1):
                        self.y_coordinate = self.y_coordinate
                    elif(grid[self.x_coordinate][self.y_coordinate-(2*self.movement_speed)]==0 or grid[self.x_coordinate][self.y_coordinate-(2*self.movement_speed)]==51):
                        self.y_coordinate = self.y_coordinate-(2*self.movement_speed)
                del_x = self.x_coordinate - new_x
                del_y = self.y_coordinate - new_y
                
class Balloon(King):
    
    def balloon_moves(self, new_x, new_y):
        if(new_x>=self.x_coordinate):
            if(new_y>=self.y_coordinate):
                del_x = new_x - self.x_coordinate
                del_y = new_y - self.y_coordinate
                if (del_x==0 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==(rows-1)):
                        self.x_coordinate = self.x_coordinate
                    else:
                        self.x_coordinate = self.x_coordinate+self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==(cols-2)):
                        self.y_coordinate = self.y_coordinate
                    else:
                        self.y_coordinate = self.y_coordinate+(2*self.movement_speed)
                del_x = new_x - self.x_coordinate
                del_y = new_y - self.y_coordinate
            else :
                del_x = new_x - self.x_coordinate
                del_y = self.y_coordinate - new_y

                if (del_x==0 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==(rows-1)):
                        self.x_coordinate = self.x_coordinate
                    else:
                        self.x_coordinate = self.x_coordinate+self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==1):
                        self.y_coordinate = self.y_coordinate
                    else:
                        self.y_coordinate = self.y_coordinate-(2*self.movement_speed)
                del_x = new_x - self.x_coordinate
                del_y = self.y_coordinate - new_y
                
        else :
            if(new_y>self.y_coordinate):
                del_x = self.x_coordinate - new_x
                del_y = new_y - self.y_coordinate

                if (del_x==0 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==0):
                        self.x_coordinate = self.x_coordinate
                    else:
                        self.x_coordinate = self.x_coordinate-self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==(cols-2)):
                        self.y_coordinate = self.y_coordinate
                    else:
                        self.y_coordinate = self.y_coordinate+(2*self.movement_speed)
                del_x = self.x_coordinate - new_x
                del_y = new_y - self.y_coordinate
            else :
                del_x = self.x_coordinate - new_x
                del_y = self.y_coordinate - new_y

                if (del_x==0 and del_y==0):
                    self.x_coordinate = self.x_coordinate
                    self.y_coordinate = self.y_coordinate
                elif(del_x!=0):
                    if(self.x_coordinate==0):
                        self.x_coordinate = self.x_coordinate
                    else:
                        self.x_coordinate = self.x_coordinate-self.movement_speed
                elif(del_y!=0):
                    if(self.y_coordinate==1):
                        self.y_coordinate = self.y_coordinate
                    else:
                        self.y_coordinate = self.y_coordinate-(2*self.movement_speed)
                del_x = self.x_coordinate - new_x
                del_y = self.y_coordinate - new_y
    