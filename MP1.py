import pyxel
import pyxelgrid as pg
from dataclasses import dataclass
TITLE: str = "Battle City"
FPS: int= 25
GRID_SIZE: int = 640

DIRS: dict[str, tuple[int, int]] = {'north': (32,0), 'west': (48, 0), 'east': (16, 0), 'south': (0,0)}

@dataclass
class CellState:
    cell_type: str
    walkable: bool
    occupancy: str

@dataclass
class Your_Tank:
    location: tuple[int,int]
    direction: tuple[int, int]

@dataclass
class Opponent_Tank:
    location: tuple[int,int]

@dataclass
class Your_Bullet:
    location: tuple[int,int]
    direction: str

#bullets should destroy each other

class App(pg.PyxelGrid[CellState]):
    grid_size = GRID_SIZE
    def __init__(self, grid_size):
        self.grid_size = grid_size
        super().__init__(r=16, c=16, dim=16)
        for r in range(self.r):
            for c in range(self.c):
                self[(r, c)] = CellState(cell_type='tank', walkable=True, occupancy='')
        self[(10, 0)].occupancy = 'your_tank'

        stones = [(2,10), (10,10), (13,4)]
        for stone in stones:
            self[stone].walkable = False
            self[stone].cell_type = 'stone'

        
    
    def init(self):
        pyxel.mouse(True)
        self.your_tank = Your_Tank((10,0), 'north')
        pyxel.images[1].load(0,0, '/home/cs12lab1/Desktop/pyxel-image1.png')
        self.your_bullet_list: list[Your_Bullet] = []


    def is_in_bounds(self, i: int, j: int) -> bool:
        if 0 <= i < self.r and 0 <= j < self.c and self[(i,j)].cell_type != 'stone':
            return True
        return False

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            print(self.mouse_cell())

        if pyxel.btnp(pyxel.KEY_A):
            cur_i, cur_j = self.your_tank.location
            self[cur_i,cur_j].occupancy = ''
            new_location = (cur_i-1, cur_j)
            if self.is_in_bounds(new_location[0], new_location[1]):
                self.your_tank.location = new_location
                self[self.your_tank.location].occupancy = 'your_tank'
            else: self[cur_i,cur_j].occupancy = 'your_tank'

        if pyxel.btnp(pyxel.KEY_W):
            cur_i, cur_j = self.your_tank.location
            self[cur_i,cur_j].occupancy = ''
            new_location = (cur_i, cur_j-1)
            if self.is_in_bounds(new_location[0], new_location[1]):
                self.your_tank.location = new_location
                self[self.your_tank.location].occupancy = 'your_tank'
            else: self[cur_i,cur_j].occupancy = 'your_tank'

        if pyxel.btnp(pyxel.KEY_S):
            cur_i, cur_j = self.your_tank.location
            self[cur_i,cur_j].occupancy = ''
            new_location = (cur_i, cur_j+1)
            if self.is_in_bounds(new_location[0], new_location[1]):
                self.your_tank.location = new_location
                self[self.your_tank.location].occupancy = 'your_tank'
            else: self[cur_i,cur_j].occupancy = 'your_tank'

        if pyxel.btnp(pyxel.KEY_D):
            cur_i, cur_j = self.your_tank.location
            self[cur_i,cur_j].occupancy = ''
            new_location = (cur_i+1, cur_j)
            if self.is_in_bounds(new_location[0], new_location[1]):
                self.your_tank.location = new_location
                self[self.your_tank.location].occupancy = 'your_tank'
            else: self[cur_i,cur_j].occupancy = 'your_tank'

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.your_bullet_list.append(Your_Bullet(self.your_tank.location, ))

    def draw_cell(self, i: int, j: int, x: int, y: int) -> None:
        if self[(i,j)].occupancy == 'your_tank':
            pyxel.blt(i*16, j*16, 1, 0, 0, 16, 16)
        if self[(i,j)].cell_type == 'stone':
            pyxel.blt(i*16, j*16, 1, 32, 32, 16, 16)

    def pre_draw_grid(self) -> None:
        pyxel.cls(0)

    def post_draw_grid(self) -> None:
        ...

BattleCity = App(GRID_SIZE)

BattleCity.run()





