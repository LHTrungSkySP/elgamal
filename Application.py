
import base64
import hashlib
from tkinter import *
from tkinter import filedialog as fd
from numpy import delete
from cacPhepToan import *
from QuanLyK import *
from KhoaBiMat import *
from KhoaCongKhai import *
from ChuKyEl import *
from elgamal import *
class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.config(self,background="#33CCFF")  
        self.parent = parent
        self.createKey_UI()
    quanlykhoaElgamal=QuanLyKhoa()
    chuKyElgamal=ChuKyElgamal()
    VBduocKy=""
    path=""
    noiDungChuKy=""
    def createKey_UI(self):  
        self.parent.title("Mã hóa Elgamal")
        self.pack(fill=BOTH, expand=1)
        strX=StringVar(None,value="")
        strP=StringVar(None,value="")
        strAlpha=StringVar(None,value="")
        strB=StringVar(None,value="")
        strK=StringVar(None,value="")
        strS1=StringVar(None,value="")
# infor
        lf_inf=LabelFrame(self, text="Thông tin sinh viên",height=180,width=350,background='#96D6FF')
        lf_inf.place(x=10,y=10)
        lb_infTen=Label(lf_inf,text="ĐỀ TÀI 4: Tìm hiểu về chữ kí điện tử ElGamal và viết\n ứng dụng minh họa",highlightthickness=1,width=45,background='#96D6FF',justify='center')
        lb_infTen.place(x=10,y=10)

        lb_infTen=Label(lf_inf,text="Họ và tên: Lê Hoàng Trung",background='#96D6FF')
        lb_infTen.place(x=10,y=50)

        lb_infMSV=Label(lf_inf,text="MSV: 2019605643",background='#96D6FF')
        lb_infMSV.place(x=10,y=80)

        lb_infTen=Label(lf_inf,text="Lớp: 20212IT6001001",background='#96D6FF')
        lb_infTen.place(x=10,y=110)
  



# giao diện 1

        lf_tao_khoa = LabelFrame(self, text="Tạo khóa",height=600,width=350,background='#97FFFF')
        lf_tao_khoa.place(x=10,y=200)

    #khoa bí mật ------------------------------

        lf_PrKey=LabelFrame(lf_tao_khoa, text="Private Key (x)",height=110,width=320,background='#79CDCD')
        lf_PrKey.place(x=10,y=30)

        lb_X=Label(lf_PrKey, text="Số nguyên x: ",background='#79CDCD')
        lb_X.place(x=10,y=10)
        
        entry_X = Entry(lf_PrKey,textvariable=strX, width = 45)
        entry_X.place(x=20,y=40)

    #khóa công khai B,al,p
        lf_PubKey=LabelFrame(lf_tao_khoa, text="Public Key (p,a,d)",height=300,width=320,background='#87CEEB')
        lf_PubKey.place(x=10,y=150)

        lb_P=Label(lf_PubKey, text="(Số nguyên tố) p:",background='#87CEEB')
        lb_P.place(x=10,y=10)

        entry_P = Entry(lf_PubKey,textvariable=strP, width = 45)
        entry_P.place(x=20,y=40)
    #-------------
        lb_Alpha=Label(lf_PubKey, text="(Số alpha) a : ",background='#87CEEB')
        lb_Alpha.place(x=10,y=80)

        entry_Alpha = Entry(lf_PubKey,textvariable=strAlpha, width = 45)
        entry_Alpha.place(x=20,y=110)
    #-------------
        lb_B=Label(lf_PubKey, text="(B= a^x mod p) B = ",background='#87CEEB')
        lb_B.place(x=10,y=150)

        entry_SoB = Entry(lf_PubKey,textvariable=strB, width = 45)
        entry_SoB.place(x=20,y=180)

        btn_tinhB=Button(lf_PubKey,text=("Tính B"),width=10,pady=10,command=lambda: btnTinhB(),background='#D1EEEE')
        btn_tinhB.place(x=200,y=220)

        btn_luuKhoa=Button(lf_PubKey,text=("Luu khoa"),width=10,command=lambda: btnLuuKhoa(),background='#D1EEEE')
        btn_luuKhoa.place(x=10,y=220)

        btn_taiKhoa=Button(lf_PubKey,text=("Tai khoa"),width=10,command=lambda: btnTaiKhoaB(),background='#D1EEEE')
        btn_taiKhoa.place(x=100,y=220)

        btn_Tao_khoa_ngau_nhien=Button(lf_tao_khoa,text="Tạo khóa ngẫu nhiên",width=20,pady=10,command=lambda: btnTaoKhoaNgauNhien_Click(),background='#D1EEEE')
        btn_Tao_khoa_ngau_nhien.place(x=30,y=480)

        btn_clear_khoa=Button(lf_tao_khoa,text=("Clear"),width=10,pady=5,command=lambda: btnClear(),background='#D1EEEE')
        btn_clear_khoa.place(x=230,y=480)

        
        # def Tao_khoa_ngau_nhien():

    #-------------
    #-------------
