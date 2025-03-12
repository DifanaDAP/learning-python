# Day 8 Fungsi dalam python

# Definisi fungsi
def sapa(nama):
    """Fungsi untuk menyapa orang"""
    print(f"hallo, {nama}! Selamat datang.")

# memanggil fungsi
sapa("didit")
sapa("fauzan")

# fungsi dengan return value
def kuadrat(angka):
    return angka ** 2

hasil = kuadrat(5)
print("Hasil Kuadrat : ", hasil)

# Fungsi dengan multiple parameter
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

luas = luas_persegi_panjang( 10, 5)
print("luas persegi panjang:", luas)

# Fungsi dengan nilai default
def salam(nama, pesan ="apa kabar?"):
    print(f"hallo {nama}, {pesan}")

salam("Didit")
salam("fauzan", "semoga hari mu menyenangkan")

# Fungsi dengan argument tak terbatas(*args)
def jumlahkan(*angka):
    return sum(angka)
print("Total jumlah:", jumlahkan(1, 2, 3, 4, 5))

# fungsi rekursif
def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n - 1)

print("faktorial dari 5:", faktorial(5))

# Latihan
# 1. Buat fungsi yang menerima nama dan usia, lalu mencetak pesan sapaan.
# 2. Buat fungsi yang menghitung luas lingkaran dengan jari-jari sebagai parameter.
# 3. Buat fungsi rekursif untuk menghitung bilangan Fibonacci ke-n.

# Latihan 1
print("latihan 1")

def sapaan(nama, usia):
    print((f"hallo, nama : {nama}, usia : {usia}"))

sapaan("didit", 24)

# Latihan 2
print("latihan 2")

def Luas_lingkaran(r):
    return 3.14 * (r **2)

luas = Luas_lingkaran(7)
print("luas lingkaran", luas)

# Latihan 3
print("latihan 3")

def fibonacci(n):
    if n <= 0:
        return "input harus bilangan positif"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("bilangan fibonacci ke 7:", fibonacci(7))
