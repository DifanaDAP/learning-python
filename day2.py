#day 2 : operator python

# Operator Atirmatika
angka1 = 10
angka2 = 3
print("penjumlahan:", angka1 + angka2) # 13
print("pengurangan:", angka1 - angka2) # 7
print("perkalian:", angka1 * angka2) # 30
print("pembagian:", angka1 / angka2) # 3.33
print("pembagian bulat:", angka1 // angka2) # 3
print("modulus:", angka1 % angka2) #1
print("pangkat:", angka1 ** angka2) # 1000

# Operator perbandingan
print("apakah 10 > 3:", angka1 > angka2) # true
print("apakah 10 < 3:", angka1 < angka2) # false
print("apakah 10 == 3:", angka1 == angka2) # false
print("apakah 10 != 3:", angka1 != angka2) # true

# Operator Logika
benar = True
salah = False
print("AND:", benar and salah) # false
print("OR:", benar or salah) # true
print("NOT:", not benar) # false

# operator Assigment
x = 5
x +=3 # sama dengan x = x + 3
print("Nilai X setelah +=4:", x)
x *= 2 # sama dengan x = x * 2
print("Nilai x setelah *=2:", x)

# Operator Membership
list_data = [1, 2, 3, 4, 5]
print("Apakah 3 ada dalam list? :", 3 in list_data) # true
print("Apakah 10 ada dalam list? :", 10 in list_data) # false

# Operator Identitas
angka_a = 10
angka_b = 10
print("Apakah angka_a adalah angka_b?", angka_a is angka_b) # true
print("Apakah angka_a bukan angka_b?", angka_a is not angka_b) # false

# Latihan
# 1. Coba gunakan operator aritmatika lainnya dengan angka yang berbeda.
# 2. Gunakan operator logika dengan kombinasi nilai True dan False.
# 3. Coba gunakan operator membership dengan string atau list lainnya.

print("Latihan")
# latihan 1
angka3 = 30
angka4 = 11
print("penjumlahan:", angka3 + angka4)
print("perkalian:", angka3 * angka4)
print("modulus:", angka3 % angka4)
print("pembagian bulat:", angka3 // angka4)

# latihan 2
satu = True
kosong = False
print("AND:", satu and kosong)
print("OR:", satu or kosong)
print("NOT:", not satu)
print("NAND:", not(satu and kosong))
print("NOR:", not( satu or kosong))

# latihan 3
list = ["aku", "kamu", "dia"]
print("Apakah aku ada dalam list?", "aku" in list)
print("apakah aku tidak ada dalam list?", "aku" not in list)