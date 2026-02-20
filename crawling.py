# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.status_code)
# print(response.text)
# print (response.json())

# suhu = 30
# if suhu >= 32:
#     print("cuaca panas")
# elif suhu >= 25:
#     print("cuaca normal")
# else:
#     print("cuaca sejuk")

# voucher = input("Masukkan kode voucher: ")
# if voucher == "DISKON25":
#     print("Voucher valid, diskon diterapkan")
# else:
#     print("Voucher tidak valid")

# def jenis_film(choice):
#     if choice == 1:
#         print("Film Action")
#     elif choice == 2:
#         print("Film Comedy")
#     elif choice == 3:
#         print("Film Horror")
#     else:
#         print("Kategori tidak ditemukan")

# jenis_film(1)
# jenis_film(2)
# jenis_film(3)
# jenis_film(4)

# saldo = int(input("Masukkan jumlah saldo: "))

# if saldo > 0:
#     print("Saldo tersedia")
#     if saldo >= 1000000:
#         print("Saldo Anda banyak")
#     else:
#         print("Saldo Anda cukup")
# elif saldo == 0:
#     print("Saldo kosong")
# else:
#     print("Terjadi kesalahan data saldo")

# saldo = int(input("Masukkan saldo: "))

# if saldo > 100000 and saldo % 2 == 0:
#     print("Saldo cukup dan jumlahnya genap")
# elif saldo > 100000 and saldo % 2 != 0:
#     print("Saldo cukup tetapi jumlahnya ganjil")
# else:
#     print("Saldo tidak mencukupi")

# saldo = int(input("Masukkan saldo: "))
# status = "Positif" if saldo > 0 else "Kosong atau Negatif"
# print(f"Saldo rekening Anda adalah {status}")

# is_on = True
# if is_on:
#     print("lampu nyala")

#perulangan menggunakan for loop
# buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
# for perulangan in buah:
#     print("daftar stok buah", perulangan)

#perulangan menggunakan while loop
# buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
# i = 0
# while i < len(buah):
#     print("daftar stok buah", i)
#     i += 1

#perulangan menggunakan for loop dengan break statement
# buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
# for perulangan in buah:
#     if perulangan == "anggur":
#         break
#     print(perulangan)

#perulangan menggunakan for loop dengan continue statement
# buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
# for perulangan in buah:
#     if perulangan == "anggur":
#         continue
#     print(perulangan)

# buah = ["apel", "jeruk", "mangga"]
# for buah_pertama in buah:
#     for buah_kedua in range(1,4):
#         print(buah_pertama, buah_kedua)

# buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
# for i in range(len(buah)):
#     for j in range(i+1):
#         print(buah[j], end=" ")
#     print()

# buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
# n = len(buah)
# faktorial = 1

# for i in range(1, n+1):
#     faktorial *= i

#     print("faktorial:", faktorial)

# buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
# if buah == "anggur":
#     pass
# else:
#     print("stok kosong")

# buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
# def tambah_buah(buah1, buah2):
#     return buah1 + buah2

# keranjang1 = ["apel", "jeruk", "mangga"]
# keranjang2 = ["anggur", "pisang"]

# hasil = tambah_buah(keranjang1, keranjang2)
# print("Isi keranjang:", hasil)
# print("Jumlah buah:", len(hasil))

# total = 0

# def hitung_buah(buah1, buah2):
#     global total
#     total = len(buah1) + len(buah2)

# keranjang1 = ["apel", "jeruk", "mangga"]
# keranjang2 = ["anggur", "pisang"]

# hitung_buah(keranjang1, keranjang2)
# print(total)
