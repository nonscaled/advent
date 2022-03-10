ex_rep = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

def rot(rep):
    g = []
    h = []
    for i in range(len(rep[0])):
        l = [bin[i] for bin in rep]
        g.append(max(set(l), key = l.count))
        h.append(min(set(l), key = l.count))
    gam = int(''.join(g),2)
    eps = int(''.join(h),2)
    print(gam * eps)


rot(ex_rep)
