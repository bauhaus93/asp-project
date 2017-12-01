#!/bin/python2

import random
import subprocess

towns = ["t1", "t2"]
depositories = ["f1", "f2", "w1", "w2", "e1"]
predicates = ["receiving1", "receiving2", "shipping"]


def add_random_measurement(towns, depositories, predicates, min_count, max_count, data = set([])):
    count = random.randint(min_count, max_count)
    count += len(data)

    while len(data) < count:
        p = random.choice(predicates)
        t = random.choice(towns)
        d = random.choice(depositories)
        v = random.randint(0, 1)
        mask = (p, t, d, v)
        data.add(mask)

    with open("test.obs", "w") as f:
        for mask in data:
            measurement = "%s(%s, %s, %d)." % mask
            f.write(measurement + "\n")
    return data

i = 0
lastSuccess = []
lastLineCount = 100000000000
while True:
    i += 1
    data = add_random_measurement(towns, depositories, predicates, 1, 2)
    out = subprocess.check_output(["dlv", "-silent", "-N=2", "-FD", "abd_carrier.dl", "abd.hyp", "abd_cstr.dl", "abd_fault.dl", "test.obs"])
    out = out.splitlines()
    if "Diagnosis:" in out:
        print "got empty, output line count: ", len(out)
        if len(out) < lastLineCount:
            lastSuccess = data
            lastLineCount = len(out)
        if len(out) == 1:
            break
    if i % 100 == 0:
        print i
