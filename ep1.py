import numpy as np
import re
import math

NUSP = [3,7,5,9,7,3,2]

def conta_transicao(lista, ocorrencia, tamanho):
    busca = '(?=' + ocorrencia + ')'
    return len(re.findall(busca,''.join(map(str, lista[:tamanho]))))
    
def _h(val):
    _alfa = NUSP[3] #9
    _beta = NUSP[4] #7
    _gama = NUSP[5] #3
    _delta = NUSP[6] #2
    
    if(val == 0):
        return _alfa/10
    if(val == 1):
        return _beta/10
    if(val == 11):
        return _gama/10
    if(val == 111):
        return _delta/10
    return 0    

T = ['0', '01', '011', '111']
X = [0,1,1]
m = 100
for t in range(0, m):
    #Procuro em X até encontrar um contexto de T 
    for i in range(1, len(X)):
        C = X[-i:]
        #print(t, i, C, len(X))
        if (''.join(map(str, C)) in T):
            break
    #Junta os elementos de C sequencialmente numa String e depois transforma num int
    H = _h(int(''.join(map(str, C))))
    #obtem um valor da Uniforme
    U = np.random.uniform(0.0, 1.0)
    print("t " + str(t) + " C " + str(C) + " H " + str(H) + " U " + str(U))
    if (U < H):
        X.append(0)
    else:        
        X.append(1)
#limpando X
X = X[3:103]
#X = [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
print(X)

print("="*5, "Item A", "="*5)
#Contando X 10
N_10_00 = conta_transicao(X, '00', 10)
N_10_01 = conta_transicao(X, '01', 10)
N_10_010 = conta_transicao(X, '010', 10)
N_10_011 = conta_transicao(X, '011', 10)
N_10_0110 = conta_transicao(X, '0110', 10)
N_10_0111 = conta_transicao(X, '0111', 10)
N_10_1111 = conta_transicao(X, '1111', 10)
N_10_1110 = conta_transicao(X, '1110', 10)

print(''.join(map(str, X[:10])))
print("N00 {} N01 {} N010 {} N011 {} N0110 {} N0111 {} N1111 {} N1110 {}".format( N_10_00, N_10_01, N_10_010, N_10_011, N_10_0110, N_10_0111, N_10_1111, N_10_1110))

#Contando X 100
N_100_00 = conta_transicao(X, '00', 100)
N_100_01 = conta_transicao(X, '01', 100)
N_100_010 = conta_transicao(X, '010', 100)
N_100_011 = conta_transicao(X, '011', 100)
N_100_0110 = conta_transicao(X, '0110', 100)
N_100_0111 = conta_transicao(X, '0111', 100)
N_100_1111 = conta_transicao(X, '1111', 100)
N_100_1110 = conta_transicao(X, '1110', 100)

print(''.join(map(str, X)))
print("N00 {} N01 {} N010 {} N011 {} N0110 {} N0111 {} N1111 {} N1110 {}".format( N_100_00, N_100_01, N_100_010, N_100_011, N_100_0110, N_100_0111, N_100_1111, N_100_1110))

print("="*5, "Item B", "="*5)
p_0_0 = NUSP[3]/10 #0.9
p_0_1 = 1 - NUSP[3]/10 # 1 - 0.9
p_01_0 = NUSP[4]/10 #0.7
p_01_1 = 1 - NUSP[4]/10 # 1 - 0.7
p_011_0 = NUSP[5]/10 # 0.3
p_011_1 = 1 - NUSP[5]/10 # 1 - 0.3
p_111_0 = NUSP[6]/10 # 0.2
p_111_1 = 1 - NUSP[6]/10 # 1 - 0.2

p_10 =  pow(p_0_0, N_10_00) * pow(p_0_1, N_10_01) \
      * pow(p_01_0, N_10_010) * pow(p_01_1, N_10_011) \
      * pow(p_011_0, N_10_0110) * pow(p_011_1, N_10_0111) \
      * pow(p_111_0, N_10_1110) * pow(p_111_1, N_10_1111)

