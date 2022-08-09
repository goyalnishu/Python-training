import pygame, sys
import random
from pygame.locals import *


class grid_obj:
    def __init__(self, bg_color, p_list, safe, coordinate):
        self.bg_color = bg_color
        self.p_list = p_list
        self.safe = safe
        self.coordinate = coordinate


class piece:
    def __init__(self, id, color, anim_state, coordinates, radius):
        self.id = id
        self.color = color
        self.anim_state = anim_state
        self.coordinates = coordinates
        self.radius = radius
        self.original_coordinate = coordinates


class circularlist:
    def __init__(self):
        self.c_list = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0),
                       (8, 0), (8, 1),
                       (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7),
                       (14, 8), (13, 8),
                       (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14),
                       (6, 14), (6, 13),
                       (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7),
                       (0, 6)]

    def move(self, init_pos, value, chance):
        i = 0
        j = -1
        flag = 0
        while True:
            if self.c_list[i] == init_pos or j >= 0:
                # return self.c_list[(i+value)%(len(self.c_list))]
                if chance == 'R' and i == 50:
                    flag = 1
                if chance == 'G' and i == 11:
                    flag = 2
                if chance == 'B' and i == 37:
                    flag = 3
                if chance == 'Y' and i == 24:
                    flag = 4
                j += 1
                if j == value:
                    break
            i = (i + 1) % len(self.c_list)
        if flag == 1:
            return (self.c_list[i][0] + 1, self.c_list[i][1] + 1)
        elif flag == 2:
            return (self.c_list[i][0] + 1, self.c_list[i][1] + 1)
        elif flag == 3:
            return (self.c_list[i][0] + 1, self.c_list[i][1] - 1)
        elif flag == 4:
            return (self.c_list[i][0] - 1, self.c_list[i][1] - 1)
        else:
            return (self.c_list[i][0], self.c_list[i][1])

    def chk(self, pos):
        if pos in self.c_list:
            return True
        else:
            return False


HEIGHT = 1100
WIDTH = 900
init_x = 0
init_y = 0
chance = 'R'
dice_clicked = False
move_list = []
pygame.init()
DISPLAYSURF = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('LUDO')
dice_value = 6
# initial values
Game_grid = [[-1 for _ in range(15)] for _ in range(15)]
color_dict = {-1: (0, 0, 0),
              0: (255, 255, 255),
              1: (255, 0, 0), 'R': (255, 0, 0),
              2: (0, 255, 0,), 'G': (0, 255, 0,),
              3: (0, 0, 255), 'B': (0, 0, 255),
              4: (255, 225, 100), 'Y': (255, 225, 100)}
