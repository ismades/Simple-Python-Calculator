# Program Kalkulator Sederhana dengan Python

# Input angka dari pengguna
A = int(input("Masukkan angka pertama: "))
B = int(input("Masukkan angka kedua: "))

# Operasi Matematika
penjumlahan = A + B
pengurangan = A - B
perkalian = A * B
pembagian = A / B if B != 0 else "Tidak bisa dibagi dengan nol"

# Menampilkan hasil perhitungan
print("\n=========== Nomor 1: Operasi Aritmatika ==========")
print(f"Hasil penjumlahan: {penjumlahan}")
print(f"Hasil pengurangan: {pengurangan}")
print(f"Hasil perkalian: {perkalian}")
print(f"Hasil pembagian: {pembagian}")

# Operasi Perbandingan
print("\n=========== Nomor 2: Operasi Perbandingan ==========")
print(f"Hasil dari perbandingan A > B: {A > B}")
print(f"Hasil dari perbandingan A < B: {A < B}")
print(f"Hasil dari perbandingan A == B: {A == B}")
print(f"Hasil dari perbandingan A != B: {A != B}")
print(f"Hasil dari perbandingan A >= B: {A >= B}")
print(f"Hasil dari perbandingan A <= B: {A <= B}")

# List Data
buah = ["Pisang", "Semangka", "Jeruk", "Alpukat", "Sirsak"]
sayuran = ["Pakcoi", "Bayam", "Kangkung", "Sawi", "Terong", "Kelor", "Pare"]
makanan_kesukaan = ["Ayam Geprek", "Takoyaki", "Nasi Goreng"]

print("\n=========== Nomor 3: Data List ==========")
print(f"Daftar Buah: {buah}")
print(f"Daftar Sayuran: {sayuran}")
print(f"Makanan Kesukaan: {makanan_kesukaan}")

# Mengakses Elemen dalam List
print("\n=========== Nomor 4: Mengakses Elemen List ==========")
print(f"Buah kedua: {buah[1]}")
print(f"Sayuran ketujuh: {sayuran[6]}")
print(f"Makanan favorit pertama: {makanan_kesukaan[0]}")
