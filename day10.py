# Day 10 list compehension dalam python

# List compehension untuk menbuat list dari range
angka = [ x for x in range(1, 11)]
print("List angka dari 1-10", angka)

# List comprehension dengan kondisi( hanya angka genap)
angka_genap = [x for x in range(1, 11) if x % 2 == 0]
print("List angka genap dari 1 - 10", angka_genap)

# List comprehension dengan operasi matematika(kuadrat dari 1 - 10)
kuadrat = [x ** 2 for x in range(1, 11)]
print("list kuadrat angka 1 - 10:", kuadrat)

# List comprehension dengan nested loop(kombinasi 2 list)
huruf = ['A', 'B', 'C']
number = [1, 2, 3]
kombinasi = [(h, n) for h in huruf for n in number]
print("kombinasi huruf dan angka:", kombinasi)

# List comprehension dengan fungsi
kata = "python"
huruf_vokal = [char for char in kata if char in 'aiueoAIUEO']
print("Huruf vokal dalam python", huruf_vokal)

# Latihan
# 1. Buat list comprehension untuk menghasilkan daftar bilangan kelipatan 3 dari 1-30.
# 2. Buat list comprehension untuk membalikkan string "Hello World" menjadi list karakter terbalik.
# 3. Gunakan list comprehension untuk membuat daftar panjang kata dari sebuah kalimat yang diberikan.

# Latihan 1
print("latihan 1")
kelipatan = [ x for x in range(3, 31) if x % 3 == 0]
print("List angka kelipatan 3:", kelipatan)

# Latihan 2
print("latihan 2")
kata1 = "Hello world"
terbalik = [x for x in kata1[::-1]]
print("karakter terbalik hello world:", terbalik)

#latihan 3
print("latihan 3")
kalimat = "Belajar Python itu menyenangkan"
panjang_kata = [len(kata) for kata in kalimat.split()]
print("panjang setiap kata dalam kalimat:", panjang_kata)