# giao diện 2
        x_default=20
        lf_thuc_hien_ky=LabelFrame(self, text="Thực hiện ký",height=820,width=530,background='#97FFFF')
        lf_thuc_hien_ky.place(x=380,y=10)

        lb_soK=Label(lf_thuc_hien_ky,text="Số ngẫu nhiên k",background='#97FFFF')
        lb_soK.place(x=x_default,y=10)
        entry_K=Entry(lf_thuc_hien_ky,textvariable=strK,width=55)
        entry_K.place(x=(x_default+20),y=40)

        btn_K=Button(lf_thuc_hien_ky,text="chọn K",width=10,command=lambda: chon_K())
        btn_K.place(x=(x_default+390),y=35)

        lb_chonFileMuonKy=Label(lf_thuc_hien_ky,text="Chọn file muốn ký:",background='#97FFFF')
        lb_chonFileMuonKy.place(x=x_default,y=70)
        text_FileMuonKy =Text(lf_thuc_hien_ky,height=2,width=41)
        text_FileMuonKy.place(x=(x_default+20),y=100)

        btn_chonFileMuonKy=Button(lf_thuc_hien_ky,text='File',width=10,command=lambda: openFileVB())
        btn_chonFileMuonKy.place(x=(x_default+390),y=100)
        #------------------------2
        lb_noiDung=Label(lf_thuc_hien_ky,text="Nội dung văn bản được gửi đi:",background='#97FFFF')
        lb_noiDung.place(x=x_default,y=150)
        text_NoiDung =Text(lf_thuc_hien_ky,height=5,width=45)
        text_NoiDung.place(x=(x_default+20),y=180)

        btn_luuVB=Button(lf_thuc_hien_ky,text='Lưu',width=10,command=lambda: luuVB())
        btn_luuVB.place(x=(x_default+400),y=200)
    # kys

        lf_chuKy=LabelFrame(lf_thuc_hien_ky, text="Chữ ký",height=270,width=500,background='#97FFFF')
        lf_chuKy.place(x=20,y=280)

        lb_hamBam=Label(lf_chuKy,text="Hàm băm (m)",background='#97FFFF')
        lb_hamBam.place(x=x_default+10,y=10)
        text_hamBam=Text(lf_chuKy,width=55,height=2) #,state='disable'
        text_hamBam.place(x=(x_default+10),y=40)

        lb_soS1=Label(lf_chuKy,text="S1 = (a^k mod p)",background='#97FFFF')
        lb_soS1.place(x=x_default+10,y=80)
        text_S1=Text(lf_chuKy,width=55,height=2)#,state='disable'
        text_S1.place(x=(x_default+10),y=110)

        lb_soS2=Label(lf_chuKy,text="S2 = (K^(-1) * (m-x*S1)) mod (p-1)",background='#97FFFF')
        lb_soS2.place(x=x_default+10,y=150)
        text_S2=Text(lf_chuKy,width=55,height=2) #,state='disable'
        text_S2.place(x=(x_default+10),y=180)
    # Tùy chọn
        lf_tuyChon=LabelFrame(lf_thuc_hien_ky, text="Tùy chọn",height=100,width=500,background='#97FFFF')
        lf_tuyChon.place(x=20,y=650)

        btn_Ky=Button(lf_tuyChon,text='Ký',width=10,pady=10,command=lambda: btnKyVB(),background='#D1EEEE')
        btn_Ky.place(x=(x_default+20),y=10)

        btn_luuChuKy=Button(lf_tuyChon,text='Lưu chữ ký',pady=10,width=17,command=lambda: btnLuuChuKy(),background='#D1EEEE')
        btn_luuChuKy.place(x=(x_default+160),y=10)

        btn_Gui=Button(lf_tuyChon,text='Gửi',width=10,pady=10,command=lambda: btnGuiVanBan(),background='#D1EEEE')
        btn_Gui.place(x=(x_default+350),y=10)

        #--------------------3
