#!/usr/bin/python
# This is a prototype of an algorithm generating Voynich-like ciphertext.
# Preprint of the paper explaining why I believe this is the right solution
# to the puzzle is comming soon.
# Copyright (C) Michal Benes 2014
# michal.benes.cz@gmail.com
#
# History:
# January 12th 2014 - First version
# January 14th 2014 - Working version

import sys

line = sys.stdin.readline().strip()

CUT = 10  # >= 8
alphabet = "EITAUSRNMOCDLPQBVHGFXJYZ"
alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

value = {}
base = 0
for i in alphabet:
    mult = 1
    if i >= CUT:
        mult = 2
    value[i] = (base, mult)
    base += mult

state = 0
mult = 1
res = ""
for a in line:
    v = value[a]
    state = state * base * mult + v[0] * mult
    c = state / mult
    res += alphabet2[c]
    state = state - c * mult

    mult *= v[1]

    while mult > 1 and state % 2 == 0:
        mult /= 2
        state /= 2

    if mult > 1024 * 1024:
        mult /= 2
        res += "1"

print res
