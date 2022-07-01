import random


def heSo(n):
    s = 0
    while((n & 1) == 0):
        s += 1
        n >>= 1
    return s, n

# x^n mod m
def binhPhuongNhan(x,soMu_n,soModulo_m):
    # chuyển số mũ sang nhị phân
    b=[]
    k=0
    while True:
        b.append(soMu_n % 2)
        k+=1
        soMu_n=soMu_n//2
        if soMu_n ==0:
            break
    b.reverse()
    kq=1
    for i in range(0,k):
        kq=(kq*kq) % soModulo_m
        if (b[i] == 1):
            kq = (kq * x) % soModulo_m
    return kq


# kiểm tra n ( một so rất lớn có phải nguyên tố hay không)
def laSoNT(n):
    if(n<2):
        return False
    if((n&1) == 0):
        return n==2
    heso=heSo(n-1)
    s=heso[0]
    d=heso[1]
    ran=[2,3,5,7,23,11,17,61]
    laSoNT=True
    for e in ran:
        if(checkMillerRabin(s,d,n,e)==False):
            laSoNT=False
    return laSoNT

# tính nghịch đảo
def nghichDaoModulo(a,m):
    mod=m
    y0=0
    y1=1
    y=-1
    while(a>1):
        r=m%a
        if(r==0):
            break
        q=m//a
        y=y0-y1*q
        m=a
        a=r
        y0=y1
        y1=y
    if(a>1):
        return -1
    return (y+mod)%mod

def GCD(a,b):
    if(b!=0):
        return GCD(b,a%b)
    else:
        return a
def SoNgauNhien(a,b):
    return random.randint(a, b)
def checkMillerRabin(s, d, n, a):
    if n == a:
        return True
    p = binhPhuongNhan(a, d, n)
    if(p == 1):
        return True
    while(s > 0):
        if(p == n-1):
            return True
        p = p*p % n
        s -= 1
    return False