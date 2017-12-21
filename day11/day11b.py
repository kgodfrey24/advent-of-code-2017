def getDistance(route):
    n = route.count("n")
    ne = route.count("ne")
    se = route.count("se")
    s = route.count("s")
    sw = route.count("sw")
    nw = route.count("nw")

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

route = map(str.strip, open("input").read().split(","))

maxDistance = 0
while len(route) > 0:
    route = route[:-1]
    currentDistance = getDistance(route)
    if currentDistance > maxDistance:
        maxDistance = currentDistance

print maxDistance
