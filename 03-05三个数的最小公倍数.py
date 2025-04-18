a = int(input())
b = int(input())
c = int(input())
########## Begin ##########
from math import gcd
gcd_ab = gcd(a,b)
lcm_ab = (a * b) //gcd_ab
gcd_ag = gcd(lcm_ab,c)
lcm_abc = (lcm_ab * c)//gcd_ag
print(lcm_abc)

########## End ##########