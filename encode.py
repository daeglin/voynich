#!/usr/bin/python
# This is a prototype of an algorithm generating Voynich-like ciphertext.
# Preprint of the paper explaining why I believe this is the right solution
# to the puzzle is comming soon.
# Copyright (C) Michal Benes 2014
# michal.benes.cz@gmail.com
#
# History:
# January 12th 2014 - First version
# January 14th 2014 - Special version

import sys

line = sys.stdin.readline().strip()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "EITAUSRNMOCDLPQBVHGFXJYZKW"
alphabetex = alphabet + alphabet.lower()


leftrule = {}
n = 0
for i in alphabetex:
    for j in alphabet:
        leftrule[i + j] = n
        n += 1

rightrule = []
for i in range(len(alphabetex)):
    for j in range(len(alphabetex)-i):
        rightrule.append(alphabetex[i] + alphabetex[j])

for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        rightrule.append(alphabet[-1] + alphabet[j])

s = "A"
res = ""
for a in line:
    idx = leftrule[s+a]
    res += rightrule[idx][0]
    s = rightrule[idx][1]

res += s
print res
