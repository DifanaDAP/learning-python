# Day 11: Dictionary Comprehension in python

# Menbuat dictioanary dengan dict comprehension
angka_genap_kuadrat = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Dictionary bilangan genap dan kuadratnya: ",angka_genap_kuadrat)

# Membalik key dan value dalam dictionary
mahasiswa = {"Andi": 21, "Budi":20, "Citra": 22}
mahasiswa_umur_kali2 = {key: umur * 2 for (key, umur) in mahasiswa.items()}
print("Dictionary dengan umur dikali 2:", mahasiswa_umur_kali2)

# membuat dictionary dari dua list
nama = ["Ayu", "Dewi", "Rina"]
umur= [19, 21, 22]
mahasiswa_dict = {nama[i] : umur[i] for i in range(len(nama))}
print("Dictionary dari dua list:", mahasiswa_dict)

# Latihan
# 1. Buat dictionary comprehension yang mengonversi list angka menjadi dictionary, 
#    dengan angka sebagai kunci dan nilai faktorial dari angka tersebut sebagai nilai.

# 2. Buat dictionary comprehension yang menukar kunci dan nilai dalam dictionary berikut:
# contoh_dict = {"a": 1, "b": 2, "c": 3}
# Hasil yang diharapkan: {1: "a", 2: "b", 3: "c"}

# 3. Buat dictionary comprehension yang mengambil daftar nama dan menghitung panjang setiap nama,
# lalu menyimpannya dalam bentuk dictionary dengan nama sebagai kunci dan panjang sebagai nilai.

# Latihan 1
print("Latihan 1")
import math
angka_list = [1, 2, 3, 4, 5]
faktorial ={x : math.factorial(x) for x in angka_list}
print("Dictionary dengan angka dan nilai faktorialnya:", faktorial)

# Latihan 2
print("Latihan 2")
contoh_dict = {"a": 1, "b": 2, "C": 3}
terbalik = {value : key for key, value in contoh_dict.items()}
print("dictionaru dengan key dan value tertukar: ", terbalik)

# Latihan 3
print("Latihan 3")
nama_list = ["Alice", "bob", "Charlie"]
panjang_nama_dict = {nama : len(nama) for nama in nama_list}
print("Dictionari dengan pangjan setiap nama:", panjang_nama_dict)