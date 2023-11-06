import openpyxl
import csv
class BanHang:
    donhang:str
    masp:str
    tensp:str
    hangsx:str
    loaisp:str
    soluong:int
    giaban:float
    tenkhachhang:str
    sodienthoai:str
    soluongban:int
    giaban:float
    def __init__(self, donhang,masp, tensp, hangsx, loaisp,soluong,giaban, tenkhachhang, sodienthoai, soluongban):
        self.donhang = donhang
        self.masp = masp
        self.tensp = tensp
        self.hangsx = hangsx
        self.loaisp = loaisp
        self.soluong = soluong
        self.giaban = giaban
        self.tenkhachhang = tenkhachhang
        self.sodienthoai = sodienthoai
        self.soluongban = soluongban
    def write_csv(file_path, data):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    @classmethod
    def soluong_daban(self,masp):
        data = []
        with open('bh.csv', 'r', encoding='utf-8') as file:
            tieude = file.readline()
            reader = csv.reader(file)
            data = [row for row in reader]
            soluongban =0
            if(len(data)>0):
                for item in data:
                    if masp == item[1]:
                    
                        soluongban += int(item[9])
            return soluongban
    @classmethod
    def add_donhang(self, donhang,masp, tensp, hangsx, loaisp,soluong,giaban, tenkhachhang, sodienthoai, soluongban):
        mess_erorr = "Vui lòng nhập đầy đủ các trường"
        mess_suss = "Thêm dữ liệu thành công"
        mess_front = "Vui lòng nhập ký tự không dấu"
        mess_trung = "ID đơn hàng đã bị trùng, bạn chỉ có thể chỉnh sửa"
        trung = False
        with open('bh.csv', 'r', encoding='utf-8') as file:
            tieude = file.readline()
            reader = csv.reader(file)
            data = [row for row in reader]
            
            for item in data:
                if donhang == item[0]:
                    trung = True
                    return mess_trung
            if trung == False:   
                if donhang =="" or masp =="" or tensp =="" or hangsx =="" or loaisp =="" or soluong =="" or giaban =="" or tenkhachhang =="" or sodienthoai =="" or soluongban=="":
                    return mess_erorr
                else: 
                    try:
                        data_add = [
                            [donhang,masp, tensp, hangsx, loaisp, soluong, giaban, tenkhachhang,sodienthoai,soluongban]
                        ]
                        existing_file_path = 'bh.csv' 
                        with open(existing_file_path, 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(data_add)
                            print(f"Data has been appended to {existing_file_path}")
                            return mess_suss
                    except:
                        return mess_front
    @classmethod
    def find_donhang(self, donhang):
        print(donhang)
        with open('bh.csv', 'r', encoding='utf-8') as file:
            tieude = file.readline()
            reader = csv.reader(file)
            data = [row for row in reader]
            for item in data:
                if donhang == item[0]:
                    print(f"In trong hàm: {item}")
                    return item
                    break
    @classmethod
    def edit_donhang(self, donhang,masp, tensp, hangsx, loaisp,soluong,giaban, tenkhachhang, sodienthoai, soluongban):
         with open('bh.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            for item in data:
                if donhang == item[0]:
                   i = data.index(item)
                   print(i)
                   print(f"Hàm sửa {item}")
                   data[i][1] = masp
                   data[i][2] = tensp
                   data[i][3] = hangsx
                   data[i][4] = loaisp
                   data[i][5] = soluong
                   data[i][6] = giaban
                   data[i][7] = tenkhachhang
                   data[i][8] = sodienthoai
                   data[i][9] = soluongban
                   BanHang.write_csv(file_path='bh.csv',data=data)
                   break
    @classmethod
    def del_dh(self, madonhang):
        print(madonhang)
        with open('bh.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            for item in data:
                if madonhang == item[0]:
                   i = data.index(item)
                   print(item)
                   del data[i]
                   BanHang.write_csv(file_path='bh.csv',data=data)
    @classmethod
    def export_file_chitiet(self,madonhang):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        with open('bh.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            reader = csv.reader(file)
            data = [row for row in reader]
            for item in data:
                if madonhang == item[0]:
                    print(item)
                    break
            add_data =[
                ["donhang","masp","tensp","hangsx","loaisp","soluong","giaban","tenkhachhang","sodienthoai","soluongban","thanhtien"],
                [item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9], int(item[6])*int(item[9])]
            ]
            for row in add_data:
                sheet.append(row)
            file_name = f"XuatFile/chi_tiet_don_hang_{madonhang}.xlsx"
            workbook.save(filename=file_name)
            