log_p_10 =  (math.log(p_0_0) * N_10_00) + (math.log(p_0_1)* N_10_01) \
      + (math.log(p_01_0) * N_10_010) + (math.log(p_01_1) * N_10_011) \
      + (math.log(p_011_0) * N_10_0110) + (math.log(p_011_1) * N_10_0111) \
      + (math.log(p_111_0) * N_10_1110) + (math.log(p_111_1) * N_10_1111)


print("p_0_0 {} p_0_1 {} p_01_0 {} p_01_1 {} p_011_0 {} p_011_1 {} p_111_0 {} p_111_1 {} ".format(p_0_0, p_0_1, p_01_0, p_01_1, p_011_0, p_011_1, p_111_0, p_111_1))
print("P100 {} LogP100 {}".format(p_10, log_p_10))

print("="*5, "Item C", "="*5)
est_vero_N_10_00 = N_10_00 / (N_10_00 + N_10_01)
est_vero_N_10_01 = N_10_01 / (N_10_00 + N_10_01)
est_vero_N_10_010 = N_10_010 / (N_10_010 + N_10_011)
est_vero_N_10_011 = N_10_011 / (N_10_010 + N_10_011)
est_vero_N_10_0110 = N_10_0110 / (N_10_0110 + N_10_0111)
est_vero_N_10_0111 = N_10_0111 / (N_10_0110 + N_10_0111)
est_vero_N_10_1110 = N_10_1110 / (N_10_1110 + N_10_1111)
est_vero_N_10_1111 = N_10_1111 / (N_10_1110 + N_10_1111)

print("ver00 {} ver01 {} ver010 {} ver011 {} ver0110 {} ver0111 {} ver1110 {} ver1111 {}".format(est_vero_N_10_00, est_vero_N_10_01, est_vero_N_10_010, est_vero_N_10_011, est_vero_N_10_0110, est_vero_N_10_0111, est_vero_N_10_1110, est_vero_N_10_1111))

print("="*5, "Item D", "="*5)
est_vero_N_100_00 = N_100_00 / (N_100_00 + N_100_01)
est_vero_N_100_01 = N_100_01 / (N_100_00 + N_100_01)
est_vero_N_100_010 = N_100_010 / (N_100_010 + N_100_011)
est_vero_N_100_011 = N_100_011 / (N_100_010 + N_100_011)
est_vero_N_100_0110 = N_100_0110 / (N_100_0110 + N_100_0111)
est_vero_N_100_0111 = N_100_0111 / (N_100_0110 + N_100_0111)
est_vero_N_100_1110 = N_100_1110 / (N_100_1110 + N_100_1111)
est_vero_N_100_1111 = N_100_1111 / (N_100_1110 + N_100_1111)

print("ver00 {} ver01 {} ver010 {} ver011 {} ver0110 {} ver0111 {} ver1110 {} ver1111 {}".format(est_vero_N_100_00, est_vero_N_100_01, est_vero_N_100_010, est_vero_N_100_011, est_vero_N_100_0110, est_vero_N_100_0111, est_vero_N_100_1110, est_vero_N_100_1111))

p_100 =  pow(p_0_0, N_100_00) * pow(p_0_1, N_100_01) \
      * pow(p_01_0, N_100_010) * pow(p_01_1, N_100_011) \
      * pow(p_011_0, N_100_0110) * pow(p_011_1, N_100_0111) \
      * pow(p_111_0, N_100_1110) * pow(p_111_1, N_100_1111)
log_p_100 =  (math.log(p_0_0) * N_100_00) + (math.log(p_0_1)* N_100_01) \
      + (math.log(p_01_0) * N_100_010) + (math.log(p_01_1) * N_100_011) \
      + (math.log(p_011_0) * N_100_0110) + (math.log(p_011_1) * N_100_0111) \
      + (math.log(p_111_0) * N_100_1110) + (math.log(p_111_1) * N_100_1111)


print("P100 {} LogP100 {}".format(p_100, log_p_100))

print("="*5, "Item E", "="*5)

#lembrando que X já está "limpo"
_K = conta_transicao(X, '0', 100)
print("K {} ".format(_K))

print("="*5, "Item F", "="*5)

N_100_01 = conta_transicao(X, '01', 100)
P_K = N_100_01 / _K
print("P_K {} ".format(P_K))