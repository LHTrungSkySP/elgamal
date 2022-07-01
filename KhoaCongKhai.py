from cacPhepToan import *
class KhoaCongKhai():
    def __init__(self, p, alpha,khoaBiMat):
        self.p = p
        self.alpha = alpha
        self.khoaBiMat=khoaBiMat
        self.beta=binhPhuongNhan(alpha,khoaBiMat.a,p)