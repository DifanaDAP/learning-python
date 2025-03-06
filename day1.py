# Day 1 : Variabel & type data

#variabel
nama = "Didit" # string
umur = 24 # Interger
tinggi = 167.5 # float
is_student = True # Boolean

# Print variabel
print("Nama:", nama, "- Tipe:", type(nama))
print("Umur:", umur, "- Tipe:", type(umur))
print("Tinggi:", tinggi, "- Tipe:", type(tinggi))
print("Mahasiswa:", is_student, "- Tipe:", type(is_student))

# multiple assigment
x, y, z, = 10, 20, 30
print("x:",x, "y:",y, "z:",z)

#konversi type data
angka_str = "100"
angka_int = int(angka_str) # konversi string ke interger
print("angka dalam bentuk string:", angka_str, "- type:", type(angka_str))
print("angka setelah konversi : ", angka_int, "- type:", type(angka_int))

# input data
#nama_user = input("masukan nama anda:")
#print("hallo", nama_user)

# Latihan
# 1. Coba deklarasikan 3 variabel dengan tipe data yang berbeda
# 2. Gunakan fungsi type() untuk mengecek tipe data variabel tersebut
# 3. Coba konversikan salah satu variabel ke tipe data lain

#latihan 1 & 2
nama, umur, tinggi = "fauzan", 24, 170.5
print("nama:", nama, "- type:", type(nama))
print("umur:", umur, " - type:", type(umur))
print("tinggi:", tinggi, "-type:", type(tinggi))

# latihan 3
umur_str= "24"
umur_int = int(umur_str)
print("umur dalam bentuk string:", umur_str, "- type:", type(umur_str))
print("umur setelah konversi:", umur_int, "- type:", type(umur_int))