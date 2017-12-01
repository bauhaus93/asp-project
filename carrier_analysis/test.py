#!/bin/python2

factory = lambda a, b: 1 if a + b == 1 else 0
warehouse_ok = lambda a, b: 1 if a + b == 2 else 0
warehouse_short = lambda a, b: 0 if a + b == 2 else 1
exporter = lambda a, b: 1 if a + b > 0 else 0

ok_str = lambda ok: "ok" if ok else "short"

def print_depositories():
    print "factory:"
    for i in range(0, 2):
        for j in range(0, 2):
            print i, j, factory(i, j)

    print "warehouse_ok:"
    for i in range(0, 2):
        for j in range(0, 2):
            print i, j, warehouse_ok(i, j)

    print "warehouse_short:"
    for i in range(0, 2):
        for j in range(0, 2):
            print i, j, warehouse_short(i, j)

    print "exporter:"
    for i in range(0, 2):
        for j in range(0, 2):
            print i, j, exporter(i, j)

def calc_town(s1, s2, s3, ok_w1 = 1, ok_w2 = 1, silent = True):
    if not silent:
        print "input:", s1, s2, s3
        print "w1_ok =", ok_w1, " w2_ok =", ok_w2
    f1 = factory(s1, s2)
    f2 = factory(s3, f1)

    if ok_w1:
        w1 = warehouse_ok(s3, f1)
    else:
        w1 = warehouse_short(s3, f1)

    if ok_w2:
        w2 = warehouse_ok(s1, s2)
    else:
        w2 = warehouse_short(s1, s2)

    e1 = exporter(w1, w2)

    if not silent:
        print "f1:", s1, s2, f1
        print "f2:", s3, f1, f2
        print "w1:", s3, f1, w1, ok_str(ok_w1)
        print "w2:", s1, s2, w2, ok_str(ok_w2)
        print "e1:", w1, w2, e1

        print "output:", f2, e1
    return (f2, e1)

#for a in range(0, 2):
#    for b in range(0, 2):
#        for c in range(0, 2):
#            for d in range(0, 2):
#                (t1_c1, t1_c2) = calc_town(1, 0, 1, ok_w1 = a, ok_w2 = b)
#                (t2_c1, t2_c2) = calc_town(0, 0, t1_c2, ok_w1 = c, ok_w2 = d)
#                if t1_c1 == 0 and t2_c1 == 0 and t2_c2 == 1:
#                    print "found result"
#                    print "t1: w1(%s), w2(%s)" % (ok_str(a), ok_str(b))
#                    print "t2: w1(%s), w2(%s)" % (ok_str(c), ok_str(d))


(t1_c1, t1_c2) = calc_town(1, 1, 1)
(t2_c1, t2_c2) = calc_town(1, 0, t1_c2)
print "outputs:"
print t1_c1, t1_c2
print t2_c1, t2_c2
