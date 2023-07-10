# GTP to Tidal rule:
# "e2 -32 a2 -27 d3 -22 g3 -17 b3 -13 e4 -8"

# 1,0 to -8
# 2,0 to -13
# 3,0 to -17
# 4,0 to -22
# 5,0 to -27
# 6,0 to -32

mp = [0, -8, -13, -17, -22, -27, -32]

def g(s):
    x = s.split()
    for i in x:
        a = int(i.split(",")[0])
        b = int(i.split(",")[1])
        print(mp[a] + b, end=" ")
    print("")
        