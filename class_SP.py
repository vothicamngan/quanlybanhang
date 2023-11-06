import csv
class SanPham():
    masp:str
    tensp:str
    hangsx:str
    loaisx:str
    soluong:int
    giaban:float
    def __init__(self, masp, tensp, hangsx, loaisx , soluong, giaban):
       self.masp = masp
       self.tensp = tensp
       self.hangsx = hangsx
       self.loaisx = loaisx
       self.soluong = soluong
       self.giaban = giaban
    def write_csv(file_path, data):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    @classmethod   
    def add_sp(self,masp, tensp, hangsx, loaisx , soluong, giaban):
        mess_erorr = "Vui lòng nhập đầy đủ các tường"
        mess_suss = "Thêm dữ liệu thành công"
        mess_front = "Vui lòng nhập ký tự không dấu"
        if masp == "" or tensp =="" or hangsx == "" or loaisx =="" or soluong=="" or giaban =="":
            return mess_erorr
        else:
            try:
                data_add = [
                    [masp, tensp, hangsx, loaisx, soluong,giaban]
                ]
                existing_file_path = 'sp.csv' 
                with open(existing_file_path, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data_add)
                print(f"Data has been appended to {existing_file_path}")
                return mess_suss
            except:
                return mess_front
    @classmethod
    def find_sp(self, masp):
        data = []
        print(masp)
        with open('sp.csv', 'r', encoding='utf-8') as file:
            tieude = file.readline()
            reader = csv.reader(file)
            data = [row for row in reader]
            for item in data:
                if masp == item[0]:
                    data = item
                    print(f"In trong hàm: {data}")
                    return data
                    break
    @classmethod
    def edit_sp(self, masp, tensp, hangsx, loaisx , soluong, giaban):
        with open('sp.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            for item in data:
                if masp == item[0]:
                   i = data.index(item)
                   print(i)
                   print(f"Hàm sửa {item}")
                   data[i][1] = tensp
                   data[i][2] = hangsx
                   data[i][3] = loaisx
                   data[i][4] = soluong
                   data[i][5] = giaban
                   SanPham.write_csv(file_path='sp.csv',data=data)
                   break
    @classmethod
    def del_sp(self, masp):
        print(masp)
        with open('sp.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            for item in data:
                if masp == item[0]:
                   i = data.index(item)
                   print(item)
                   del data[i]
                   SanPham.write_csv(file_path='sp.csv',data=data)

    
                
