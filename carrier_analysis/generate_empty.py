#!/bin/python2

import random
import subprocess

towns = ["t1", "t1"]
depositories = ["f1", "f2", "w1", "w2", "e1"]
predicates = ["receiving1", "receiving2", "shipping"]

def try_it(towns, depositories, predicates, min_count, max_count):
    count = random.randint(min_count, max_count)
    done = []
    with open("test.obs", "w") as f:
        while len(done) < count:
            p = random.choice(predicates)
            t = random.choice(towns)
            d = random.choice(depositories)
            v = random.randint(0, 1)
            mask = p + t + d + str(v)
            if mask not in done:
                measurement = "%s(%s, %s, %d)." % (p, t, d, v)
                f.write(measurement + "\n")
                done.append(mask)


i = 0
while True:
    i += 1
    try_it(towns, depositories, predicates, 5, 30)
    out = subprocess.check_output(["dlv", "-silent", "-N=2", "-FD", "abd_carrier.dl", "abd.hyp", "abd_cstr.dl", "abd_fault.dl", "test.obs"])
    out = out.splitlines()

    if len(out) == 1:
        print out
        break
    if i % 1000 == 0:
        print i
