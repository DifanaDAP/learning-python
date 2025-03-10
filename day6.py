# Day 6 : Dictionary & set python

# Dictionary - Struktur data key value
mahasiswa = {
    "nama": "Didit",
    "umur": 22,
    "jurusan": "Elektro"
}

# Akses nilai dalam dictionary
print("Nama Mahasiswa:", mahasiswa["nama"])
print("Umur Mahasiswa:", mahasiswa.get("umur"))

# Menambah dan mengubah nilai dalam idctionary
mahasiswa["Universitas"] = "Universitas Muhammadiyah Bandung"
mahasiswa["umur"] = 23 # update umur
print("Dictionary Setelah update:", mahasiswa)

# Menghapus dictionary
del mahasiswa["jurusan"]
print("Dictionary setelah dihapus:", mahasiswa)

# Iterasi dictionary
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Set - Kumpulan elemen unik
angka_set = {1, 2, 3, 4, 5, 5, 3, 2, 5} # Duplikat akan di hapus otomatis
print("Set angka: ", angka_set)

# Menambahkan dan menghapus elemen pada set
angka_set.add(6)
angka_set.remove(3)
print("Set angka setelah update:", angka_set)

# Operasi himpunan pada set
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Irisan(intersection):", set_a & set_b)
print("Gabungan(union):", set_a | set_b)
print("Selisih(defference):", set_a - set_b)

# Latihan
# 1. Buat dictionary berisi data diri kamu dan tambahkan informasi baru.
# 2. Buat dua set berisi angka dan lakukan operasi union, intersection, dan difference.
# 3. Gunakan dictionary untuk menyimpan daftar nilai mata kuliah dan hitung rata-ratanya.
