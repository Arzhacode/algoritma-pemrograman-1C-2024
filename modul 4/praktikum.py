# # praktikum py struktur perulangan
# for i in range (1,4) :
#     print(f"loop luar i = (i) ")

#     for j in range (1,4) :
#         print (f"loop di dalam j (j) ")

# latihan kedua
# a = 24
# b = 36

# while b!=0:
#    a = b
#    b = a % b 

# print (f"FPB nya adalah : {a} ")

#latihan ketiga
# n = 100
# a = 0
# b = 1
# print ("bilangan fibonacci hingga " , n)
# while a <= n:
#     print (a, end= " ")
#     a,b + b, a + b

# latihan keempat
# n = 15

# for i in range (1, n +1) :

#     for j in range (n-1):
#         print(" ", end= " ")
#     for k in range(1, i+1):
#         print(k, end=" ")
#     print()

    # latihan kelima

# # Mengambil input dari pengguna
# N = int(input("Masukkan ukuran sisi N: "))
# karakter = input("Masukkan karakter pilihan (misalnya 'X' atau 'O'): ")

# # Ukuran total dari belah ketupat
# ukuran = 2 * N - 1

# # Membuat pola belah ketupat
# for i in range(ukuran):
#     # Menghitung jumlah spasi dan karakter pada setiap baris
#     if i < N:
#         spasi = N - i - 1
#         karakter_baris = i + 1
#     else:
#         spasi = i - N + 1
#         karakter_baris = ukuran - i

#     # Mencetak spasi
#     print(' ' * spasi, end='')

#     # Mencetak pola checkerboard
#     for j in range(karakter_baris):
#         if (i + j) % 2 == 0:  # Jika kondisi genap, cetak karakter
#             print(karakter, end='')  # Mencetak karakter pilihan
#         else:
#             print(' ', end='')  # Mencetak spasi

#     # Pindah ke baris berikutnya
#     print()

# Mengambil input dari pengguna
# N = int(input("Masukkan ukuran sisi N: "))
# karakter = input("Masukkan karakter yang akan dibentuk contohnya di soal pakai x atau o : ")

# ukuran = 2 * N - 1

# # Membuat pola belah ketupat
# for i in range(ukuran):
#     # Menghitung jumlah spasi
#     if i < N:
#         spasi = N - i - 1
#     else:
#         spasi = i - N + 1

#     # Mencetak spasi
#     print(' ' * spasi, end='')

#     for j in range(ukuran - 2 * spasi):
#         if (i + j) % 2 == 0:  # Jika kondisi genap, cetak karakter
#             print(karakter, end='')  # Mencetak karakter pilihan
#         else:
#             print(' ', end='')  # Mencetak spasi

#     # Pindah ke baris berikutnya
#     print()

# # Mengambil input dari pengguna
# N = int(input("Masukkan ukuran sisi N: "))
# karakter = input("Masukkan karakter pilihan (misalnya 'X' atau 'O'): ")

# # Ukuran total dari belah ketupat
# ukuran = 2 * N - 1

# # Membuat pola belah ketupat
# for i in range(ukuran):
#     # Menghitung jumlah spasi dan karakter pada setiap baris
#     if i < N:
#         spasi = N - i - 1
#         karakter_baris = i + 1
#     else:
#         spasi = i - N + 1
#         karakter_baris = ukuran - i

#     # Mencetak spasi
#     print(' ' * spasi, end='')

#     # Mencetak pola checkerboard
#     for j in range(karakter_baris):
#         if (i + j) % 2 == 0:  # Jika kondisi genap, cetak karakter
#             print(karakter, end='')  # Mencetak karakter pilihan
#         else:
#             print(' ', end='')  # Mencetak spasi

#     # Pindah ke baris berikutnya
#     print()

# angka = int(input("masukkan ukuran yang ingin dibentuk belah ketupat: "))
# bentuk = input("masukkan bentuk (X/O): ").upper()

# if bentuk not in ['X','O']:
#     print("Not valid! Masukkan hanya 'X' atau 'O'.")
# else:
#     for i in range(1, angka + 1):
#         for j in range(angka - i):
#             print(' ', end=' ')
#         for k in range(1, i + 1):
#             print(bentuk, end="   ")
#         print()

#     for bawah in range(1, angka + 1):
#         for k in range(1, bawah + 1):
#             print(' ', end=" ")
#         for J in range(angka - bawah):
#             print(bentuk, end="   ")
#         print()

# n=100
# a,b = 0,1

# print("Bilangan Fibonacci hingga", n)
# while a<= n :
#     print (a, end=" ")
#     a,b=b, a + b

n = 5

for i in range(1, n+1) :

    for j in range(n-1):
      print('', end='')

    for k in range(1, i+1) :
       print(k, end = '')
       print()
