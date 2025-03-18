# Day 7 : String Manupilation dalam python

# mendefinisikan string
text = "Belajar Python itu Menyenangkan!"

# mengakses karakter dalam string
print("Karakter pertama:", text[0])
print("Karakter Kedua:", text[1])

# mengiris string (Slicing)
print("kata pertama:", text[:7])
print("Kata kedua:", text[8:14])

# Mengubah case
print("Uppercase:", text.upper())
print("lowercase:", text.lower())
print("Title Case:", text.title())

# menghapus spasi dan karakter khusus
text2= "  Python Programming    "
print("Tenpa spasi awal dan akhir:", text2.strip())

# Menganti kata dalam string
print("ganti 'python' dengan 'Data Science':", text.replace("Python", "Data Science"))

# Memeriksa keberadaan kata dalam string
print("Apakah 'python' ada dalam teks?", "python" in text)

# Memisahkan dan mengabungkan string
kalimat = "Saya, suka, belajar, python"
list_kata = kalimat.split(",")
print("list kata:", list_kata)
print("GAbungkan kembali:", " ".join(list_kata))

# format string
nama = "Alice"
umur = 25
print(f"Nama saya {nama}, saya berusia {umur} tahun.")

# Latihan
# 1. Buat program yang menerima input nama dan mengubahnya menjadi uppercase.
print("latihan 1")
nama = input("input nama anda:")
print("Nama upper case :", nama.upper())

# 2. Cek apakah kata "Data" ada dalam input kalimat pengguna.
print("latihan 2")
kalimat2 = "aku adalah seorang data science"
print("apakah 'data' ada dalam kalimat?", "data" in kalimat2)

# 3. Ambil hanya huruf vokal dari sebuah string menggunakan looping.
print("latihan 3")
teks_vokal = input("Masukan sebuah kalimat:")
vokal = "aiueoAIUEO"
filter_vokal = "".join([huruf for huruf in teks_vokal if huruf in vokal])
print("Huruf vokal dalam teks:", filter_vokal)