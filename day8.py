# day 8 List comprehension dalam python

# list comprehension dasar
angka = [1, 2, 3, 4, 5]
kubik = [x**3 for x in angka]
print("Kubik dari angka:", kubik)

# List Comprehension dengan kondisi
angka_genap = [x for x in range(20) if x % 2 == 0]
print("Angka genap dari 0 - 19", angka_genap)

# list comprehension dendan nested loop
pasangan = [ ( x, y) for x in range (3) for y in range(3)]
print("Pasangan angka: ", pasangan)

# menggunakan list comprehension untuk manipulasi string
kata ="pemograman"
vokal = [huruf for huruf in kata if huruf in "aiuoeAIUEO"]
print("Huruf vokal dalam kata:", vokal)

# list konprehension dengan fungsi
angka_kuadrat = [pow(x,2) for x in range(10)]
print("Angka kuadrat dari 0-9:", angka_kuadrat)

# Latihan
# 1. Buat list comprehension untuk menghasilkan daftar angka ganjil dari 1-20.
print("latihan 1")
angka_ganjil = [ x for x in range(21)if x % 2 == 1]
print("Angka ganjil dari 1 - 21", angka_ganjil)

# 2. Buat list comprehension untuk mengubah semua huruf dalam sebuah string menjadi huruf kapital.
print("latihan 2")
teks = input("masukan sebuah teks: ")
teks_kapital = [huruf.upper() for huruf in teks]
print("Huruf kapital:", " ".join(teks_kapital))

# 3. Buat list comprehension untuk membalik urutan kata dalam sebuah kalimat.
kalimat = input("Masukan sebuah kalimat:")
kalimat_terbalik = " ".join(kalimat.split()[::-1])
print("Kalimat terbalik:", kalimat_terbalik)