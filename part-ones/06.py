#not this
class Feesh:
    t = 0
    init_t = 0

    def __init__(self, time) -> None:
        pass

    def nextDay(self):
        if self.t > 0:
            self.t -= 1
        else:
            self.t = 6 #hardcode week zero inclusive
            Feesh(self.init_t + 2)

#may make sense w/o object model
def feesh():
    ex_fishlist = [3,4,3,1,2]    
    fishlist = ex_fishlist
    days = 20
    while days:
        while 0 in fishlist:
            #need nums one higher because new fish exempt from subtraction on day of spawning
            fishlist[fishlist.index(0)] = 7 
            fishlist.append(9)
        fishlist = [fish - 1 for fish in fishlist]
        days -= 1
    print(fishlist)
    count = len(fishlist)
    print(count)

#feesh()

#some compression (# of occurrences of #)
def feesh2():
    ex_fishlist = [3,4,3,1,2] 
    ex_fish2 = [[x, 0] for x in range(0,10)]
    for f in ex_fishlist:
        ex_fish2[f][1] += 1
    
    days = 80
    while days:
        while ex_fish2[0][1] > 0:
            ex_fish2[7][1] += 1
            ex_fish2[9][1] += 1
            ex_fish2[0][1] -= 1

        #print(ex_fish2)   
        for fish in ex_fish2[1:]:
            ex_fish2[fish[0] - 1][1] = fish[1]
        ex_fish2[9][1] = 0 
        days -= 1
    print(ex_fish2)
    count = sum([f[1] for f in ex_fish2])
    print(count)

feesh2()


def proc(inp):
    return inp.split(',')