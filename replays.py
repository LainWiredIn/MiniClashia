from src.headers import *
from src.building import *
from src.king import *
from src.input import *
import time
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print("using numpy version", np.__version__)
time.sleep(3)


# clearing screen on ubuntu
os.system('clear')

# defining the huts
Hut1 = Building("HUT1", 100, 9, 99)
Hut2 = Building("HUT2", 100, 3, 77)
Hut3 = Building("HUT3", 100, 7, 107)
Hut4 = Building("HUT4", 100, 1, 93)
Hut5 = Building("HUT5", 100, 13, 107)

# defining troops list
troops = []

# defining the walls
# CHANGE COORDINATES BASED ON COORDINATES OF TOWNHALL
Wall1 = Building("WALL1", 20, 8, 67)
Wall2 = Building("WALL2", 20, 5, 67)
Wall3 = Building("WALL3", 20, 7, 67)
Wall4 = Building("WALL4", 20, 6, 67)
Wall5 = Building("WALL5", 20, 8, 59)
Wall6 = Building("WALL6", 20, 7, 59)
Wall7 = Building("WALL7", 20, 5, 59)
Wall8 = Building("WALL8", 20, 6, 59)
Wall9 = Building("WALL9", 20, 4, 61)
Wall10 = Building("WALL10", 20, 4, 63)
Wall11 = Building("WALL11", 20, 4, 65)
Wall12 = Building("WALL12", 20, 9, 65)
Wall13 = Building("WALL13", 20, 9, 63)
Wall14 = Building("WALL14", 20, 9, 61)

# defining spawning points
Spawning_Point_1 = Building("Portal 1", 42069, 1, 1)
Spawning_Point_2 = Building("Portal 2", 42069, 7, 1)
Spawning_Point_3 = Building("Portal 3", 42069, 13, 1)

# defining the town hall 8 points for boundary

TownHall_Bound1 = Building("Townhall", 500, 8, 65)
TownHall_Bound2 = Building("Townhall", 500, 8, 63)
TownHall_Bound3 = Building("Townhall", 500, 8, 61)
TownHall_Bound4 = Building("Townhall", 500, 7, 61)
TownHall_Bound5 = Building("Townhall", 500, 6, 61)
TownHall_Bound6 = Building("Townhall", 500, 5, 61)
TownHall_Bound7 = Building("Townhall", 500, 5, 63)
TownHall_Bound8 = Building("Townhall", 500, 5, 65)
TownHall_Bound9 = Building("Townhall", 500, 7, 65)
TownHall_Bound10 = Building("Townhall", 500, 6, 65)

Cannon1 = Canon("Big Bang Attack", 10, 5, 21, 3, 30)
Cannon2 = Canon("Kamehameha", 10, 10, 21, 3, 30)


MC = King("Lain", 2, 1, 9, 1000, 1)

# rows = 15
# cols = 121
# grid = np.zeros((rows, cols), dtype = int)
grid[::2, ::2] = 1
grid[1::2, ::2] = 1
    
