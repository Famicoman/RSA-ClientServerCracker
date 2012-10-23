#Client Program 0.1
#Mike Dank
#02/2012

import random, math
import fractions
import sys               
import socket
import string
import time
import threading

#Make socket
clisock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
clisock.connect( ("127.0.0.1", 12347) )

c = 5183
d = 421
e = 1499
exit=0

class sending(threading.Thread):
    def run(self):
        send = ""
        while send.startswith("/q")==False:
            send= sys.stdin.readline()
            sendlist = list(send)
            for i in sendlist[:]:
                i=endecrypt(ord(i),e,c)
            clisock.send(repr(sendlist)) #Send command
        exit = 1

class receiving(threading.Thread):
    def run(self):
        rec = ['0','0']
        while exit==0:
            rec = eval(clisock.recv(1024))
            if rec != ['0','0']:
                for i in rec[:]:
                    i=str(endecrypt(ord(i),d,c))
                out = ''.join(rec)
                print out #Print message from server

def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b/a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def mod_inverse(e, m):
	return (e^(totient(m)-1))%m

def coprime(x):
    gen = []
    for i in xrange(2,x):
        if fractions.gcd(i,x) == 1:
            gen.append(i)
    random.shuffle(gen)
    return gen[0]


def totient(n):
    result = 0
    for i in range(1,(n-1)):
        if fractions.gcd(i,n)==1:
            result = result + 1
    return result

def modulo(a,b,c):
	return math.pow(a,b)%c

def endecrypt(msg_or_cypher,key,c):
    return (msg_or_cypher**key)%c

def is_prime(n):
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def rando(x,y):
	randy = random.randint(x,y)
	temp=0
	while temp==0:
		if is_prime(randy)==True:
			temp=1
		else:
			randy = random.randint(x,y)
	return randy

print "public: ( "+ str(e) +" , "+ str(c) +" )"
print "private: ( "+ str(d) +" , "+ str(c) +" )"
print "type to send an excrypted message."

s = sending()
r = receiving()
s.start()
r.start()
s.join()
r.join()

clisock.close()