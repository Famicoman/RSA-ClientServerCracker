#Cracking Program 0.1
#Mike Dank
#02/2012

import random, math, fractions

a=0;
b=0;
c = 5183
e = 1499

def mod_inverse(e, m):
	return (e^(totient(m)-1))%m

def totient(n):
    result = 0
    for i in range(1,(n-1)):
        if fractions.gcd(i,n)==1:
            result = result + 1
    return result

x = False
while x==False:
	for i in range(2,c):
		for j in range(2,c):
			if (i*j)==c:
				a=i;
				b=j;
				x=True

m = (a-1)*(b-1)
d = mod_inverse(e,m)
print "priv key: "+str(d)
