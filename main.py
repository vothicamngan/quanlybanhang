import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import csv
import class_SP 
import class_BH
from tkinter import messagebox


# Function SP
def add_data():
    data = class_SP.SanPham.add_sp(masp=entry_masp.get(),tensp=entry_tensp.get(), hangsx=entry_hangsx.get()
                            , loaisx= combobox_loaisp.get(), soluong= entry_sl.get(), giaban=entry_gianban.get())
  
    entry_masp.delete(0, 'end')
    entry_tensp.delete(0, 'end')
    entry_hangsx.delete(0, 'end')
    combobox_loaisp.delete(0 ,'end')
    entry_sl.delete(0, 'end')
    entry_gianban.delete(0, 'end')
    messagebox.showinfo("Thông báo", data)
    file_path1 = 'sp.csv' 
    data1 = read_csv(file_path1)
    populate_treeview(tree, data1)
def find_data():
    entry_tensp.delete(0, 'end')
    entry_hangsx.delete(0, 'end')
    combobox_loaisp.delete(0 ,'end')
    entry_sl.delete(0, 'end')
    entry_gianban.delete(0, 'end')
    data2 = class_SP.SanPham.find_sp(masp=entry_masp.get())
    print(data2)
    if data2!=None:
        print(data)
        entry_tensp.insert(0, data2[1])
        entry_hangsx.insert(0,data2[2])
        combobox_loaisp.insert(0,data2[3])
        entry_sl.insert(0,data2[4])
        entry_gianban.insert(0,data2[5])
    else:
        messagebox.showerror("Thông báo", "Không tìm thấy dữ liệu")  

def edit_data():
    if entry_masp.get() == "":
        messagebox.showerror("Thông báo", "Vui lòng nhập thông tin sản phẩm")
    else:
        data = class_SP.SanPham.edit_sp(masp=entry_masp.get(),tensp=entry_tensp.get(), hangsx=entry_hangsx.get()
                                , loaisx= combobox_loaisp.get(), soluong= entry_sl.get(), giaban=entry_gianban.get())
        entry_masp.delete(0, 'end')
        entry_tensp.delete(0, 'end')
        entry_hangsx.delete(0, 'end')
        combobox_loaisp.delete(0 ,'end')
        entry_sl.delete(0, 'end')
        entry_gianban.delete(0, 'end')
        messagebox.showinfo("Thông báo", "Cập nhật dữ liệu thành công")
        file_path1 = 'sp.csv' 
        data1 = read_csv(file_path1)
        populate_treeview(tree, data1)
def del_data():
    if(entry_masp.get()==""):
        messagebox.showerror("Thông báo", "Vui lòng nhập thông tin sản phẩm")
    else:
        class_SP.SanPham.del_sp(masp=entry_masp.get())
        messagebox.showinfo("Thông báo", "Xóa dữ liệu thành công")
        file_path1 = 'sp.csv' 
        data1 = read_csv(file_path1)
        populate_treeview(tree, data1)


def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tieude = file.readline()
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def populate_treeview(tree, data):
    tree.delete(*tree.get_children())
    for row in data:
        tree.insert('', 'end', values=row)

def show_framesp():
    if frame_sp.winfo_ismapped():
        print("if")
        frame_sp.pack_forget()
    else:
        print("else")
        frame_bh.pack_forget()
        frame_sp.pack()

def show_framebh():
    if frame_bh.winfo_ismapped():
        print("if")
        frame_bh.pack_forget()
    else:
        print("else")
        frame_sp.pack_forget()
        frame_bh.pack()

def on_combobox_selected(event):
    selected_value = combobox_loaisp.get()
    return selected_value
