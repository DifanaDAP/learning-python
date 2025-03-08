# Day 4 Fungsi & Lambda python

# Definisi fungsi sederhana
def sapa(nama):
    """"Fungsi untuk menyapa seseorang"""
    print(f"Hallo, {nama}! Selamat datang.")

# memanggil fungsi
sapa("Didit")
sapa("Fauzan")

# Fungsi dengan return value
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print("Hasil Penjumlahan: ", hasil)

# Fungsi Dengan Default Parameter
def perkenalan(nama, umur=18):
    print(f"nama: {nama}, umur: {umur}")

perkenalan("Didit") # Defaul umur 18
#overriding default parameter
perkenalan("Fauzan", 25)

# Fungsi dengan Keyword Arguments
def biodata(nama, kota):
    print(f"nama: {nama}, kota: {kota}")

biodata(kota="Bandung", nama="Didit")

# Fungsi Lambda (Anonymous fungtion)
kali_dua = lambda x: x * 2
print("Hasil kali dua:", kali_dua(4))

# Lambda dengan dua parameter
tambah_angka = lambda x, y : x + y
print("hasil lambda penjumlahan: ", tambah_angka(7, 3))

# Latihan
# 1. Buat fungsi untuk menghitung luas persegi panjang.
# 2. Buat fungsi yang menerima list angka dan mengembalikan angka terbesar.
# 3. Gunakan lambda untuk menghitung pangkat dua dari sebuah angka.

# Latihan1
print("latihan 1")
def persegi (p, l):
    return p * l

luas = persegi(9, 7)
print("Luas persegi panjang:", luas)

# Latihan 2
print("latihan 2")
def angka_terbesar (list):
    return max(list)

list_angka = [10,13,61,9,77, 47]
print("Angka terbesar dalam List:", angka_terbesar(list_angka))

# Latihan 3
print("latihan 3")
pangkat_dua = lambda x : x ** 2
print("Hasil pangkat dua :", pangkat_dua(6))