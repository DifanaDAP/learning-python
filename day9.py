# Day 9 Exception Handling dalam python

# Contoh dasar exception handling
try:
    angka = int(input("Masukkan sebuah angka: "))
    hasil = 10 / angka
    print("Hasil bagi 10 dengan angka tersebut adalah:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
except ValueError:
    print("Error: Harap masukkan angka yang valid!")
except Exception as e:
    print(f"Error tidak terduga: {e}")

# menggunakan finally
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File tidak ditemukan!")
finally:
    print("Eksekusi blok finally, apakah ada error atau tidak.")

# menggunakan raise untuk membuat error sendiri
def cek_umur(umur):
    if umur < 0 :
        raise ValueError("Umur tidak bisa negatif!")
    print("Umur anda: ", umur)

try:
    cek_umur(int(input("Masukan Umur: ")))
except ValueError as e:
    print("Error:", e)

# Latihan
# 1. Buat exception handling untuk menangani input string yang tidak bisa dikonversi ke float.
print("Latihan 1")
try:
    angka = float(input("Masukkan angka desimal: "))
    print("Angka yang dimasukkan:", angka)
except ValueError:
    print("Error: Harap masukkan angka yang valid!")

# 2. Tangani error jika pengguna memasukkan indeks yang melebihi panjang list.
print("latihan 2")
data = [10, 20, 30, 40 , 50]
try:
    indeks = int(input("Masukan indeks(0-4): "))
    print("Data pada indek tesebut:", data[indeks])
except IndexError:
    print("Error: Indeks di luar jangkauan!")
except ValueError:
    print("Error: Harap masukan angka yang valid")
    
# 3. Buat fungsi yang membaca file dan menangani jika file tidak ditemukan.
print("Latihan 3")
def baca_file(nama_file):
    try:
        with open(nama_file, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(" Error: File tidak ditemukan!")

#contoh pemangilan fungsi
baca_file("data.txt")