def on_select_sp(event):
    entry_masp.delete(0,'end')
    entry_tensp.delete(0,'end')
    entry_hangsx.delete(0,'end')
    combobox_loaisp.delete(0,'end')
    entry_sl.delete(0,'end')
    entry_gianban.delete(0,'end')
    item = tree.focus()
    entry_masp.insert(0,tree.item(item)["values"][0])
    entry_tensp.insert(0,tree.item(item)["values"][1])
    entry_hangsx.insert(0,tree.item(item)["values"][2])
    combobox_loaisp.insert(0,tree.item(item)["values"][3])
    entry_sl.insert(0,tree.item(item)["values"][4])
    entry_gianban.insert(0,tree.item(item)["values"][5])
    print("Selected Item:", tree.item(item)["values"][0])


# Function bán hàng
def find_data_bh():
    entry_tensp_bh.delete(0, 'end')
    entry_hangsx_bh.delete(0, 'end')
    combobox_loaisp_bh.delete(0 ,'end')
    entry_sl_bh.delete(0, 'end')
    entry_gianban_bh.delete(0, 'end')
    entry_sl_bh.delete(0,'end')
    data2 = class_SP.SanPham.find_sp(entry_masp_bh.get())
    tongsoluongban = class_BH.BanHang.soluong_daban(masp=entry_masp_bh.get())
    print(tongsoluongban)
    print(data2)
    if data2!=None:
        print(data)
        entry_tensp_bh.insert(0, data2[1])
        entry_hangsx_bh.insert(0,data2[2])
        combobox_loaisp_bh.insert(0,data2[3])
        entry_sl_bh.insert(0,int(data2[4])-tongsoluongban)
        entry_gianban_bh.insert(0,data2[5])
    else:
        messagebox.showerror("Thông báo", "Không tìm thấy dữ liệu")  
def add_data_bh():
    
    data1 = class_SP.SanPham.find_sp(entry_masp_bh.get())
    soluongban = class_BH.BanHang.soluong_daban(entry_masp_bh.get())
    soluongton = int(data1[4])-int(soluongban)
    if soluongton< int(entry_slban.get()):
        messagebox.showerror("Thông báo", f"Số lượng tồn không đủ, tồn {soluongton}")
    else:
        data = class_BH.BanHang.add_donhang(entry_donhang_bh.get(),entry_masp_bh.get(), entry_tensp_bh.get(), entry_hangsx_bh.get(),
                                            combobox_loaisp_bh.get(),soluongton,entry_gianban_bh.get(), entry_tenkh.get()
                                            , entry_sdtkh.get(), entry_slban.get() )
        messagebox.showinfo("Thông báo", data)
        entry_donhang_bh.delete(0,'end')
        data_banhang1 = read_csv(file_path=file_path_banhang)
        entry_donhang_bh.insert(0, int(data_banhang1[len(data_banhang1)-1][0])+1)
        entry_masp_bh.delete(0,'end')
        entry_tensp_bh.delete(0, 'end')
        entry_hangsx_bh.delete(0, 'end')
        combobox_loaisp_bh.delete(0 ,'end')
        entry_sl_bh.delete(0, 'end')
        entry_gianban_bh.delete(0, 'end')
        entry_tenkh.delete(0,'end')
        entry_sdtkh.delete(0,'end')
        entry_sl_bh.delete(0,'end')
        entry_slban.delete(0,'end')
        populate_treeview(tree1,data_banhang1)
    
def find_data_dh():
    entry_masp_bh.delete(0,'end')
    entry_tensp_bh.delete(0, 'end')
    entry_hangsx_bh.delete(0, 'end')
    combobox_loaisp_bh.delete(0 ,'end')
    entry_sl_bh.delete(0, 'end')
    entry_gianban_bh.delete(0, 'end')
    entry_tenkh.delete(0,'end')
    entry_sdtkh.delete(0,'end')
    entry_sl_bh.delete(0,'end')
    data = class_BH.BanHang.find_donhang(entry_donhang_bh.get())
    print(data)
    if data!=None:
        entry_masp_bh.insert(0,data[1])
        entry_tensp_bh.insert(0,data[2])
        entry_hangsx_bh.insert(0,data[3])
        combobox_loaisp_bh.insert(0,data[4])
        entry_sl_bh.insert(0,data[5])
        entry_gianban_bh.insert(0,data[6])
        entry_tenkh.insert(0,data[7])
        entry_sdtkh.insert(0,data[8])
        entry_slban.insert(0,data[9])
    else:
        messagebox.showerror("Thông báo", "Không tìm thấy đơn hàng")
