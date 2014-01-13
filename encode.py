#!/usr/bin/python
# This is a prototype of an algorithm generating Voynich like ciphertext.
# Preprint of a paper explaing the why I believe this is the right solution
# to the puzzle is comming soon.
# Copyright (C) Michal Benes January 13th 2014

import sys

line = sys.stdin.readline().strip()

#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"
alphabet = "EITAUSRNMOCDLPQBVHGFXJYZKW123456"

code = {}
n = 0
for i in alphabet:
    code[i] = n
    n += 1

class Coder:
    def __init__(self):
        self.fr = [10,5]
        self.st = 0.0

    def update(self, v):
        self.fr[v] += 1
        q = float(self.fr[0])/(self.fr[0]+self.fr[1])
        if v > 0:
            self.st += 1.0

        if self.st > 10.0:
            self.st = 0.0

        if self.st >= 1.0:
            res = 1
            self.st -= q
        else:
            res = 0

        return res

res = ""
coders = []
for i in range(5):
    coders.append(Coder())

for a in line:
    r = 0
    n = 0
    c = code[a]
    for i in [1, 2, 4, 8, 16]:
        r = r * 2 + coders[n].update((c & i) / i)
        n += 1
    res += alphabet[r]

print res
#for i in range(5):
#    print coders[i].hit, coders[i].miss

