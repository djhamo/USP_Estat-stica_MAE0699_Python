import numpy as np
import math
#import pylatex

def p(theta, k):
    pk = np.exp(-theta) * ((math.pow(theta,k))/(np.math.factorial(k)))
    return pk


def ramificacao(M, X, theta):
    n = 0
    while (X[n] != 0 and n <= (M - 1)):
        n += 1
        print("Inicio: {}".format(n))
        j = 1
        X[n] = 0
        while (j <= X[n - 1]):
            U = np.random.uniform()
            i = 0
            soma = p(theta, i)
            while (U >= soma):
                i += 1
                soma += p(theta, i)

            X[n] += i
            j += 1


def qk(alpha, k):
    q = (1-alpha)*math.pow(alpha,k)
    return q

def epidemia(M,X,alpha,p):
    n = 0
    while (X[n]!=0 and n<=M-1):
        n += 1
        print("Inicio: {}".format(n))
        X[n] = 0
        for i in range(X[n-1]):
            k = 0 #número de contatos
            u = np.random.uniform()
            #print("u1 {}".format(u))
            contatos = qk(alpha, k)
            while(u>=contatos):
                k += 1
                contatos += qk(alpha, k)
            s = 0
            j = 0
            for j in range(k):
                u = np.random.uniform()
                #print("u2 {}".format(u))
                if(u<=p):
                    s += 1
            X[n] += s
            #print("X[{}] = {}".format(n, X[n]))


r1 = np.zeros(21, int)
r1[0] = 10

ramificacao(20,r1,0.2)

print(r1)

r2 = np.zeros(21,int)
r2[0] = 10

ramificacao(20,r2,2.2)

print(r2)

e1 = np.zeros(21, int)
e1[0] = 10

epidemia(20,e1,0.9,0.3)

print(e1)

e2 = np.zeros(20,int)
e2[0] = 10

epidemia(21,e2,0.1,0.3)

print(e2)