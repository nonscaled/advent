"""
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
"""

ex_hmap = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip().split('\n')

#preprocessing
def proc(hm):
    x = [list(map(int, list(h))) for h in hm]
    for z in x:
        print(z)
    return x


def low(pm):
    low_horizontal = []
    low_vertical = []
    low_corner = []
    risk = 0

    end = len(pm[0])
    bot = len(pm)

    #top left, top right, bottom left, bottom right
    if pm[0][0] < pm[0][1] and pm[0][0] < pm[1][0]:
        low_corner.append((0,0))
    if pm[0][end-1] < pm[0][end-2] and pm[0][end-1] < pm[1][end-1]:
        low_corner.append((0, end-1))
    if pm[bot-1][0] < pm[0][1] and pm[bot-1][0] < pm[bot-2][0]:
        low_corner.append((bot-1, 0))
    if pm[bot-1][end-1] < pm[bot-1][end-2] and pm[bot-1][end-1] < pm[bot-2][end-1]:
        low_corner.append((bot-1, end-1))
    
    print(low_corner)
    for y in range(1, len(pm)):
        for x in range(1, len(pm[0])):
            if x-2 < 0:
                if pm[y][x-1] < pm[y][x]:
                    low_horizontal.append((y, x-1))
            if y-2 < 0:
                if pm[y-1][x] < pm[y][x]:
                    low_vertical.append((y-1, x))
            else:
                if pm[y][x-1] < pm[y][x-2] and pm[y][x-1] < pm[y][x]:
                    low_horizontal.append((y, x-1))
                if pm[y-1][x] < pm[y-2][x] and pm[y-1][x] < pm[y][x]:
                    low_vertical.append((y-1, x))
                
            

                
    print(low_vertical)
    #print([pm[a][b] for (a,b) in low_vertical])
    print(low_horizontal)
    #print([pm[a][b] for (a,b) in low_horizontal])

    
    low = list(set(low_horizontal).intersection(set(low_vertical)))
    for c in low_corner:
        low.append(c)
    print(low)
    print([pm[a][b] for (a,b) in low])
    
    for point in low:
        y = point[0]
        x = point[1]
        risk += pm[y][x] + 1
    
    print(risk)

low(proc(ex_hmap))