import math
from tkinter import *
from cacPhepToan import *
class elgamal():          
    def NgauNhienK(p):   
        k= SoNgauNhien(2,p-1)
        while(GCD(p-1,k)!=1 or nghichDaoModulo(k,p-1)==-1 or k<=1):
            k=(k + 2) % ( p- 1)
            if(k % 2 == 0):
                k=(k+1)%(p-1)
        return k
    def maHoa(k,m,K_pr,K_pub):
        y1=binhPhuongNhan(K_pub.alpha,k,K_pub.p)
        print(nghichDaoModulo(k,K_pub.p-1))
        y2=(nghichDaoModulo(k,K_pub.p-1)*(m-K_pr.a*y1))%(K_pub.p-1)
        return  y1,y2
    def giaiMa(m,S1,S2,K_pub):
        V1=binhPhuongNhan(K_pub.alpha,m,K_pub.p)
        V2=(binhPhuongNhan(K_pub.beta,S1,K_pub.p) * binhPhuongNhan(S1,S2,K_pub.p))% K_pub.p
        return V1,V2
    def binhPhuongNhan(self,x,soMu_n,soModulo_m):
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
        print(b)
        kq=1
        for i in range(0,k):
            kq=(kq*kq) % soModulo_m
            if (b[i] == 1):
                kq = (kq * x) % soModulo_m
        return kq
    def check_prime_number(self,n):
        if (n <2):
            return False  #Số nhỏ hơn 2 không phải số nguyên tố => trả về 0
        
        #Sử dụng vòng lặp while để kiểm tra có tồn tại ước số nào khác không
        for p in range(2, round(math.sqrt(n))+1):
            if n % p == 0:
                return False #Chỉ cần tìm thấy 1 ước số là đủ và thoát vòng lặp
        return True
        
        
        
