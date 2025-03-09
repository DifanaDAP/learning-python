# Day 5 List & Tuple dalam Python

# List - Struktur data yang bisa di ubah
angka_list = [1, 2, 3, 4, 5]
nama_list = ["Didit", "Fauzan", "Nasrulloh"]


# Akses Elemen list
print("Elemen Pertama:", angka_list[0])
print("Elemen Terakhir:", angka_list[-1])

# Menambahkan Elemen ke list
angka_list.append(6)
nama_list.insert(1, "abang")
print("list angka setelah append:", angka_list)
print("list nama setelah insert:", nama_list)

# Menghapus Elemen dari list
angka_list.remove(3)
del nama_list[2]
print("list angka setelah remove:", angka_list)
print("list nama setelah del:", nama_list)

# Iterasi List
total = 0
for angka in angka_list:
    total += angka
print("Total penjumlahan elemen angka_list:", total)

# List Comprehension
kuadrat = [x ** 2 for x in angka_list]
print("list kuadrat dari angka_list:", kuadrat)

# Tuple - Struktur data yang tidak bisa diubah
angka_tuple = (10, 20, 30, 40, 50)
nama_tuple = ("Didit", "Fauzan", "Nasrulloh")
print("Elemen pertama tuple:", angka_tuple[0])

# konversi antara list dan tuple
list_ke_tuple = tuple(angka_list)
tuple_ke_list = list(angka_tuple)
print("konversi list ke tuple:", tuple_ke_list)
print("konversi tuple ke list:", tuple_ke_list)

# Latihan
# 1. Buat list berisi nama teman-temanmu, lalu tambahkan dan hapus beberapa nama.
# 2. Buat tuple berisi angka favoritmu dan akses elemen tertentu.
# 3. Gunakan list comprehension untuk membuat list berisi angka genap dari 1-20.

#latihan 1
print("latihan 1")
nama_teman= ["Hafidz", "ilyasa", "zyan", "Dhea", "zahra"]
print("Nama teman awal:", nama_teman)

nama_teman.insert(3, "cinta")
print("Nama teman sudah di insert:", nama_teman)

del nama_teman[2]
print("nama teman sudah di del:", nama_teman)

# Latihan 2
print("latihan 2")
list_angka = [ 4, 8, 12, 23, 29]
print("list angka awal:", list_angka)

kurang = 10
for angka in list_angka:
    kurang -= angka
print("total pengurangan elemen list_angka", kurang)

pembagian = [x / 2 for x in list_angka]
print("List dibagi dari list angka:", pembagian)

# Latihan 3
print("latihan3")
angka_genap = [x for x in range(1, 21) if x % 2 == 0]
print("list angka genap 1 - 20:", angka_genap)