#Soal 1
# Inisialisasi dictionary alat kesehatan
alat_kesehatan = {
    "pengukur_tekanan_darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0,
}

# Fungsi untuk menambah atau mengurangi jumlah alat
def update_alat(alat, jumlah):
    if alat in alat_kesehatan:
        alat_kesehatan[alat] += jumlah
        if alat_kesehatan[alat] < 0:
            alat_kesehatan[alat] = 0
    else:
        print("Nama alat tidak ditemukan.")

# Fungsi untuk menampilkan alat yang dipinjam
def lihat_alat():
    print("\nAlat yang sedang dipinjam:")
    for alat, jumlah in alat_kesehatan.items():
        if jumlah > 0:
            print(f"- {alat.replace('_', ' ').capitalize()}: {jumlah}")
    print()

# Program utama dengan menu sederhana
while True:
    print("Menu:")
    print("1. Pinjam alat")
    print("2. Kembalikan alat")
    print("3. Tukar alat")
    print("4. Lihat alat yang dipinjam")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":  # Pinjam alat
        alat = input("Masukkan nama alat yang ingin dipinjam: ").lower().replace(" ", "_")
        jumlah = int(input("Masukkan jumlah yang ingin dipinjam: "))
        update_alat(alat, jumlah)

    elif pilihan == "2":  # Kembalikan alat
        alat = input("Masukkan nama alat yang ingin dikembalikan: ").lower().replace(" ", "_")
        jumlah = int(input("Masukkan jumlah yang ingin dikembalikan: "))
        update_alat(alat, -jumlah)

    elif pilihan == "3":  # Tukar alat
        alat_tukar = input("Masukkan nama alat yang ingin ditukar: ").lower().replace(" ", "_")
        jumlah_tukar = int(input("Masukkan jumlah yang ingin ditukar: "))
        update_alat(alat_tukar, -jumlah_tukar)

        alat_pengganti = input("Masukkan nama alat pengganti: ").lower().replace(" ", "_")
        jumlah_pengganti = int(input("Masukkan jumlah alat pengganti yang diterima: "))
        update_alat(alat_pengganti, jumlah_pengganti)

    elif pilihan == "4":  # Lihat alat yang dipinjam
        lihat_alat()

    elif pilihan == "5":  # Keluar
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")