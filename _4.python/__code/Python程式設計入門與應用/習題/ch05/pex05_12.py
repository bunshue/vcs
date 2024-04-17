# Filename: pex05_12.py
def phi(n):
    presult = 0
    ptemp = 1
    for i in range(1, n + 1, 1):
        presult = presult+ptemp/(2 * i - 1) 
        ptemp = -1*ptemp
    presult = 4*presult
    return presult

print(phi(900))