color_matrix = [[-1, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 2, 2, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 2, 2, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 2, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 2, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 2, 0, -1, -1, -1, -1, -1, -1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 4, 4, 4, 4, 4, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
                [-1, -1, -1, -1, -1, -1, 0, 3, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 3, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 3, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 3, 3, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 3, 3, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1]]
coordinate_matrix = [[[init_x + i * 50, init_y + j * 50] for i in range(0, 15)] for j in range(0, 15)]
safe_matrix = [[0 for _ in range(15)] for _ in range(15)]
safe_matrix[6][2] = 1
safe_matrix[8][1] = 1
safe_matrix[12][6] = 1
safe_matrix[13][8] = 1
safe_matrix[8][12] = 1
safe_matrix[6][13] = 1
safe_matrix[2][8] = 1
safe_matrix[1][6] = 1
# chess_faces
chess_faces = {1: [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
               2: [[0, 1, 0], [0, 0, 0], [0, 1, 0]],
               3: [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
               4: [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
               5: [[1, 0, 1], [0, 1, 0], [1, 0, 1]],
               6: [[1, 0, 1], [1, 0, 1], [1, 0, 1]],
               }

for i in range(15):
    for j in range(15):
        ob = grid_obj(color_dict[color_matrix[i][j]], [], safe_matrix[i][j], coordinate_matrix[i][j])
        Game_grid[i][j] = ob
# piece_initialization
R1 = piece('R1', color_dict[1], 0, (50 * 1, 50 * 1), 20)
Game_grid[1][1].p_list.append(R1)
R2 = piece('R2', color_dict[1], 0, (50 * 4, 50 * 1), 20)
Game_grid[4][1].p_list.append(R2)
R3 = piece('R3', color_dict[1], 0, (50 * 1, 50 * 4), 20)
Game_grid[1][4].p_list.append(R3)
R4 = piece('R4', color_dict[1], 0, (50 * 4, 50 * 4), 20)
Game_grid[4][4].p_list.append(R4)
G1 = piece('G1', color_dict[2], 0, (50 * 10, 50 * 1), 20)
Game_grid[10][1].p_list.append(G1)
G2 = piece('G2', color_dict[2], 0, (50 * 13, 50 * 1), 20)
Game_grid[13][1].p_list.append(G2)
G3 = piece('G3', color_dict[2], 0, (50 * 10, 50 * 4), 20)
Game_grid[10][4].p_list.append(G3)
G4 = piece('G4', color_dict[2], 0, (50 * 13, 50 * 4), 20)
Game_grid[13][4].p_list.append(G4)
B1 = piece('B1', color_dict[3], 0, (50 * 1, 50 * 10), 20)
Game_grid[1][10].p_list.append(B1)
B2 = piece('B2', color_dict[3], 0, (50 * 4, 50 * 10), 20)
Game_grid[4][10].p_list.append(B2)
B3 = piece('B3', color_dict[3], 0, (50 * 1, 50 * 13), 20)
Game_grid[1][13].p_list.append(B3)
B4 = piece('B4', color_dict[3], 0, (50 * 4, 50 * 13), 20)
Game_grid[4][13].p_list.append(B4)
Y1 = piece('Y1', color_dict[4], 0, (50 * 10, 50 * 10), 20)
Game_grid[10][10].p_list.append(Y1)
Y2 = piece('Y2', color_dict[4], 0, (50 * 13, 50 * 10), 20)
Game_grid[13][10].p_list.append(Y2)
Y3 = piece('Y3', color_dict[4], 0, (50 * 10, 50 * 13), 20)
Game_grid[10][13].p_list.append(Y3)
Y4 = piece('Y4', color_dict[4], 0, (50 * 13, 50 * 13), 20)
Game_grid[13][13].p_list.append(Y4)

clist_obj = circularlist()


def gridlocation(pos):
    x = pos[0]
    y = pos[1]
    return (x // 50, y // 50)


# test_pending
def relativePieceStructure(p_list, x, y):
    l = len(p_list)
    relRadius = int((2 / (l + 1)) * 20)
    relpoint = []
    j = 0
    if l % 2 == 0:
        l1 = [i + 1 for i in range((l // 2))]
        l2 = [i - 1 for i in range((l // 2))]
        relpoint = l2[::-1] + l1
    else:
        l1 = [i + 1 for i in range((l // 2))]
        l2 = [i - 1 for i in range((l // 2))]
        relpoint = l2[::-1] + [0] + l1
    for p in p_list:
        p.radius = relRadius
        p.coordinates = ((x) + (relpoint[j] * (relRadius // 2)), (y))
        j += 1


def drawGrid():
    global Game_grid
    newSurface = pygame.display.set_mode((HEIGHT, WIDTH))
    for i in range(15):
        for j in range(15):
            pygame.draw.rect(newSurface, Game_grid[i][j].bg_color, tuple(Game_grid[i][j].coordinate + [50, 50]))
            pygame.draw.rect(newSurface, (0, 0, 0), tuple(Game_grid[i][j].coordinate + [50, 50]), 1)

    # always constant
    pygame.draw.rect(newSurface, color_dict[1], (init_x, init_y, 300, 300))
    pygame.draw.rect(newSurface, color_dict[0], (init_x + 50, init_y + 50, 200, 200))
    pygame.draw.rect(newSurface, color_dict[2], (init_x + 450, init_y, 300, 300))
    pygame.draw.rect(newSurface, color_dict[0], (init_x + 500, init_y + 50, 200, 200))
    pygame.draw.rect(newSurface, color_dict[3], (init_x, init_y + 450, 300, 300))
    pygame.draw.rect(newSurface, color_dict[0], (init_x + 50, init_y + 500, 200, 200))
    pygame.draw.rect(newSurface, color_dict[4], (init_x + 450, init_y + 450, 300, 300))
    pygame.draw.rect(newSurface, color_dict[0], (init_x + 500, init_y + 500, 200, 200))

    for i in range(15):
        for j in range(15):
            relativePieceStructure(Game_grid[i][j].p_list, i * 50, j * 50)
            for k in Game_grid[i][j].p_list:
                c = k.coordinates
                # if c in [(50*1,6*50),(8*50,1*50),(13*50,8*50),(6*50,13*50)]:
                #     print("Yup")
                pygame.draw.circle(newSurface, k.color, (c[0] + 25, c[1] + 25), k.radius)
                pygame.draw.circle(newSurface, color_dict[-1], (c[0] + 25, c[1] + 25), k.radius, 1)
                # highlight
                if k.id[0] == chance:
                    pygame.draw.circle(newSurface, color_dict[0], (c[0] + 25, c[1] + 25), k.radius - 2, 2)
    # chess_faces

    face = chess_faces[dice_value]
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(newSurface, color_dict[0], ((0 + 800) + (50 * j), (0 + 300) + (50 * i), 50, 50))
            if face[i][j] == 1:
                pygame.draw.circle(newSurface, color_dict[1], ((0 + 800) + (50 * j) + 25, (0 + 300) + (50 * i) + 25),
                                   10)
    pygame.draw.rect(newSurface, color_dict[chance], ((0 + 798), (0 + 298), 150, 150), 4)
    return newSurface

def checkCollision(p_list):
    global chance
    global Game_grid
    new_list=[]
    for p in p_list:
        if p.id[0] == chance:
            new_list.append(p)
        else:
            p.coordinates=p.original_coordinate
            i=p.coordinates[0]//50
            j=p.coordinates[1]//50
            Game_grid[i][j].p_list.append(p)
    return new_list




def chk_id(p_list):
    global chance
    for i in p_list:
        if i.id[0] == chance:
            return True
    return False


# main_loop
while (True):
    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN:
            loc = gridlocation(event.pos)
            if loc[0] >= 16 and loc[0] <= 18 and loc[1] >= 6 and loc[1] <= 8 and dice_clicked == False:
                # dice_value = 6
                dice_value = random.randint(1, 6)
                print("dice clicked", chance)
                dice_clicked = True
            if dice_value != 6 and dice_clicked == True:
                print(1)
                flag = 0
                for i in clist_obj.c_list:
                    for p in Game_grid[i[0]][i[1]].p_list:
                        if p.id[0] == chance:
                            flag = 1
                if flag == 0:
                    if chance == 'R':
                        chance = 'G'
                    elif chance == 'G':
                        chance = 'Y'
                    elif chance == 'Y':
                        chance = 'B'
                    elif chance == 'B':
                        chance = 'R'
                    dice_clicked = False

            if chance == 'R' and dice_value == 6 and (loc in [(1, 1), (4, 1), (4, 4), (1, 4)]) and dice_clicked == True:
                print(2)
                print(Game_grid[1][6].p_list)
                Game_grid[1][6].p_list.append(Game_grid[loc[0]][loc[1]].p_list[0])
                Game_grid[1][6].p_list[-1].coordinates = (50 * 1, 50 * 6)
                for p in Game_grid[1][6].p_list:
                    print(p.coordinates)
                Game_grid[loc[0]][loc[1]].p_list = []
                print(Game_grid[1][6].p_list[-1].id)
                dice_clicked = False
            elif chance == 'G' and dice_value == 6 and (
                    loc in [(10, 1), (13, 1), (13, 4), (10, 4)]) and dice_clicked == True:
                print(3)
                print(Game_grid[8][1].p_list)
                Game_grid[8][1].p_list.append(Game_grid[loc[0]][loc[1]].p_list[0])
                Game_grid[8][1].p_list[-1].coordinates = (50 * 8, 50 * 1)
                Game_grid[loc[0]][loc[1]].p_list = []
                print(Game_grid[8][1].p_list[0].id)
                dice_clicked = False
            elif chance == 'Y' and dice_value == 6 and (
                    loc in [(10, 10), (13, 10), (13, 13), (10, 13)]) and dice_clicked == True:
                print(4)
                print(Game_grid[13][8].p_list)
                Game_grid[13][8].p_list.append(Game_grid[loc[0]][loc[1]].p_list[0])
                Game_grid[13][8].p_list[-1].coordinates = (50 * 13, 50 * 8)
                Game_grid[loc[0]][loc[1]].p_list = []
                print(Game_grid[13][8].p_list[0].id)
                dice_clicked = False
            elif chance == 'B' and dice_value == 6 and (
                    loc in [(1, 10), (4, 10), (4, 13), (1, 13)]) and dice_clicked == True:
                print(5)
                print(Game_grid[6][13].p_list)
                Game_grid[6][13].p_list.append(Game_grid[loc[0]][loc[1]].p_list[0])
                Game_grid[6][13].p_list[-1].coordinates = (50 * 6, 50 * 13)
                Game_grid[loc[0]][loc[1]].p_list = []
                print(Game_grid[6][13].p_list[0].id)
                dice_clicked = False

            elif chance == 'R' and (loc in [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7)]) and len(
                    Game_grid[loc[0]][loc[1]].p_list) > 0 and dice_clicked == True:
                if loc[0] + dice_value <= (5 + 1):
                    Game_grid[loc[0] + dice_value][loc[1]].p_list.append(Game_grid[loc[0]][loc[1]].p_list[-1])
                    Game_grid[loc[0] + dice_value][loc[1]].p_list[-1].coordinates = (
                    50 * (loc[0] + dice_value), 50 * (loc[1]))
                    Game_grid[loc[0]][loc[1]].p_list = Game_grid[loc[0]][loc[1]].p_list[:-1]
                dice_clicked = False

            elif chance == 'G' and (loc in [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5)]) and len(
                    Game_grid[loc[0]][loc[1]].p_list) > 0 and dice_clicked == True:
                if loc[1] + dice_value <= (5 + 1):
                    Game_grid[loc[0]][loc[1] + dice_value].p_list.append(Game_grid[loc[0]][loc[1]].p_list[-1])
                    Game_grid[loc[0]][loc[1] + dice_value].p_list[-1].coordinates = (
                        50 * (loc[0]), 50 * (loc[1] + dice_value))
                    Game_grid[loc[0]][loc[1]].p_list = Game_grid[loc[0]][loc[1]].p_list[:-1]
                dice_clicked = False

            elif chance == 'Y' and (loc in [(9, 7), (10, 7), (11, 7), (12, 7), (13, 7)]) and len(
                    Game_grid[loc[0]][loc[1]].p_list) > 0 and dice_clicked == True:
                if loc[0] - dice_value >= (9 - 1):
                    Game_grid[loc[0] - dice_value][loc[1]].p_list.append(Game_grid[loc[0]][loc[1]].p_list[-1])
                    Game_grid[loc[0] - dice_value][loc[1]].p_list[-1].coordinates = (
                        50 * (loc[0] - dice_value), 50 * (loc[1]))
                    Game_grid[loc[0]][loc[1]].p_list = Game_grid[loc[0]][loc[1]].p_list[:-1]
                dice_clicked = False

            elif chance == 'B' and (loc in [(7, 9), (7, 10), (7, 11), (7, 12), (7, 13)]) and len(
                    Game_grid[loc[0]][loc[1]].p_list) > 0 and dice_clicked == True:
                if loc[1] + dice_value >= (9 - 1):
                    Game_grid[loc[0]][loc[1] + dice_value].p_list.append(Game_grid[loc[0]][loc[1]].p_list[-1])
                    Game_grid[loc[0]][loc[1] + dice_value].p_list[-1].coordinates = (
                        50 * (loc[0]), 50 * (loc[1] + dice_value))
                    Game_grid[loc[0]][loc[1]].p_list = Game_grid[loc[0]][loc[1]].p_list[:-1]
                dice_clicked = False

            elif (clist_obj.chk(loc)) and chk_id(Game_grid[loc[0]][loc[1]].p_list) and dice_clicked == True:
                print(6)
                newpos = clist_obj.move(loc, dice_value, chance)
                new_list = []
                flg = 0
                for i in Game_grid[loc[0]][loc[1]].p_list:
                    if i.id[0] == chance and flg == 0:
                        Game_grid[newpos[0]][newpos[1]].p_list.append(i)
                        Game_grid[newpos[0]][newpos[1]].p_list[-1].coordinates = (50 * newpos[0], 50 * newpos[1])
                        #eating pieces
                        Game_grid[newpos[0]][newpos[1]].p_list=checkCollision(Game_grid[newpos[0]][newpos[1]].p_list)
                        flg = 1
                    else:
                        new_list.append(i)
                Game_grid[loc[0]][loc[1]].p_list = new_list
                dice_clicked = False

                if dice_value != 6:
                    if chance == 'R':
                        chance = 'G'
                    elif chance == 'G':
                        chance = 'Y'
                    elif chance == 'Y':
                        chance = 'B'
                    elif chance == 'B':
                        chance = 'R'

            # DISPLAYSURF.blit(drawGrid(), (0, 0))
            # pygame.display.update()
        DISPLAYSURF.blit(drawGrid(), (0, 0))
        pygame.display.update()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