# giao diện 3
        lf_thuc_hien_kt=LabelFrame(self, text="Thực hiện kiểm tra chữ ký",height=820,width=530,background='#97FFFF')
        lf_thuc_hien_kt.place(x=950,y=10)

        lb_chonFileKT=Label(lf_thuc_hien_kt,text="Chọn file thực hiện kiểm tra chữ ký số:",background='#97FFFF')
        lb_chonFileKT.place(x=x_default,y=10)
        text_chonFileKT =Text(lf_thuc_hien_kt,height=2,width=40)
        text_chonFileKT.place(x=(x_default+20),y=40)
        btn_FileKT=Button(lf_thuc_hien_kt,text='File',width=10,command=lambda: openFileVBDuocKy(),background='#D1EEEE')
        btn_FileKT.place(x=(x_default+350),y=40)

        lb_noiDungVBKT=Label(lf_thuc_hien_kt,text="Nội dung văn bản muốn kiểm tra: ",background='#97FFFF')
        lb_noiDungVBKT.place(x=x_default,y=90)
        text_noiDungVBKT =Text(lf_thuc_hien_kt,height=4,width=55)
        text_noiDungVBKT.place(x=(x_default+20),y=120)

        lb_chonFileChuKy=Label(lf_thuc_hien_kt,text="Chọn file chứa chữ ký số:",background='#97FFFF')
        lb_chonFileChuKy.place(x=x_default,y=200)
        text_chonFileChuKy =Text(lf_thuc_hien_kt,height=2,width=40)
        text_chonFileChuKy.place(x=(x_default+20),y=230)
        btn_FileChuKy=Button(lf_thuc_hien_kt,text='File',width=10,command=lambda: openFileChuKy(),background='#D1EEEE')
        btn_FileChuKy.place(x=(x_default+350),y=230)


        lf_chuKyKT=LabelFrame(lf_thuc_hien_kt, text="Chữ ký",height=180,width=500,background='#97FFFF')
        lf_chuKyKT.place(x=20,y=280)

        lb_soS1KT=Label(lf_chuKyKT,text="S1 = (a^k mod p)",background='#97FFFF')
        lb_soS1KT.place(x=x_default+10,y=10)
        text_S1KT=Text(lf_chuKyKT,width=55,height=2)
        text_S1KT.place(x=(x_default+10),y=40)

        lb_soS2KT=Label(lf_chuKyKT,text="S2 = (K^(-1) * (m-x*S1)) mod (q-1)",background='#97FFFF')
        lb_soS2KT.place(x=x_default+10,y=80)
        text_S2KT=Text(lf_chuKyKT,width=55,height=2)
        text_S2KT.place(x=(x_default+10),y=100)


        lf_chuKQKT=LabelFrame(lf_thuc_hien_kt, text="Kết quả kiểm tra",height=280,width=500,background='#97FFFF')
        lf_chuKQKT.place(x=20,y=480)       

        lb_soV1=Label(lf_chuKQKT,text="V1 = (a^m mod p)",background='#97FFFF')
        lb_soV1.place(x=x_default+10,y=10)
        text_V1=Text(lf_chuKQKT,width=50,height=2)#,state='disable'
        text_V1.place(x=(x_default+20),y=30)

        lb_soV2=Label(lf_chuKQKT,text="V2 = (Beta^S1) * (S1^S2) mod p",background='#97FFFF')
        lb_soV2.place(x=x_default+10,y=70)
        text_V2=Text(lf_chuKQKT,width=50,height=2) #,state='disable'
        text_V2.place(x=(x_default+20),y=90)

        lb_kq=Label(lf_chuKQKT,text="kết quả kiểm tra",background='#97FFFF')
        lb_kq.place(x=x_default+10,y=130)
        text_kq=Text(lf_chuKQKT,width=50,height=2) #,state='disable'
        text_kq.place(x=(x_default+20),y=150)

        btn_KT=Button(lf_chuKQKT,text='Kiểm tra',width=30,pady=10,command=lambda: KTChuKy(),background='#D1EEEE')
        btn_KT.place(x=(x_default+120),y=200)


        def btnLuuKhoa():
            if( entry_Alpha.get() =="" or entry_SoB.get() =="" or entry_P.get() =="" ):
                Application.WindowWarning(self,"Không tìm thấy khóa để lưu")
                return
            filetypes=(
                ('text files','*.key'),
                ('All files', '*.*')
            )
            filename = fd.asksaveasfile(
                initialfile = 'Untitled.key',
                defaultextension=".key",
                filetypes=filetypes
                )    
            
            digest1=entry_P.get()
            digest2=entry_Alpha.get()
            digest3=entry_SoB.get()
            path=filename.name           

            f=open(path , 'w',encoding='UTF-8')
            digest=digest1+'\n'+digest2 +'\n'+ digest3
            f.write(digest)
            f.close()
            # path=path.replace('.txt','.sig')

            self.WindowWarning("Khóa đã được lưu vào file: \n"+path)            
        def btnTaiKhoaB():
            strAlpha.set("")
            strP.set("")
            strB.set("")            
            filetypes = (
                ('text files', '*.key'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                title='Open a file',
                initialdir=r"C:\Users\Le Trung\Desktop\ATBMTT\btl03",
                filetypes=filetypes)
            f1 = open(filename, 'r', encoding='UTF-8')
            data1 = f1.readline()
            data2 = f1.readline()
            data3 = f1.readline()
            f1.close()
            strP.set(data1)

            strAlpha.set(data2)
            strB.set(data3)

        def btnTaoKhoaNgauNhien_Click():
            Application.quanlykhoaElgamal=QuanLyKhoa.GetRandomElgammalManaged()
            strP.set(Application.quanlykhoaElgamal.khoaCongKhai.p)
            strAlpha.set(Application.quanlykhoaElgamal.khoaCongKhai.alpha)
            strB.set(Application.quanlykhoaElgamal.khoaCongKhai.beta)
            strX.set(Application.quanlykhoaElgamal.khoaBiMat.a)
            So_P=int(strP.get())
            So_A=int(strAlpha.get())
            So_B=int(strB.get())
            So_X=int(strX.get())
            
            print(So_X,So_P,So_A,So_B)

        def chon_K():
            if(strP.get()!=''):
                strK.set(elgamal.NgauNhienK(int(strP.get())))

            else:
                Application.WindowWarning(self,'Chưa nhập P')

        def openFileVB():
            data1=""
            text_S1.config(state='normal')
            text_FileMuonKy.delete('1.0',"end-1c")
            # text_S1.delete('1.0',"end-1c")
            text_NoiDung.delete('1.0',"end-1c")
            filetypes = (
                ('text files', '*.doc'),
                ('text files', '*.txt'),
                ('text files', '*.pdf'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                title='Open a file',
                initialdir=r"C:\Users\Le Trung\Desktop\ATBMTT\btl03",
                filetypes=filetypes)
            text_FileMuonKy.insert('1.0',filename)     
            f1 = open(filename, 'r', encoding='UTF-8')
            data1 = f1.read()
            f1.close()
            text_NoiDung.insert('1.0',data1) 

        def btnKyVB():

            data1= text_NoiDung.get("1.0","end-1c")
            text_S1.delete('1.0',"end-1c")
            text_S2.delete('1.0',"end-1c")
            state=checkInput_fomat(strX,strP,strAlpha,strK,strB)
            if(state==False):
                return            
            hashed_string = int.from_bytes(hashlib.sha256(data1.encode('utf-8')).digest(), "big")
            S1,S2=elgamal.maHoa(So_K,hashed_string,Application.quanlykhoaElgamal.khoaBiMat,Application.quanlykhoaElgamal.khoaCongKhai)
            text_S1.insert('1.0',S1) 
            text_S2.insert('1.0',S2) 
            print(text_S1.get("1.0","end-1c"))
            Application.noiDungChuKy=hashed_string
            text_hamBam.delete('1.0','end-1c')
            text_hamBam.insert('1.0',hashed_string)

        def btnLuuChuKy():            
            if( text_S1.get("1.0","end-1c") =="" or text_S2.get("1.0","end-1c") =="" ):
                Application.WindowWarning(self,"Không tìm thấy chữ ký để lưu")
                return
            filetypes=(
                ('text files','*.sig'),
                ('All files', '*.*')
            )
            filename = fd.asksaveasfile(
                initialfile = 'Untitled.sig',
                defaultextension=".sig",
                filetypes=filetypes
                )    
            
            digest1=text_S1.get("1.0","end-1c")
            digest2=text_S2.get("1.0","end-1c")
            path=filename.name
            # path=path.replace('.sig','.txt')

            f=open(path , 'w',encoding='UTF-8')
            digest=digest1+'\n'+digest2
            f.write(digest)
            f.close()
            # path=path.replace('.txt','.sig')

            self.WindowWarning("Chữ ký đã được lưu vào file: \n"+path)

        def luuVB():
            if( text_NoiDung.get("1.0","end-1c") ==""):
                Application.WindowWarning(self,"Không tìm thấy văn bản để lưu")
                return            
            text_FileMuonKy.delete('1.0',"end-1c")
            filetypes = (
                ('text files', '*.txt'),
                ('text files', '*.doc'),
                ('text files', '*.docx'),
                ('text files', '*.pdf'),
                ('All files', '*.*')
            )
            filename = fd.asksaveasfile(
                initialfile = 'Untitled.txt',
                defaultextension=".txt",
                filetypes=filetypes
                )
            text_FileMuonKy.insert('1.0',filename.name)
            path=text_FileMuonKy.get('1.0','end-1c')
            f=open(path , 'w' ,encoding='UTF-8')
            digest=text_NoiDung.get("1.0","end-1c")
            f.write(digest)
            f.close()
            self.WindowWarning("Nội dung đã được lưu vào file: \n"+path)          

        def btnGuiVanBan():            
            if(Application.noiDungChuKy==""):
                Application.WindowWarning(self,"Không tìm thấy chữ ký!!!")
                return
            # text_noiDungVBKT.config(state=['normal'])
            text_noiDungVBKT.delete('1.0','end-1c')
            text_noiDungVBKT.insert('1.0',text_NoiDung.get("1.0","end-1c"))
            text_S1KT.delete("1.0","end-1c")
            text_S2KT.delete("1.0","end-1c")

            text_S1KT.insert('1.0',text_S1.get("1.0","end-1c"))
            text_S2KT.insert("1.0",text_S2.get("1.0","end-1c"))           



        def openFileVBDuocKy():
            text_noiDungVBKT.delete("1.0","end-1c")
            text_chonFileKT.delete('1.0',"end-1c")
            filetypes = (
                ('text files', '*.doc'),
                ('text files', '*.txt'),
                ('text files', '*.pdf'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                title='Open a file',
                initialdir=r"C:\Users\Le Trung\Desktop\ATBMTT\btl03",
                filetypes=filetypes) 
            text_chonFileKT.insert('1.0',filename)
            f1 = open(filename, 'r', encoding='UTF-8')
            data1 = f1.read()
            f1.close()
            text_noiDungVBKT.insert("1.0",data1)
            
        def openFileChuKy():
            text_chonFileChuKy.delete("1.0","end-1c")
            text_S1KT.delete('1.0','end-1c')
            text_S2KT.delete('1.0','end-1c')
            filetypes = (
                ('text files', '*.sig'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                title='Open a file',
                initialdir=r"C:\Users\Le Trung\Desktop\ATBMTT\btl03",
                filetypes=filetypes) 
            text_chonFileChuKy.insert('1.0',filename)
            f1 = open(filename, 'r', encoding='UTF-8')
            data1 = f1.readline()
            data2 = f1.readline()
            f1.close()
            text_S1KT.insert("1.0",data1)
            text_S2KT.insert("1.0",data2)
            
        def KTChuKy():
            text_kq.delete('1.0',"end-1c")

            data1=text_noiDungVBKT.get('1.0',"end-1c")
            hash_string=int.from_bytes(hashlib.sha256(data1.encode('utf-8')).digest(), "big")
            flag=True
            try: 
                flag=elgamal.giaiMa(hash_string,int(text_S1KT.get("1.0","end-1c")),int(text_S2KT.get("1.0","end-1c")),Application.quanlykhoaElgamal.khoaCongKhai)
            except:
                self.WindowWarning("Không tìm thấy chữ ký")
                return
            if(flag[0] == flag[1]):
                text_V1.delete('1.0',"end-1c")
                text_V2.delete('1.0',"end-1c")
                text_V2.insert('1.0',flag[1])
                text_V1.insert('1.0',flag[0])
                # text_V2.insert('1.0',flag[1])
                text_kq.insert('1.0','Chữ ký hợp lệ')
                Application.WindowWarning(self,'Chữ ký chính xác')
                
                
            else:
                text_V1.delete('1.0',"end-1c")
                text_V2.delete('1.0',"end-1c")
                text_V1.insert('1.0',flag[0])
                text_V2.insert('1.0',flag[1])
                text_kq.insert('1.0','Không khớp!!!')
                self.WindowWarning("Văn bản hoặc chữ ký không chính xác")
        def btnTinhB():
            try:
                a=binhPhuongNhan(int(entry_Alpha.get()),int(entry_X.get()),int(entry_P.get()))
                strB.set(a)
                Application.quanlykhoaElgamal=QuanLyKhoa(int(entry_P.get()),int(entry_Alpha.get()),int(entry_X.get()))
            except:
                msg="Nhập thiếu dữ liệu ( X, Alpha, P)"
                self.w_num(msg)
                strB.set("")
                return

        def btnClear():
            strAlpha.set("")
            strB.set("")
            strK.set("")
            strP.set("")
            strX.set("")
            strS1.set("")
        def checkInput_fomat(x,p,a,k,B):
            global So_X,So_P,So_A,So_K,So_B
            try:                
                So_B=int(B.get())  
            except:
                msg="Nhập lại số Beta"
                self.w_num(msg)
                B.set("")
                return False
            try:                
                So_X=int(x.get())  
            except:
                msg="Nhập lại số nguyên x"
                self.w_num(msg)
                x.set("")
                return False
            try:
                So_P=int(p.get())  
                if(laSoNT(So_P)==False):
                    msg="Nhập lại số nguyên tố p"
                    self.w_num(msg)
                    p.set("")
                    return False
                if(So_P<pow(2,256)):
                    msg="Nhập lại số nguyên tố p (p>2^256)"
                    self.w_num(msg)
                    p.set("")
                    return False                   
            except:
                msg="Nhập lại số nguyên tố p"
                self.w_num(msg)
                p.set("")
                return False
            try:
                So_A=int(a.get())  
            except:
                msg="Nhập lại số alphal a"
                self.w_num(msg)
                a.set("")
                return False  
            try:
                So_K=int(k.get())  
            except:
                msg="Nhập lại số K"
                self.w_num(msg)
                k.set("")
                return False  
            return True

            
    def w_num(self,msg):
        wd= Tk()
        wd.geometry("400x200+700+200")
        w = Label(wd, text ='Cảnh báo', font = "50") 
        w.pack()                
        msg = Label( wd, text = "Dữ liệu nhập vào không hợp lệ\n"+msg)                
        msg.pack()  
        btn=Button(wd, text="OKE",font=20,command=wd.destroy)
        btn.place(x=120,y=100)
        wd.mainloop()  
    def WindowWarning(self,msg):
        wd= Tk()
        wd.geometry("300x200+700+200")
        w = Label(wd, text ='Cảnh báo', font = "50") 
        w.pack()                
        msg = Label( wd, text = msg)                
        msg.pack()  
        btn=Button(wd, text="OKE",font=20,command=wd.destroy)
        btn.place(x=120,y=100)
        wd.mainloop()  