def edit_data_dh():
    try:
        data = class_BH.BanHang.edit_donhang(entry_donhang_bh.get(),entry_masp_bh.get(), entry_tensp_bh.get(), entry_hangsx_bh.get(), combobox_loaisp_bh.get(),
                                         entry_sl_bh.get(),entry_gianban_bh.get(),entry_tenkh.get(),entry_sdtkh.get(),entry_slban.get())
        messagebox.showinfo("Thông báo", "Chỉnh sửa đơn hàng thành công")
        entry_donhang_bh.delete(0,'end')
        data_banhang1 = read_csv(file_path=file_path_banhang)
        entry_donhang_bh.insert(0, int(data_banhang1[len(data_banhang1)-1][0])+1)
        entry_masp_bh.delete(0,'end')
        entry_tensp_bh.delete(0, 'end')
        entry_hangsx_bh.delete(0, 'end')
        combobox_loaisp_bh.delete(0 ,'end')
        entry_sl_bh.delete(0, 'end')
        entry_gianban_bh.delete(0, 'end')
        entry_tenkh.delete(0,'end')
        entry_sdtkh.delete(0,'end')
        entry_sl_bh.delete(0,'end')
        entry_slban.delete(0,'end')
        populate_treeview(tree1,data_banhang1)
    
    except:
        messagebox.showerror("Thông báo", "Chỉnh sửa đơn hàng không thành công")
def del_data_dh():
    try:
        data = class_BH.BanHang.del_dh(entry_donhang_bh.get())
        messagebox.showinfo("Thông báo", "Xóa đơn hàng thành công")
        data_banhang1 = read_csv(file_path=file_path_banhang)
        populate_treeview(tree1,data_banhang1)
        entry_donhang_bh.delete(0,'end')
        a = 0
        if len(data_banhang) == 0:
            a =1
        else:
            a= int(data_banhang[len(data_banhang)-1][0])+1 
        entry_donhang_bh.insert(0,a)
        entry_masp_bh.delete(0,'end')
        entry_tensp_bh.delete(0, 'end')
        entry_hangsx_bh.delete(0, 'end')
        combobox_loaisp_bh.delete(0 ,'end')
        entry_sl_bh.delete(0, 'end')
        entry_gianban_bh.delete(0, 'end')
        entry_tenkh.delete(0,'end')
        entry_sdtkh.delete(0,'end')
        entry_sl_bh.delete(0,'end')
        entry_slban.delete(0,'end')
        
        
    except:
        messagebox.showinfo("Thông báo", "Xóa đơn hàng không thành công")
def on_select_tree_bh(event):
    entry_donhang_bh.delete(0,'end')
    entry_masp_bh.delete(0,'end')
    entry_tensp_bh.delete(0, 'end')
    entry_hangsx_bh.delete(0, 'end')
    combobox_loaisp_bh.delete(0 ,'end')
    entry_sl_bh.delete(0, 'end')
    entry_gianban_bh.delete(0, 'end')
    entry_tenkh.delete(0,'end')
    entry_sdtkh.delete(0,'end')
    entry_slban.delete(0,'end')
    item = tree1.focus()
    print(item)
    entry_donhang_bh.insert(0,tree1.item(item)["values"][0])
    entry_masp_bh.insert(0,tree1.item(item)["values"][1])
    entry_tensp_bh.insert(0,tree1.item(item)["values"][2])
    entry_hangsx_bh.insert(0,tree1.item(item)["values"][3])
    combobox_loaisp_bh.insert(0,tree1.item(item)["values"][4])
    entry_sl_bh.insert(0,tree1.item(item)["values"][5])
    entry_gianban_bh.insert(0,tree1.item(item)["values"][6])
    entry_tenkh.insert(0,tree1.item(item)["values"][7])
    entry_sdtkh.insert(0,tree1.item(item)["values"][8])
    entry_slban.insert(0,tree1.item(item)["values"][9])
