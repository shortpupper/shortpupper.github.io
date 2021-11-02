class val:
    def __init__(self, start, increments, vals, repet):
        self.start = start
        self.increments = increments
        self.vals = vals
        self.repet = repet


#start1       = input("Enter start vaule")
#increments1  = input("Enter how the the vaule go's")
#vals1        = input("Enter what n is")
#repet1       = input("Enter how many times n go's")



stats = val(-4, -2.5, 2, 10)



b1 = stats.vals
b2 = str(b1)
z1 = stats.repet
z2 = stats.vals


length = z1
maxlength = length
its = 1

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
example_string = "a"+b2
sru = (example_string.translate(SUB))

while z1 <= maxlength:
  print(sru)
  if z2 >= length:
    break
  z2 += 1



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
print(y3)