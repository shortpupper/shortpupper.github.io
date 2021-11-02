class val:
    def __init__(self, start, increments, vals, repet):
        self.start = start
        self.increments = increments
        self.vals = vals
        self.repet = repet


stats = val(-4, -2.5, 2, 1)



example_string = "a"+str(stats.vals)
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
sru = (example_string.translate(SUB))


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

'''
start_vaule = 19
sub_n = 2
common_repeat = 6


q_strat   = (sru+"=")
q_subs    = sub_n-1
q_string  = common_repeat
q_1       = q_string*q_subs
q_2       = q_strat+str(q_1+start_vaule)



t1 = (sub_val+"="+str(common_repeat)+"("+str(sub_n)+str(-1)+")"+"+"+str(start_vaule))
t2 = (sub_val+"="+str(common_repeat)+"("+str(sub_n-1)+")"+"+"+str(start_vaule))
t3 = (q_strat+str(q_1)+"+"+str(start_vaule))
t4 = q_2

print(t1)
print(t2)
print(t3)
print(t4)
'''


#print(stats.start)
print(y2)
print(y1)
print(y4)
print(y3)