def export_donhang():
    data = class_BH.BanHang.export_file_chitiet(entry_donhang_bh.get())
    messagebox.showinfo("Thông báo", f"Xuát file chi tiết đơn hàng {entry_donhang_bh.get()} thành công")

file_path = 'sp.csv' 
data = read_csv(file_path)


file_path_banhang = 'bh.csv'
data_banhang = read_csv(file_path=file_path_banhang)
print(len(data_banhang))
# Màn hình chính
main = tk.Tk()
main.geometry("2800x1800")
main.title("QUẢN LÝ BÁN HÀNG")
# Memu
menu_bar = tk.Menu(main)
main.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Hệ thống", menu=file_menu)
file_menu.add_command(label="Đóng", command=main.destroy)

# Tilte
frame_title = tk.Frame(main, width=2800, height=100)
frame_title.place(anchor='center', relx=0.5, rely=0.03)
title_page = tk.Label(frame_title, text="PHẦN MỀM QUẢN LÝ BÁN HÀNG", font="Time 15 bold" , fg="#06a099")
title_page.pack()
frame_title.pack(pady=10)
# Button
btn_sp = tk.Button(main , text="QUẢN LÝ SẢN PHẨM" , fg="#0000FF" , font="Time 12 bold", command=show_framesp)
btn_sp.place(x=500, y=50)
btn_banhang = tk.Button(main , text="QUẢN LÝ BÁN HÀNG" , fg="#0000FF" , font="Time 12 bold", command= show_framebh)
btn_banhang.place(x=700, y=50)

frame1 = tk.Frame(main)
frame1.pack(pady=20)

# Frame sp
frame_sp = tk.Frame (main, width=1500 , height=1200,  bg="#EEEEEE")
title_sp = tk.Label(frame_sp, text="CHI TIẾT SẢN PHẨM", bg='#EEEEEE', font="Time 12 bold")
title_sp.place(x=250, y=20)

# Mã sản phẩm
title_masp = tk.Label(frame_sp, text="Mã sản phẩm:",bg='#EEEEEE' , font="Time 12" )
title_masp.place(x=50, y=50)
entry_masp = tk.Entry(frame_sp,width=30, font="Time 12")
entry_masp.place(x=170, y = 50)

# Tên sản phẩm
title_tensp = tk.Label(frame_sp, text="Tên sản phẩm:",bg='#EEEEEE' , font="Time 12" )
title_tensp.place(x=50, y=80)
entry_tensp = tk.Entry(frame_sp,width=40, font="Time 12")
entry_tensp.place(x=170, y = 80)


# Hãng sx
title_hangsx = tk.Label(frame_sp, text="Hãng sản xuất:",bg='#EEEEEE' , font="Time 12" )
title_hangsx.place(x=50, y=110)
entry_hangsx = tk.Entry(frame_sp,width=40, font="Time 12")
entry_hangsx.place(x=170, y = 110)

# Loại sản phẩm
selected_value = tk.StringVar()
title_loaisp = tk.Label(frame_sp, text="Loại sản phẩm:",bg='#EEEEEE' , font="Time 12" )
title_loaisp.place(x=50, y=140)
combobox_loaisp = ttk.Combobox(frame_sp, textvariable=selected_value, font="Time 12")
combobox_loaisp['values'] = ('Nuoc suoi', 'Nuoc co gas', 'Nuoc co con', 'Nuoc ngot')
combobox_loaisp.pack(pady=10)
combobox_loaisp.set('Nuoc suoi')
combobox_loaisp.bind('<<ComboboxSelected>>', on_combobox_selected)
combobox_loaisp.place(x=170, y = 140)

# Số lượng
title_sl = tk.Label(frame_sp, text="Số lượng:",bg='#EEEEEE' , font="Time 12" )
title_sl.place(x=50, y=170)
entry_sl = tk.Entry(frame_sp,width=40, font="Time 12")
entry_sl.place(x=170, y = 170)

