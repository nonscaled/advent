class Map:
    map = []
    size = 0
    overlap = 0
    def __init__(self, size) -> None:
        self.size = size
        self.map = [[0 for _ in range(self.size)] for _ in range(self.size)]

    #probably unnecessary, should only be called by addline anyway
    def markPoint(self, point):
        #y,x
        self.map[point[1]][point[0]] += 1

    def addLine(self, start, end):
        x1 = int(start[0])
        x2 = int(end[0])
        y1 = int(start[1])
        y2 = int(end[1])
    
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        if x1 == x2:
            linex = [x1]
        else:
            linex = [*range(x1, x2+1)]
        if y1 == y2:
            liney = [y1]
        else:
            liney = [*range(y1, y2+1)]
        #print(linex)
        #print(liney)
        for a in linex:
            for b in liney:
                #print("mark")
                self.markPoint([a,b])
                
    
    def scanMap(self) -> int:
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] > 1:
                    self.overlap += 1
        return self.overlap

    def printMap(self) -> None:
        for i in range(len(self.map)):
            print(self.map[i])

ex_lines = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip().split('\n')

def proc(lines):
    lines_proc = [[point[0].split(','), point[1].split(',')] for point in [line.split(" -> ") for line in lines]]
    for line in lines_proc:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            lines_proc.remove(line)
        if line in lines_proc:
            line.sort()
    #quickfix for last line bug
    lines_proc = lines_proc[:-1]
    
    print(lines_proc)
    size = int(max([c for a in lines_proc for b in a for c in b])) + 1
    #print(size)
    return lines_proc, size

def main():
    lines, map_size = proc(ex_lines)
    m = Map(map_size)
    for line in lines:
        m.addLine(line[0],line[1])
    m.printMap()
    print(m.scanMap())

main()