# Day 7 Control Flow (percabangan & perulangan) dalam python

# percabangan (if, elif, else)
umur = 20
if umur < 20:
    print("kamu masih anak-anak")
elif 18<= umur < 25:
    print("kamu dewasa muda")
else:
    print("kamu sudah dewasa")

#perulangan For
buah = ["apel", "jeruk", "mangga", "anggur"]
for b in buah :
    print("buah", b)

# perulangan dengan range
for i in range( 1, 6):
    print("nomorL", i)

# perulangan  while
angka = 1
while angka < 5:
    print("angka", angka)
    angka +=1

# break dan continue dalam loop
for i in range( 1, 10):
    if i == 5:
        break # keluar dari loop jika i = 5
    print("iterasi:", i)

for i in range(1, 10):
    if i % 2 == 0:
        continue # lewati iterasi jika i genap
    print("Angka ganjil", i)

# Nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")


# Latihan
# 1. Buat program yang meminta input usia pengguna, lalu cetak kategori usia (anak, remaja, dewasa).
# 2. Buat perulangan for yang mencetak angka kelipatan 3 dari 1-30.
# 3. Gunakan while loop untuk menghitung jumlah angka dari 1-10.

# latihan 1
print("latihan 1")

usia = int(input("masukan usia anda: "))
if usia < 18:
    print("kamu masih anak-anak")
elif 18 <= usia < 25:
    print("Kamu sudah remaja")
else:
    print("kamu sudah dewasa")

# latihan 2
print("latihan 2")
for i in range(3, 31, 3):
    print("kelipatan 3: ", i)

# latihan 3
print("latihan 3")
jumlah =0
angka = 1
while angka <= 10:
    jumlah += angka
    angka += 1
print("jumlah angka dari 1-10:", jumlah)