# Giá bán

title_giaban = tk.Label(frame_sp, text="Giá bán:",bg='#EEEEEE' , font="Time 12" )
title_giaban.place(x=50, y=200)
entry_gianban = tk.Entry(frame_sp,width=40, font="Time 12")
entry_gianban.place(x=170, y = 200)

# Button  tác vụ

# Tìm kiếm
btn_tim_kiem = tk.Button(frame_sp, text="Tìm kiếm", font="Time 9", command= find_data)
btn_tim_kiem.place(x= 450, y=48)

# Thêm
btn_them = tk.Button(frame_sp, text="Thêm mới", font="Time 13", command= add_data)
btn_them.place(x= 70, y =230)
# Sửa
btn_sua = tk.Button(frame_sp, text="Sửa" ,font="Time 13" ,width=10 , command=edit_data)
btn_sua.place(x=230, y=230)
#Xóa

btn_xoa = tk.Button(frame_sp, text="Xóa" ,font="Time 13" ,width=10, command=del_data)
btn_xoa.place(x=400, y=230)

# Danh sách sản phẩm
label_dmsp = tk.Label(frame_sp, text="DANH SÁCH SẢN PHẨM", font="Time 12 bold")
label_dmsp.place(x=800, y = 20)
# Create Treeview
columns  = ("MaSP", "TenSP","HangSX","LoaiSP","SLSP","GiaBan")
tree = ttk.Treeview(frame_sp, columns=columns, show='headings',height=25)
tree.place(x=600, y =50)


for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)  


# Bind a function to item selection
tree.bind("<ButtonRelease-1>", on_select_sp)

# Pack Treeview
populate_treeview(tree, data)

frame_sp.pack_forget()

# Frame bán hàng
frame_bh = tk.Frame(main,width=1500 , height=1200,  bg="#EEEEEE")
title_sp = tk.Label(frame_bh, text="CHI TIẾT BÁN HÀNG", bg='#EEEEEE', font="Time 12 bold")
title_sp.place(x=250, y=20)

# Don hang
title_madonhang_bh = tk.Label(frame_bh, text="Mã đơn hàng:",bg='#EEEEEE' , font="Time 12" )
title_madonhang_bh.place(x=50, y=50)
entry_donhang_bh = tk.Entry(frame_bh,width=30, font="Time 12" )
entry_donhang_bh.place(x=170, y = 50)
a = 0
if len(data_banhang) == 0:
    a =1
else:
    a= int(data_banhang[len(data_banhang)-1][0])+1 
entry_donhang_bh.insert(0,a)

# MaSP
title_masp_bh = tk.Label(frame_bh, text="Mã sản phẩm:",bg='#EEEEEE' , font="Time 12" )
title_masp_bh.place(x=50, y=80)
entry_masp_bh = tk.Entry(frame_bh,width=30, font="Time 12")
entry_masp_bh.place(x=170, y = 80)

# Tên sản phẩm
title_tensp_bh = tk.Label(frame_bh, text="Tên sản phẩm:",bg='#EEEEEE' , font="Time 12" )
title_tensp_bh.place(x=50, y=110)
entry_tensp_bh = tk.Entry(frame_bh,width=40, font="Time 12")
entry_tensp_bh.place(x=170, y = 110)


# Hãng sx
title_hangsx_bh = tk.Label(frame_bh, text="Hãng sản xuất:",bg='#EEEEEE' , font="Time 12" )
title_hangsx_bh.place(x=50, y=140)
entry_hangsx_bh = tk.Entry(frame_bh,width=40, font="Time 12")
entry_hangsx_bh.place(x=170, y = 140)

# Loại sản phẩm
title_loaisp_bh = tk.Label(frame_bh, text="Loại sản phẩm:",bg='#EEEEEE' , font="Time 12" )
title_loaisp_bh.place(x=50, y=170)
combobox_loaisp_bh = tk.Entry(frame_bh, width=40, font="Time 12")
combobox_loaisp_bh.place(x=170, y = 170)