def king_attacks(b_index):
    if(b_index==-1):
        # hut1 has been attacked by the king
        Hut1.hitpoint = Hut1.hitpoint - MC.damage
    elif(b_index==-2) :
        # hut2 has been attacked by the king
        Hut2.hitpoint = Hut2.hitpoint - MC.damage
    elif(b_index==-3) :
        Hut3.hitpoint = Hut3.hitpoint - MC.damage
    elif(b_index==-4): 
        Hut4.hitpoint = Hut4.hitpoint - MC.damage
    elif(b_index==-5): 
        Hut5.hitpoint = Hut5.hitpoint - MC.damage
    elif(b_index==-6): 
        # TOWNHALL IS UNDER ATTACK BY THE ALMIGHTY KING
        TownHall_Bound1.hitpoint = TownHall_Bound1.hitpoint - MC.damage
        TownHall_Bound2.hitpoint = TownHall_Bound2.hitpoint - MC.damage
        TownHall_Bound3.hitpoint = TownHall_Bound3.hitpoint - MC.damage
        TownHall_Bound4.hitpoint = TownHall_Bound4.hitpoint - MC.damage
        TownHall_Bound5.hitpoint = TownHall_Bound5.hitpoint - MC.damage
        TownHall_Bound6.hitpoint = TownHall_Bound6.hitpoint - MC.damage
        TownHall_Bound7.hitpoint = TownHall_Bound7.hitpoint - MC.damage
        TownHall_Bound8.hitpoint = TownHall_Bound8.hitpoint - MC.damage
        TownHall_Bound9.hitpoint = TownHall_Bound9.hitpoint - MC.damage
        TownHall_Bound10.hitpoint = TownHall_Bound10.hitpoint - MC.damage
    elif(b_index==-7): 
        Wall1.hitpoint = Wall1.hitpoint - MC.damage
    elif(b_index==-8): 
        Wall2.hitpoint = Wall2.hitpoint - MC.damage
    elif(b_index==-9): 
        Wall3.hitpoint = Wall3.hitpoint - MC.damage
    elif(b_index==-10): 
        Wall4.hitpoint = Wall4.hitpoint - MC.damage
    elif(b_index==-11): 
        Wall5.hitpoint = Wall5.hitpoint - MC.damage
    elif(b_index==-12): 
        Wall6.hitpoint = Wall6.hitpoint - MC.damage
    elif(b_index==-13): 
        Wall7.hitpoint = Wall7.hitpoint - MC.damage
    elif(b_index==-14): 
        Wall8.hitpoint = Wall8.hitpoint - MC.damage
    elif(b_index==-15): 
        Wall9.hitpoint = Wall9.hitpoint - MC.damage
    elif(b_index==-16): 
        Wall10.hitpoint = Wall10.hitpoint - MC.damage
    elif(b_index==-17): 
        Wall11.hitpoint = Wall11.hitpoint - MC.damage
    elif(b_index==-18): 
        Wall12.hitpoint = Wall12.hitpoint - MC.damage
    elif(b_index==-19): 
        Wall13.hitpoint = Wall13.hitpoint - MC.damage
    elif(b_index==-20): 
        Wall14.hitpoint = Wall14.hitpoint - MC.damage
    elif(b_index==-21):
        Cannon1.hitpoint = Cannon1.hitpoint - MC.damage
    elif(b_index==-22):
        Cannon2.hitpoint = Cannon2.hitpoint - MC.damage
        
def barbarian_attacks(damage, b_index):
    if(b_index==-1):
        # hut1 has been attacked by the king
        Hut1.hitpoint = Hut1.hitpoint - damage
    elif(b_index==-2) :
        # hut2 has been attacked by the king
        Hut2.hitpoint = Hut2.hitpoint - damage
    elif(b_index==-3) :
        Hut3.hitpoint = Hut3.hitpoint - damage
    elif(b_index==-4): 
        Hut4.hitpoint = Hut4.hitpoint - damage
    elif(b_index==-5): 
        Hut5.hitpoint = Hut5.hitpoint - damage
    elif(b_index==-6): 
        # TOWNHALL IS UNDER ATTACK BY THE ALMIGHTY KING
        TownHall_Bound1.hitpoint = TownHall_Bound1.hitpoint - damage
        TownHall_Bound2.hitpoint = TownHall_Bound2.hitpoint - damage
        TownHall_Bound3.hitpoint = TownHall_Bound3.hitpoint - damage
        TownHall_Bound4.hitpoint = TownHall_Bound4.hitpoint - damage
        TownHall_Bound5.hitpoint = TownHall_Bound5.hitpoint - damage
        TownHall_Bound6.hitpoint = TownHall_Bound6.hitpoint - damage
        TownHall_Bound7.hitpoint = TownHall_Bound7.hitpoint - damage
        TownHall_Bound8.hitpoint = TownHall_Bound8.hitpoint - damage
        TownHall_Bound9.hitpoint = TownHall_Bound9.hitpoint - damage
        TownHall_Bound10.hitpoint = TownHall_Bound10.hitpoint - damage
    elif(b_index==-7): 
        Wall1.hitpoint = Wall1.hitpoint - damage
    elif(b_index==-8): 
        Wall2.hitpoint = Wall2.hitpoint - damage
    elif(b_index==-9): 
        Wall3.hitpoint = Wall3.hitpoint - damage
    elif(b_index==-10): 
        Wall4.hitpoint = Wall4.hitpoint - damage
    elif(b_index==-11): 
        Wall5.hitpoint = Wall5.hitpoint - damage
    elif(b_index==-12): 
        Wall6.hitpoint = Wall6.hitpoint - damage
    elif(b_index==-13): 
        Wall7.hitpoint = Wall7.hitpoint - damage
    elif(b_index==-14): 
        Wall8.hitpoint = Wall8.hitpoint - damage
    elif(b_index==-15): 
        Wall9.hitpoint = Wall9.hitpoint - damage
    elif(b_index==-16): 
        Wall10.hitpoint = Wall10.hitpoint - damage
    elif(b_index==-17): 
        Wall11.hitpoint = Wall11.hitpoint - damage
    elif(b_index==-18): 
        Wall12.hitpoint = Wall12.hitpoint - damage
    elif(b_index==-19): 
        Wall13.hitpoint = Wall13.hitpoint - damage
    elif(b_index==-20): 
        Wall14.hitpoint = Wall14.hitpoint - damage
    elif(b_index==-21):
        Cannon1.hitpoint = Cannon1.hitpoint - damage
    elif(b_index==-22):
        Cannon2.hitpoint = Cannon2.hitpoint - damage
    

