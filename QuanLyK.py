from KhoaCongKhai import *
from KhoaBiMat import *
from cacPhepToan import *
class QuanLyKhoa():
    def __init__(self, p=1, alpha=1,a=1):
        self.khoaBiMat = KhoaBiMat(a)
        self.khoaCongKhai = KhoaCongKhai(p,alpha,self.khoaBiMat)
        
    def GetRandomElgammalManaged():
        tam=[1,3,7,9]
        p=random.randint(80<<500, 100<<500)*10+tam[random.randint(0, 3)]
        while(laSoNT(p)==False):
            p=p+10
        alpha=random.randint(1<<500, 100<<500-1)
        a=random.randint(2<500, 100<<500-2)
        return QuanLyKhoa(p,alpha,a)
    def Verific(x):
        return True 