# Số lượng
title_sl_bh = tk.Label(frame_bh, text="Số lượng tồn:",bg='#EEEEEE' , font="Time 12" )
title_sl_bh.place(x=50, y=200)
entry_sl_bh = tk.Entry(frame_bh,width=40,  font="Time 12")
entry_sl_bh.place(x=170, y = 200)


# Giá bán

title_giaban_bh = tk.Label(frame_bh, text="Giá bán:",bg='#EEEEEE' , font="Time 12" )
title_giaban_bh.place(x=50, y=230)
entry_gianban_bh = tk.Entry(frame_bh,width=40, font="Time 12")
entry_gianban_bh.place(x=170, y = 230)
# Ten khách hàng
title_tenkh = tk.Label(frame_bh, text="Tên khách hàng:",bg='#EEEEEE' , font="Time 12" )
title_tenkh.place(x=50, y=260)
entry_tenkh = tk.Entry(frame_bh,width=40, font="Time 12")
entry_tenkh.place(x=170, y = 260)

# SĐT khách hàng
title_sdtkh = tk.Label(frame_bh, text="Số điện thoại KH:",bg='#EEEEEE' , font="Time 12" )
title_sdtkh.place(x=50, y=290)
entry_sdtkh = tk.Entry(frame_bh,width=40, font="Time 12")
entry_sdtkh.place(x=170, y = 290)
# Số lượng bán
title_slban = tk.Label(frame_bh, text="Số lượng bán:",bg='#EEEEEE' , font="Time 12" )
title_slban.place(x=50, y=320)
entry_slban = tk.Entry(frame_bh,width=40, font="Time 12")
entry_slban.place(x=170, y = 320)
# Tìm kiếm
btn_tim_kiem_dh = tk.Button(frame_bh, text="Tìm kiếm", font="Time 9",  command=find_data_dh)
btn_tim_kiem_dh.place(x= 450, y=48)

btn_tim_kiem_msp = tk.Button(frame_bh, text="Tìm kiếm", font="Time 9",command= find_data_bh )
btn_tim_kiem_msp.place(x= 450, y=78)
# Thêm
btn_them_bh = tk.Button(frame_bh, text="Thêm mới", font="Time 13", command=add_data_bh)
btn_them_bh.place(x= 70, y =350)
# Sửa
btn_sua_bh = tk.Button(frame_bh, text="Sửa" ,font="Time 13" ,width=10 , command=edit_data_dh)
btn_sua_bh.place(x=230, y=350)
#Xóa

btn_xoa_bh = tk.Button(frame_bh, text="Xóa" ,font="Time 13" ,width=10, command=del_data_dh)
btn_xoa_bh.place(x=400, y=350)

# Xuat chi tiết đơn hàng
btn_donhang = tk.Button(frame_bh, text="Xuất file chi tiết" ,font="Time 13" , command=export_donhang)
btn_donhang.place(x=220, y=390)

# Danh sách đơn hàng
label_dmsp = tk.Label(frame_bh, text="DANH SÁCH ĐƠN HÀNG", font="Time 12 bold")
label_dmsp.place(x=800, y = 20)
# Create Treeview

columns  = ("DonHang", "MaSP","TenSP","HangSX","LoaiSP","SoLuongTon","GiaBan","TenKH","SoDT-KH", "SoLuongBan")
tree1 = ttk.Treeview(frame_bh, columns=columns, show='headings',height=25 ,selectmode='browse')
tree1.place(x=550, y =50)
for col in columns:
    tree1.heading(col, text=col)
    tree1.column(col, width=80)  

# Bind a function to item selection
tree1.bind("<ButtonRelease-1>", on_select_tree_bh)

populate_treeview(tree1,data_banhang)
# Pack Treeview
populate_treeview(tree, data)

frame_sp.pack()

frame_bh.pack_forget()
main.mainloop()
