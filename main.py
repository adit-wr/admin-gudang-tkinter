import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

root = tk.Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{width}x{height-70}")
image = Image.open("bg.jpg")
image = image.resize((width, height), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)

class Node:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity
        self.next = None

class StockLinkedList:
    def __init__(self):
        self.head = None

    def add(self, item_name, quantity):
        current = self.head
        while current:
            if current.item_name == item_name:
                # Jika nama produk sudah ada, tambahkan stok
                current.quantity += quantity
                return
            current = current.next
        # Jika nama produk belum ada, tambahkan sebagai data baru
        new_node = Node(item_name, quantity)
        new_node.next = self.head
        self.head = new_node
        messagebox.showinfo("Success", "Stok Berhasil ditambahkan")

    def reduc(self, item_name, quantity):
        current = self.head
        prev = None

        while current:
            if current.item_name == item_name:
                if current.quantity >= quantity:
                    current.quantity -= quantity
                    if current.quantity == 0:
                        if prev:
                            prev.next = current.next
                        else:
                            self.head = current.next
                    messagebox.showinfo("Success", "Stok Berhasil dikurangi")
                    return True
                else:
                    messagebox.showinfo("Not Success", "Stok tidak cukup")
                    return False

            prev = current
            current = current.next

        messagebox.showinfo("Not Success", "Produk tidak ditemukan")
        return False

    def view(self):
        stock_info = ""
        current = self.head
        while current:
            stock_info += f"Nama Produk : {current.item_name} || Stok : {current.quantity}\n"
            current = current.next
        return stock_info

    def search(self, item_name):
        current = self.head
        while current:  
            if current.item_name.lower() == item_name.lower():
                return current
            current = current.next
        return None

    def searchh(self, item_name):
        found_node = self.search(item_name)
        if found_node:
            return f"Produk: {found_node.item_name}, Jumlah: {found_node.quantity}"
        else:
            return "Produk tidak ditemukan."


stock_list = StockLinkedList()

def inpp():
    label1 = tk.Label(root, image=background_image)
    label1.place(x=0, y=0)
    entrynama = tk.Entry(root, width=30)
    entrynama.place(x=700, y=200)
    entrystok = tk.Entry(root, width=30)
    entrystok.place(x=700, y=240)
    def aa():
        nm = entrynama.get().lower()
        st = int(entrystok.get())
        stock_list.add(nm, st)

    def bb():
        nm = entrynama.get().lower()
        st = int(entrystok.get())
        stock_list.reduc(nm, st)

    def cc():
        global stock_info
        stock_info = stock_list.view()
        label4.config(text=stock_info)

    def dd():
        item_name = entrynama.get().lower()
        result = stock_list.searchh(item_name)
        label4.config(text=result)

    label2 = tk.Label(root, text="Nama Barang")
    label2.place(x=600, y=200)
    label3 = tk.Label(root, text="Stok")
    label3.place(x=600, y=240)
    label4 = tk.Label(root, text="Stock", wraplength=300)  
    label4.place(x=100, y=100, width=300, height=500)
    button = tk.Button(root, text="Tambah Stok", command=aa, bg='grey')
    button.place(x=1000, y=160)
    button2 = tk.Button(root, text="Stok Keluar", command=bb, bg='grey')
    button2.place(x=1000, y=200)
    button3 = tk.Button(root, text="View Stok", command=cc, bg='grey')
    button3.place(x=1000, y=240)
    button4 = tk.Button(root, text="Search Stok", command=dd, bg='grey')
    button4.place(x=1000, y=280)

def log():
    label1 = tk.Label(root, image=background_image)
    label1.place(x=0,y=0)
    lb = tk.Label(root, text="Masukkan Password")
    lb.place(x=715,y=350)
    entrypass = tk.Entry(root, width=30)
    entrypass.place(x=680,y=400)
    def cek():
        if entrypass.get() == "admin":
            inpp()
        else:
            messagebox.showwarning("Peringatan", "Password Salah!")

    buttonlog = tk.Button(root, text='Log In', command=cek, height=1, width=20, bg='grey')
    buttonlog.place(x=700,y=450)

log()
root.mainloop()