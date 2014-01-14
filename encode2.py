#!/usr/bin/python
# This is a prototype of an algorithm generating Voynich like ciphertext.
# Preprint of the paper explaing why I believe this is the right solution
# to the puzzle is comming soon.
# Copyright (C) Michal Benes 2014
#
# History:
# January 12th 2014 - First version
# January 13th 2014 - Another experiment

import sys

line = sys.stdin.readline().strip()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "EITAUSRNMOCDLPQBVHGFXJYZKW"
#alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabc"
alphabet2 = "ABCDEFGHIJKLMNOPQRSTUV"

value = {}
n = 0
for i in alphabet:
    value[i] = float(n)
    n += 1

state = 0.0
res = ""
for a in line:
    if True or value[a] > 3:
        state = (state + value[a] / len(alphabet)) * len(alphabet2)
    else:    
        state = (state + value[a] / len(alphabet) / 3.0) * len(alphabet2)
    s = int(state)
    if s >= len(alphabet2):
        res += str(s / len(alphabet2))
    res += alphabet2[s%len(alphabet2)]
    state -= s 

print res
