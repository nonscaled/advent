from dataclasses import dataclass, asdict

ex_grid = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip().split('\n')

#TODO: rewrite to take actual advantage of dataclass features (auto getters and setters)
#      as well as proper labeling of internal fields
#      or just use property decorator next time
@dataclass
class Octo:

    pos: tuple
    energy: int
    highlighted: bool = False
    has_flashed: bool = False #this step

    def __init__(self, pos, val) -> None:
        assert len(pos) == 2
        self.pos = pos
        self.energy = val

        
    def adj(self, pos, max_x, max_y) -> list[tuple]:
        x = pos[0]
        y = pos[1]
        #assert x > 0 and y > 0 # and x <= grid_len and y <= grid_len
        adj = [(a, b) for a in (x, x-1, x+1) for b in (y, y-1, y+1)]
        adj.remove((x,y))
        #this filter v convenient
        adj = list(filter(lambda p: 0 <= p[0] < max_x and 0 <= p[1] < max_y, adj))
        return adj #adj as dubiously ordered list of tuples may need to be reworked
    
    def energy_reset(self) -> None:
        self.energy = 0
    
    def energy_bump(self) -> None:
        self.energy += 1
    
    def highlight(self):
        self.highlighted = True

    def flash(self) -> None:
        #may want to put majority of flash logic in step
        #or well just the parts with side effects
        #change condition to assertion, force conditions to grid function(s)
        assert self.has_flashed == False and self.energy > 9
        self.highlight()
        self.energy_reset()
        self.has_flashed = True
    
    def clear_flash(self):
        self.has_flashed = False

    def getloc(self) -> tuple:
        return self.pos
    
    def setloc(self, pos) -> None:
        self.x = pos[0]
        self.y = pos[1]

    def gethighlighted(self) -> bool:
        return self.highlighted
    
    def getenergy(self) -> int:
        return self.energy

    def getflash(self) -> bool:
        return self.has_flashed

    def clear_highlight(self):
        self.highlighted = False

    #for prettier printing
    def __repr__(self):
        o = asdict(self)
        o["highlighted"] = int(o["highlighted"])
        o["has_flashed"] = int(o["has_flashed"])
        return "{pos}|{energy}|{highlighted}|{has_flashed}".format(**o) 

#not fixing this anytime soon ig
class Grid:
    grid = []
    flashcount = 0

    def __init__(self, g):
        #list comp a better way to populate the grid
        self.grid = [[Octo((i,j), g[i][j]) for j in range(len(g[0]))] for i in range(len(g))]

    #redundant??
    def adj(self, pos, max_x, max_y) -> list[Octo]:
        x = pos[0]
        y = pos[1]
        #assert x > 0 and y > 0 # and x <= grid_len and y <= grid_len
        adj = [(a, b) for a in (x, x-1, x+1) for b in (y, y-1, y+1)]
        adj.remove((x,y))
        #this filter v convenient
        adj = list(filter(lambda p: 0 <= p[0] < max_x and 0 <= p[1] < max_y, adj))
        adj = [self.grid[pos[0]][pos[1]] for pos in adj] #add separate list of oct objects, rip perf
        return adj #adj as dubiously ordered list of tuples may need to be reworked

    #oh highlights arent in spec forgor           
    def step(self):
        self.clear_flash()
        self.clear_highlight()
        self.grid_bump() # first bullet point


        #TODO: Extend ranges and handle corner cases // done
        #tbh i might be missing something here, will double check logic w/ testcases
        #yeah most logic has to be factored out to meet behavior, conditionality breaks spec
        """
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[0])):
                current_oct = self.grid[i][j]
                if current_oct.getenergy() > 9 and not current_oct.getflash():
                    current_oct.flash()
                    adj = current_oct.adj(current_oct.getloc(), len(self.grid), len(self.grid[0]))
                    for oct_pos in adj:
                        adj_oct = self.grid[oct_pos[0]][oct_pos[1]]
                        adj_oct.energy_bump()
                        if adj_oct.getenergy() > 9 and not adj_oct.getflash():
                            adj_oct.flash()
        """

        self.flash_update()
        self.count_flash()
        
    #do the thing recursively
    def flash_update(self):
        self.flash_pass() #update full grid state
        #print(self.grid)
        for oct in self.flashed(): #get updated grid state
            adj = self.adj(oct.getloc(), len(self.grid), len(self.grid[0])) #get adjacent to updated octs
            for oct_adj in adj:
                if oct_adj.getenergy() > 9 and not oct_adj.getflash(): #check adjacent criteria 
                    self.flash_update() #recurse

    def clear_flash(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.grid[row][col].clear_flash()

    def count_flash(self):
        fc = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                fc += self.grid[row][col].getflash()
        self.flashcount += fc        

    def getflash(self):
        return str(self.flashcount)

    def clear_highlight(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.grid[row][col].clear_highlight()
    
    def grid_bump(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.grid[row][col].energy_bump()
    
    def flash_pass(self):
        #wonder if this can be done recursively
        #flashes everything on the grid that hits the criteria
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col].getenergy() > 9 and not self.grid[row][col].getflash(): #flash constraint here
                    self.grid[row][col].flash()

    #check is for flash but everything flashed is highlit, will get copied for flash though    
    def highlit(self):
        highlit = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col].gethighlighted():
                    highlit.append(self.grid[row][col].getloc())
        return highlit
    
    def flashed(self):
        flashed = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col].getflash():
                    flashed.append(self.grid[row][col])
        return flashed

    def __repr__(self) -> str:
         return "\n".join(" ".join(repr(o) for o in r) for r in self.grid) #sneaky double join
        

def main(stepcount):
    inp = [list(map(int, list(x))) for x in ex_grid]
    g = Grid(inp)
    #print(g)
    #print(" ")
    for _ in range(stepcount):
        g.step()
        #print(g)
        print(str(g.getflash()) + '\n')


main(3)
