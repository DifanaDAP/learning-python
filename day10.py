# Day 10 : File Handling dalam python

# membuka dan menulis file
with open("contoh.txt","w") as file:
    file.write("Hallo ini adalah contoh file. \n")
    file.write("Belajar file handling di Python!\n")

print("file telah ditulis.")

# membaca file
with open("contoh.txt", "r") as file:
    isi_file = file.read()
    print("Isi file:")
    print(isi_file)

# menambahkan (append) ke file
with open("contoh.txt", "a") as file:
    file.write("menambahkan baris baru ke file. \n")

print("Data Telah ditambahkan ke file")

# membaca baris per baris
with open("contoh.txt", "r") as file:
    print("Membaca file baris per baris:")
    for baris in file:
        print(baris.strip())


# Latihan
# 1. Buat program yang meminta pengguna memasukkan teks, lalu menyimpannya ke dalam file "user_input.txt".
print("latihan 1")
with open("user_input.txt", "w") as file:
    file.write(input("Masukan kalimat:"))

print("file telah di tulis")

# 2. Buat program yang membaca isi dari "user_input.txt" dan menampilkannya ke layar.
print("latihan 2")
with open("user_input.txt", "r") as file:
    baca_file = file.read()
    print("Baca file:")
    print(baca_file)
# 3. Buat program yang menyalin isi dari satu file ke file lain.
print("latihan 3")
def salin_file(sumber, tujuan):
    try:
        with open(sumber, "r") as file_sumber:
            data = file_sumber.read()
        with open(tujuan, "w") as file_tujuan:
            file_tujuan.write(data)
        print(f"Isi dari {sumber} telah disalin ke {tujuan}.")
    except FileNotFoundError:
        print("error: File sumber tidak ditemukan!")

# contoh pemanggilan fungsi
salin_file("user_input.txt", "salinan.txt")