def show_village():
        for i in range(rows):
            print("",end="")
            for j in range(cols):
                print("-", end="")
            print("")
            for j in range(cols):
                if grid[i][j] == 1 :
                    print("|", end="")
                else :
                    # grid value used to indicate map obstacles
                    grid[i][j] = -420
                    # assuming some grid has some obstacle on it
                    
                    # Barbarians
                    flag = 0
                    if barbarian_exists == True:
                        for obj in troops:
                            if i==obj.x_coordinate and j==obj.y_coordinate and obj.health>0 :
                                if obj.health>=50:
                                    print(f"{Fore.LIGHTBLACK_EX + Style.BRIGHT + Back.GREEN}B", end="")
                                elif obj.health>=20 and obj.health>=50:
                                    print(f"{Fore.LIGHTBLACK_EX + Style.NORMAL + Back.YELLOW}B", end="")
                                else :
                                    print(f"{Fore.LIGHTBLACK_EX + Style.DIM + Back.RED}B", end="")
                                grid[i][j] = 50
                                flag = 1
                                if(obj.y_coordinate!=(cols-2) and grid[obj.x_coordinate][obj.y_coordinate+2]!=0):
                                    barbarian_attacks(obj.damage, grid[obj.x_coordinate][obj.y_coordinate+2])
                                elif(obj.y_coordinate!=1 and grid[obj.x_coordinate][obj.y_coordinate-2]!=0):
                                    barbarian_attacks(obj.damage, grid[obj.x_coordinate][obj.y_coordinate-2])
                                elif(obj.x_coordinate!=(rows-1) and grid[obj.x_coordinate+1][obj.y_coordinate]!=0):
                                    barbarian_attacks(obj.damage, grid[obj.x_coordinate+1][obj.y_coordinate])
                                elif(obj.x_coordinate!=0 and grid[obj.x_coordinate-1][obj.y_coordinate]!=0):
                                    barbarian_attacks(obj.damage, grid[obj.x_coordinate-1][obj.y_coordinate])
                                break
                    if(flag==1):
                        continue
                    
                    # Huts
                    if i==Hut1.x_coordinate and j==Hut1.y_coordinate and Hut1.hitpoint>0:
                        grid[i][j] = -1
                        if Hut1.hitpoint>=50:
                            print(f"{Back.GREEN}H", end="")
                        elif Hut1.hitpoint>=20 and Hut1.hitpoint<50 :
                            print(f"{Back.YELLOW}H", end="")
                        else :
                            print(f"{Back.RED}H", end="")
                    elif i==Hut2.x_coordinate and j==Hut2.y_coordinate and Hut2.hitpoint>0:
                        grid[i][j] = -2
                        if Hut2.hitpoint>=50:
                            print(f"{Back.GREEN}H", end="")
                        elif Hut2.hitpoint>=20 and Hut2.hitpoint<50 :
                            print(f"{Back.YELLOW}H", end="")
                        else :
                            print(f"{Back.RED}H", end="")
                    elif i==Hut3.x_coordinate and j==Hut3.y_coordinate and Hut3.hitpoint>0:
                        grid[i][j] = -3
                        if Hut3.hitpoint>=50:
                            print(f"{Back.GREEN}H", end="")
                        elif Hut3.hitpoint>=20 and Hut3.hitpoint<50 :
                            print(f"{Back.YELLOW}H", end="")
                        else :
                            print(f"{Back.RED}H", end="")
                    elif i==Hut4.x_coordinate and j==Hut4.y_coordinate and Hut4.hitpoint>0:
                        grid[i][j] = -4
                        if Hut4.hitpoint>=50:
                            print(f"{Back.GREEN}H", end="")
                        elif Hut4.hitpoint>=20 and Hut4.hitpoint<50 :
                            print(f"{Back.YELLOW}H", end="")
                        else :
                            print(f"{Back.RED}H", end="")
                    elif i==Hut5.x_coordinate and j==Hut5.y_coordinate and Hut5.hitpoint>0:
                        grid[i][j] = -5
                        if Hut5.hitpoint>=50:
                            print(f"{Back.GREEN}H", end="")
                        elif Hut5.hitpoint>=20 and Hut5.hitpoint<50 :
                            print(f"{Back.YELLOW}H", end="")
                        else :
                            print(f"{Back.RED}H", end="")

                    elif i==Spawning_Point_1.x_coordinate and j==Spawning_Point_1.y_coordinate :
                        print(f"{Back.LIGHTRED_EX}S", end="")
                    elif i==Spawning_Point_2.x_coordinate and j==Spawning_Point_2.y_coordinate :
                        print(f"{Back.LIGHTRED_EX}S", end="")
                    elif i==Spawning_Point_3.x_coordinate and j==Spawning_Point_3.y_coordinate :
                        print(f"{Back.LIGHTRED_EX}S", end="")

                    elif i==TownHall_Bound1.x_coordinate and j==TownHall_Bound1.y_coordinate and TownHall_Bound1.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound2.x_coordinate and j==TownHall_Bound2.y_coordinate and TownHall_Bound2.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound3.x_coordinate and j==TownHall_Bound3.y_coordinate and TownHall_Bound3.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound4.x_coordinate and j==TownHall_Bound4.y_coordinate and TownHall_Bound4.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound5.x_coordinate and j==TownHall_Bound5.y_coordinate and TownHall_Bound5.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound6.x_coordinate and j==TownHall_Bound6.y_coordinate and TownHall_Bound6.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound7.x_coordinate and j==TownHall_Bound7.y_coordinate and TownHall_Bound7.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound8.x_coordinate and j==TownHall_Bound8.y_coordinate and TownHall_Bound8.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound9.x_coordinate and j==TownHall_Bound9.y_coordinate and TownHall_Bound9.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")
                    elif i==TownHall_Bound10.x_coordinate and j==TownHall_Bound10.y_coordinate and TownHall_Bound10.hitpoint>0 :
                        grid[i][j] = -6
                        if TownHall_Bound1.hitpoint>=250:
                            print(f"{Back.GREEN}T", end="")
                        elif TownHall_Bound1.hitpoint>=100 and TownHall_Bound1.hitpoint<250 :
                            print(f"{Back.YELLOW}T", end="")
                        else :
                            print(f"{Back.RED}T", end="")

                    # WALLS
                    elif i==Wall1.x_coordinate and j==Wall1.y_coordinate and Wall1.hitpoint>0 :
                        grid[i][j] = -7
                        if Wall1.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall1.hitpoint>=4 and Wall1.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall2.x_coordinate and j==Wall2.y_coordinate and Wall2.hitpoint>0 :
                        grid[i][j] = -8
                        if Wall2.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall2.hitpoint>=4 and Wall2.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall3.x_coordinate and j==Wall3.y_coordinate and Wall3.hitpoint>0 :
                        grid[i][j] = -9
                        if Wall3.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall3.hitpoint>=4 and Wall3.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall4.x_coordinate and j==Wall4.y_coordinate and Wall4.hitpoint>0 :
                        grid[i][j] = -10
                        if Wall4.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall4.hitpoint>=4 and Wall4.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall5.x_coordinate and j==Wall5.y_coordinate and Wall5.hitpoint>0 :
                        grid[i][j] = -11
                        if Wall5.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall5.hitpoint>=4 and Wall5.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall6.x_coordinate and j==Wall6.y_coordinate and Wall6.hitpoint>0 :
                        grid[i][j] = -12
                        if Wall6.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall6.hitpoint>=4 and Wall6.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall7.x_coordinate and j==Wall7.y_coordinate and Wall7.hitpoint>0 :
                        grid[i][j] = -13
                        if Wall7.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall7.hitpoint>=4 and Wall7.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall8.x_coordinate and j==Wall8.y_coordinate and Wall8.hitpoint>0 :
                        grid[i][j] = -14
                        if Wall8.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall8.hitpoint>=4 and Wall8.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall9.x_coordinate and j==Wall9.y_coordinate and Wall9.hitpoint>0 :
                        grid[i][j] = -15
                        if Wall9.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall9.hitpoint>=4 and Wall9.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall10.x_coordinate and j==Wall10.y_coordinate and Wall10.hitpoint>0 :
                        grid[i][j] = -16
                        if Wall10.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall10.hitpoint>=4 and Wall10.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall11.x_coordinate and j==Wall11.y_coordinate and Wall11.hitpoint>0 :
                        grid[i][j] = -17
                        if Wall11.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall11.hitpoint>=4 and Wall11.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall12.x_coordinate and j==Wall12.y_coordinate and Wall12.hitpoint>0 :
                        grid[i][j] = -18
                        if Wall12.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall12.hitpoint>=4 and Wall12.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall13.x_coordinate and j==Wall13.y_coordinate and Wall13.hitpoint>0 :
                        grid[i][j] = -19
                        if Wall13.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall13.hitpoint>=4 and Wall13.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Wall14.x_coordinate and j==Wall14.y_coordinate and Wall14.hitpoint>0 :
                        grid[i][j] = -20
                        if Wall14.hitpoint>=10:
                            print(f"{Back.GREEN}W", end="")
                        elif Wall14.hitpoint>=4 and Wall14.hitpoint<10 :
                            print(f"{Back.YELLOW}W", end="")
                        else :
                            print(f"{Back.RED}W", end="")
                    elif i==Cannon1.x_coordinate and j==Cannon1.y_coordinate and Cannon1.hitpoint>0 :
                        grid[i][j] = -21
                        if Cannon1.hitpoint>=5:
                            print(f"{Back.GREEN}C", end="")
                        elif Cannon1.hitpoint>=2 and Cannon1.hitpoint<5 :
                            print(f"{Back.YELLOW}C", end="")
                        else :
                            print(f"{Back.RED}C", end="")
                    elif i==Cannon2.x_coordinate and j==Cannon2.y_coordinate and Cannon2.hitpoint>0 :
                        grid[i][j] = -22
                        if Cannon2.hitpoint>=5:
                            print(f"{Back.GREEN}C", end="")
                        elif Cannon2.hitpoint>=2 and Cannon2.hitpoint<5 :
                            print(f"{Back.YELLOW}C", end="")
                        else :
                            print(f"{Back.RED}C", end="")
                    elif i==MC.x_coordinate and j==MC.y_coordinate and MC.health>0 :
                        print(f"{Fore.CYAN + Style.BRIGHT + Back.MAGENTA}K", end="")
                        grid[i][j] = 50
                    else :
                        grid[i][j] = 0
                        # grid cell is empty
                        print(" ", end="")
            print()
        print("-------------------------------------------------------------------------------------------------------------------------")

