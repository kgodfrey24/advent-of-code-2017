route = map(str.strip, open("input").read().split(","))

n = route.count("n")
ne = route.count("ne")
se = route.count("se")
s = route.count("s")
sw = route.count("sw")
nw = route.count("nw")

def getDistance():
    # clean n - s
    mv = min(n, s)
    n -= mv
    s -= mv

    # clean ne - sw
    mv = min(ne, sw)
    ne -= mv
    sw -= mv

    # clean nw - se
    mv = min(nw, se)
    nw -= mv
    se -= mv

    # reduce n - se to ne
    mv = min(n, se)
    n -= mv
    se -= mv
    ne += mv

    # reduce n - sw to nw
    mv = min(n, sw)
    n -= mv
    sw -= mv
    nw += mv

    # reduce s - ne to se
    mv = min(s, ne)
    s -= mv
    ne -= mv
    se += mv

    # reduce s - nw to sw
    mv = min(s, nw)
    s -= mv
    nw -= mv
    sw += mv

    # reduce sw - se to s
    mv = min(sw, se)
    sw -= mv
    se -= mv
    s += mv

    # reduce ne - nw to n
    mv = min(ne, nw)
    nw -= mv
    ne -= mv
    n += mv

    return n + ne + se + s + sw + nw

print "n  " + str(n)
print "ne " + str(ne)
print "se " + str(se)
print "s  " + str(s)
print "sw " + str(sw)
print "nw " + str(nw)
print "---"
print
