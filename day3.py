# Day 3 Struktur kontrol (if-Else, Looping)

# Struktur kontrol if-else
umur= 20
if umur < 18 : 
    print("Kamu masih di bawah umur")
elif umur >= 18 and umur < 60:
    print("kamu sudah dewasa")
else:
    print("kamu sudah tua")

# looping dengan for
print("looping dengan for")
for i in range(1, 6):  # range (1,6) berarti dari 1 sampai 5
    print(f"Interasi ke-{i}")

# looping dengan while
print("looping dengan while")
n = 5
while n > 0:
    print(f"NIlai n: {n}")
    n -= 1 # mengurangi n setiap iterasi

# looping dengan break dan continue
print("looping dengan break dan continue")
for i in range (1, 8):
    if i == 3:
        print("lewati iterasi ke 3 dengan continue")
        continue # lewati iterasi ke 3
    if i == 7:
        print("hentikan loop dengan break di iterasi ke 7")
        break # hentikan loop
    print(f"iterasi ke-{i}")

# Latihan
# 1. Ubah nilai umur dan lihat hasil percabangan if-else.
# 2. Buatlah loop for yang mencetak angka kelipatan 2 dari 2 hingga 10.
# 3. Buatlah loop while yang mencetak angka dari 10 hingga 1.

# jawaban 
print("latihan 1")
umur = 60
if umur > 30:
    print("Kamu sudah tua")

print("latihan 2")
for i in range (2, 11, 2):
    print(f"Iterasi ke-{i}")

print("latihan 3")
n = 10
while n > 0:
    print(f"nilai n: {n}")
    n-=1