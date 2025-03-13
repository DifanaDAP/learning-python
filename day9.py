# Day 9 Lambda function, map, and filter dalam python

# Lambda Fuction - Fungis anonom dalam satu baris
kuadrat = lambda X : X ** 2
print("kuadrat dari 4:", kuadrat(4))

penjumlahan = lambda a, b : a + b
print("Hasil penjumlahan 5 + 4:", penjumlahan(5, 4))

# mengunakan lambda dalam fungsi bawaan python
angka = [1, 2, 3, 4, 5]
kuadrat_angka = list(map(lambda x : x ** 2, angka))
print("list angka dikuadratkan:", kuadrat_angka)

# Menggunakan filter untuk menyaring data
angka_genap = list(filter(lambda x : x % 2 == 0, angka))
print("Angka genap dari list", angka_genap)

# Menggunakan lambda dalam sorting
mahasiswa = [("Alice", 22), ("Bob", 20), ("charlie", 23)]
mahasiswa.sort(key = lambda x : x[1]) # sort berdasarkan umur
print("Mahasiswa setelah diurutkan berdasarkan umur : ", mahasiswa)

# Latihan
# 1. Buat lambda function untuk menghitung luas lingkaran dengan jari-jari sebagai parameter.
# 2. Gunakan map() untuk mengubah list suhu dari Celcius ke Fahrenheit.
# 3. Gunakan filter() untuk menyaring angka yang lebih besar dari 10 dalam sebuah list.

# Latihan 1
print("latihan 1")

lingkaran = lambda x : (x ** 2) * 3.14
print("luas lingkaran : ", lingkaran(7))

# Latihan 2
print("latihan 2")
celsius = [0, 20, 30, 37, 100]
farenheit = list(map(lambda c : (c * 9/5) + 32, celsius))
print("Suhu Farenheit:", farenheit)

# Latihan 3
print("latihan 3")

list_angka = [4, 3, 7, 9, 12, 18, 20]
menyaring = list(filter(lambda x : x > 10, list_angka))
print("Angka sesudah di saring", menyaring)