# BillWood.checksum(10,20)
barbarian_exists = False

path = "replays"

replay_file = open(os.path.join(path, 'replay.txt'), 'r')
lines = replay_file.readlines()
line_index = 0

t0 = time.time()

# bonus
deactivate_flag = 0


value = True
while (value):
    if(line_index < len(lines)):
        lok = lines[line_index].split(" ")
        if(len(lok) == 3):
            key_val = " "
            timelim = float(lok[2])
        else :
            key_val = lok[0]
            timelim = float(lok[1])
    if(time.time()-t0 > timelim):
        print(f"{Fore.GREEN}------------------------------------------WELCOME TO CLASH OF CLANS: 2D--------------------------------------------------")
        # print("KING SPEED = ", MC.movement_speed)
        show_village()
        MC.show_King_Health(MC.health/10, 100, "Current Health")
        
        line_index = line_index + 1
        
        if(key_val=="q"):
            # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
            os.system('clear')
            print("You have quit the game")
            break
        if(Cannon1.hitpoint>0 and MC.x_coordinate>=(Cannon1.x_coordinate-Cannon1.range) and MC.x_coordinate<=(Cannon1.x_coordinate+Cannon1.range) and MC.y_coordinate>=(Cannon1.y_coordinate-(2*Cannon1.range)) and MC.y_coordinate<=(Cannon1.y_coordinate+(2*Cannon1.range))) :
            MC.health = MC.health - Cannon1.damage_value
        if(Cannon2.hitpoint>0 and MC.x_coordinate>=(Cannon2.x_coordinate-Cannon2.range) and MC.x_coordinate<=(Cannon2.x_coordinate+Cannon2.range) and MC.y_coordinate>=(Cannon2.y_coordinate-(2*Cannon2.range)) and MC.y_coordinate<=(Cannon2.y_coordinate+(2*Cannon2.range))) :
            MC.health = MC.health - Cannon2.damage_value
        print("")
        print("Current keyvalue = ", key_val)
        Kingspeed = MC.movement_speed
        if(MC.health>0) :
            if key_val=="w" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if(MC.x_coordinate==0):
                    MC.x_coordinate = MC.x_coordinate
                elif(grid[MC.x_coordinate-Kingspeed][MC.y_coordinate]==0) :
                    MC.x_coordinate = MC.x_coordinate-Kingspeed
            elif key_val=="s" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if(MC.x_coordinate==(rows-1)):
                    MC.x_coordinate = MC.x_coordinate
                elif(grid[MC.x_coordinate+Kingspeed][MC.y_coordinate]==0) :
                    MC.x_coordinate = MC.x_coordinate+Kingspeed
            elif key_val=="a" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if(MC.y_coordinate==1):
                    MC.y_coordinate = MC.y_coordinate
                elif(grid[MC.x_coordinate][MC.y_coordinate-2*Kingspeed]==0):
                    MC.y_coordinate = MC.y_coordinate-2*Kingspeed
            elif key_val=="d" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if(MC.y_coordinate==(cols-2)):
                    MC.y_coordinate = MC.y_coordinate
                elif(grid[MC.x_coordinate][MC.y_coordinate+(2*Kingspeed)]==0):
                    MC.y_coordinate = MC.y_coordinate+(2*Kingspeed)
            elif key_val=="p" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                barbarian_exists = True
                troops.append(Barbarian("StormTrooper", 1, 3, 5, 100, 1))
                # os.system('clear')
                # print("VICTORY!")
                # time.sleep(5)
            elif key_val=="l" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                barbarian_exists = True
                troops.append(Barbarian("StormTrooper", 7, 3, 5, 100, 1))
            elif key_val=="m" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                barbarian_exists = True
                troops.append(Barbarian("StormTrooper", 13, 3, 5, 100, 1))
            elif key_val==" " :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if(MC.y_coordinate!=(cols-2) and grid[MC.x_coordinate][MC.y_coordinate+2]!=0):
                    king_attacks(grid[MC.x_coordinate][MC.y_coordinate+2])
                elif(MC.y_coordinate!=1 and grid[MC.x_coordinate][MC.y_coordinate-2]!=0):
                    king_attacks(grid[MC.x_coordinate][MC.y_coordinate-2])
                elif(MC.x_coordinate!=(rows-1) and grid[MC.x_coordinate+1][MC.y_coordinate]!=0):
                    king_attacks(grid[MC.x_coordinate+1][MC.y_coordinate])
                elif(MC.x_coordinate!=0 and grid[MC.x_coordinate-1][MC.y_coordinate]!=0):
                    king_attacks(grid[MC.x_coordinate-1][MC.y_coordinate])
            # leviathan axe
            elif key_val=="x" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if(MC.y_coordinate!=(cols-2) and grid[MC.x_coordinate][MC.y_coordinate+2]!=0):
                    king_attacks(grid[MC.x_coordinate][MC.y_coordinate+2])
                if(MC.y_coordinate!=1 and grid[MC.x_coordinate][MC.y_coordinate-2]!=0):
                    king_attacks(grid[MC.x_coordinate][MC.y_coordinate-2])
                if(MC.x_coordinate!=(rows-1) and grid[MC.x_coordinate+1][MC.y_coordinate]!=0):
                    king_attacks(grid[MC.x_coordinate+1][MC.y_coordinate])
                if(MC.x_coordinate!=0 and grid[MC.x_coordinate-1][MC.y_coordinate]!=0):
                    king_attacks(grid[MC.x_coordinate-1][MC.y_coordinate])
            # spells
            elif key_val=="r" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if MC.health>0 :
                    MC.damage = MC.damage*2
                    MC.movement_speed = MC.movement_speed*2
                if barbarian_exists == True:
                    for obj in troops:
                        if obj.health>0:
                            obj.damage = obj.damage*2
                            obj.movement_speed = obj.movement_speed*2
                
            elif key_val=="h" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if MC.health>0 :
                    MC.health = MC.health*1.5
                    if(MC.health>1000):
                        MC.health = 1000
                    
                if barbarian_exists == True:
                    for obj in troops:
                        if obj.health>0:
                            obj.health = obj.health*1.5
                            if(obj.health>100):
                                obj.health = 100
            
            # deactivate cannons (deactivates for time period and can be used only once)
            # using a signal jamming device
            # but the cannons are smart and they register the signature of the signal jamming device used and do not allow it to jam them again 
            
            elif key_val=="o" :
                # replay_file.write(key_val+" "+str(time.time()-t0)+"\n")
                if(deactivate_flag==0):
                    deactivate_flag = 1
                    Cannon1.damage_value = 0
                    Cannon2.damage_value = 0
                    t_minus = time.time()
        
        # 10 seconds on the timer for cannon deactivation
        if(deactivate_flag == 1 and (time.time() - t_minus) > 10):
            deactivate_flag = 2
            Cannon1.damage_value = 30
            Cannon2.damage_value = 30
            
                

        for obj in troops:
            if(obj.health>0):
                if(Cannon1.hitpoint>0 and obj.x_coordinate>=(Cannon1.x_coordinate-Cannon1.range) and obj.x_coordinate<=(Cannon1.x_coordinate+Cannon1.range) and obj.y_coordinate>=(Cannon1.y_coordinate-(2*Cannon1.range)) and obj.y_coordinate<=(Cannon1.y_coordinate+(2*Cannon1.range))) :
                    obj.health = obj.health - Cannon1.damage_value
                if(Cannon2.hitpoint>0 and obj.x_coordinate>=(Cannon2.x_coordinate-Cannon2.range) and obj.x_coordinate<=(Cannon2.x_coordinate+Cannon2.range) and obj.y_coordinate>=(Cannon2.y_coordinate-(2*Cannon2.range)) and obj.y_coordinate<=(Cannon2.y_coordinate+(2*Cannon2.range))) :
                    obj.health = obj.health - Cannon2.damage_value
                barbarian_x = obj.x_coordinate
                barbarian_y = obj.y_coordinate
                curr_distance = 1000
                
                if(Hut1.hitpoint>0):
                    new_distance = ((((barbarian_x - Hut1.x_coordinate)**2) + ((barbarian_y - Hut1.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = Hut1.x_coordinate
                        y = Hut1.y_coordinate
                        br_index = -1
                
                if(Hut2.hitpoint>0):
                    new_distance = ((((barbarian_x - Hut2.x_coordinate)**2) + ((barbarian_y - Hut2.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = Hut2.x_coordinate
                        y = Hut2.y_coordinate
                        br_index = -2
                
                if(Hut3.hitpoint>0):
                    new_distance = ((((barbarian_x - Hut3.x_coordinate)**2) + ((barbarian_y - Hut3.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = Hut3.x_coordinate
                        y = Hut3.y_coordinate
                        br_index = -3
                
                if(Hut4.hitpoint>0):
                    new_distance = ((((barbarian_x - Hut4.x_coordinate)**2) + ((barbarian_y - Hut4.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = Hut4.x_coordinate
                        y = Hut4.y_coordinate
                        br_index = -4
                
                if(Hut5.hitpoint>0):
                    new_distance = ((((barbarian_x - Hut5.x_coordinate)**2) + ((barbarian_y - Hut5.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = Hut5.x_coordinate
                        y = Hut5.y_coordinate
                        br_index = -5
                
                if(TownHall_Bound1.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound1.x_coordinate)**2) + ((barbarian_y - TownHall_Bound1.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound1.x_coordinate
                        y = TownHall_Bound1.y_coordinate
                        br_index = -6
                    
                if(TownHall_Bound2.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound2.x_coordinate)**2) + ((barbarian_y - TownHall_Bound2.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound2.x_coordinate
                        y = TownHall_Bound2.y_coordinate
                        br_index = -6
                
                if(TownHall_Bound3.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound3.x_coordinate)**2) + ((barbarian_y - TownHall_Bound3.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound3.x_coordinate
                        y = TownHall_Bound3.y_coordinate
                        br_index = -6
                
                if(TownHall_Bound4.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound4.x_coordinate)**2) + ((barbarian_y - TownHall_Bound4.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound4.x_coordinate
                        y = TownHall_Bound4.y_coordinate
                        br_index = -6
                
                if(TownHall_Bound5.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound5.x_coordinate)**2) + ((barbarian_y - TownHall_Bound5.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound5.x_coordinate
                        y = TownHall_Bound5.y_coordinate
                        br_index = -6
                
                if(TownHall_Bound6.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound6.x_coordinate)**2) + ((barbarian_y - TownHall_Bound6.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound6.x_coordinate
                        y = TownHall_Bound6.y_coordinate
                        br_index = -6
                    
                if(TownHall_Bound7.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound7.x_coordinate)**2) + ((barbarian_y - TownHall_Bound7.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound7.x_coordinate
                        y = TownHall_Bound7.y_coordinate
                        br_index = -6
                    
                if(TownHall_Bound8.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound8.x_coordinate)**2) + ((barbarian_y - TownHall_Bound8.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound8.x_coordinate
                        y = TownHall_Bound8.y_coordinate
                        br_index = -6
                
                if(TownHall_Bound9.hitpoint>0):
                    new_distance = ((((barbarian_x - TownHall_Bound9.x_coordinate)**2) + ((barbarian_y - TownHall_Bound9.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound9.x_coordinate
                        y = TownHall_Bound9.y_coordinate
                        br_index = -6
                
                if(TownHall_Bound10.hitpoint>0):  
                    new_distance = ((((barbarian_x - TownHall_Bound10.x_coordinate)**2) + ((barbarian_y - TownHall_Bound10.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = TownHall_Bound10.x_coordinate
                        y = TownHall_Bound10.y_coordinate
                        br_index = -6
                
                if(Cannon1.hitpoint>0):
                    new_distance = ((((barbarian_x - Cannon1.x_coordinate)**2) + ((barbarian_y - Cannon1.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = Cannon1.x_coordinate
                        y = Cannon1.y_coordinate
                        br_index = -21
                
                if(Cannon2.hitpoint>0):
                    new_distance = ((((barbarian_x - Cannon2.x_coordinate)**2) + ((barbarian_y - Cannon2.y_coordinate)**2) )**0.5)
                    if(new_distance<curr_distance):
                        curr_distance = new_distance
                        x = Cannon2.x_coordinate
                        y = Cannon2.y_coordinate
                        br_index = -22
                    
                obj.barbarian_moves(x, y)
        

        
        
            
                
                
            
        # time.sleep(0.03)
        # os.system('clear')
        # print("\033[%d;%dH" % (0,0))
        print("")
        print("\033[1;1H", end="")
        test_var = -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 50:
                    test_var = 1
                    break
            if(test_var==1):
                break
        if(test_var==-1):
            break
        test_var = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == -21 or grid[i][j] == -22 or (grid[i][j] <=-1 and grid[i][j] >=-6):
                    test_var = 1
                    break
            if(test_var==1):
                break
        if(test_var==0):
            break
    
if(test_var==0):
    os.system('clear')
    print("VICTORY!")
    print()
elif(test_var==-1):
    os.system('clear')
    print("DEFEAT!")
    print()
    
replay_file.close()