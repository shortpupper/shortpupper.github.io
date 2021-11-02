import atexit
import os
import sys


class val:
    def __init__(self, start, increments, vals, repet):
        self.start = start
        self.increments = increments
        self.vals = vals
        self.repet = repet

class inputs_:
    def __unicode__(self, e, f):
        self.e = "ys"
        self.f = " "

texts = "s"
inputs = inputs_()
print(inputs)

runcommand   = input(">>")

if runcommand == "math" or "Math":
    runcommands = input("Math()>>")
    if runcommands == "raf":
        start1 = input("Enter start vaule:")
        increments1 = input("Enter what the increments are:")
        vals1 = input("Enter what n is:")
        repet1 = input("Enter how many times to repeat from n:")
        yesorno = input("show how to do propblem:")
        if yesorno:
            print("k")
        stats = val(int(start1), int(increments1), int(vals1), int(repet1))
        z1 = stats.repet
        z2 = stats.vals
        length = z1
        maxlength = length
        its = stats.vals
        while z1 <= maxlength:
            SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
            SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
            b1 = stats.vals
            b2 = str(b1)
            example_string = "a"+str(its)
            sru = (example_string.translate(SUB))
            x1 = "="
            x15 = its
            x2 = x15 - 1
            x3 = stats.increments
            x4 = "("
            x5 = ")"
            x6 = "+"
            x7 = str(x15) + str(-1)
            x8 = sru
            x9 = stats.start
            x10 = x8 + x1
            x11 = x6 + str(x9)
            x12 = str(x3) + x4 + str(x2) + x5
            x13 = str(x3) + x4 + x7 + x5
            x14 = x2 * x3
            x15 = str(x14 + x9)
            y1 = x10 + x12 + x11
            y2 = x10 + x13 + x11
            y3 = x10 + x15
            y4 = x10 + str(x14) + str(x11)
            print(y3)
            if z2 >= length:
              break
            z2  += 1
            b1  += 1
            its += 1
elif runcommand == "help":
    print("yes")
else:
    print("error")



"""
x1 = "="
x2 = stats.vals-1
x3 = str(stats.increments)
x4 = "("
x5 = ")"
x6 = "+"
x7 = str(stats.vals)+str(-1)
x8 = sru
x9 = stats.start
x10 = x8+x1
x11 = x6+str(x9)
x12 = x3+x4+str(x2)+x5
x13 = x3+x4+x7+x5
x14 = x2*stats.increments
x15 = str(x14+stats.start)
y1 = x10+x12+x11
y2 = x10+x13+x11
y3 = x10+x15
y4 = x10+str(x14)+str(x11)
"""

"""
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

"""

#print(stats.start)
#print(y2)
#print(y1)
#print(y4)
#print(y3)
