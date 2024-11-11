#SOAL 3
barang_list = {
    'darurat': [],
    'biasa': [],
    'non-darurat': []
}

def tambah_barang():
    nama_barang = input("Nama Barang: ")
    id_barang = input("ID Barang: ")
    prioritas = input("Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ").lower()

    while prioritas not in ['darurat', 'biasa', 'non-darurat']:
        print("Prioritas tidak valid. Harap pilih Darurat, Biasa, atau Non-Darurat.")
        prioritas = input("Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ").lower()

    barang = (id_barang, nama_barang)
    barang_list[prioritas].append(barang)

    print("Barang berhasil ditambahkan!")#

def tampilkan_barang():
    if not any(barang_list.values()):
        print("Belum ada barang yang ditambahkan.")
    else:
        print("Daftar Barang yang Dikirim:")
        for prioritas, barang_list_prio in barang_list.items():
            if barang_list_prio:
                print(f"{prioritas.capitalize()}:")
                for barang in barang_list_prio:
                    print(f"ID Barang: {barang[0]}, Nama Barang: {barang[1]}")

def main():
    while True:
        tambah_barang()

        tampilkan_barang()

        lagi = input("Apakah Anda ingin menambahkan barang lain? (ya/tidak): ").lower()
        if lagi != "ya":
            print("Terima kasih!!!!!!!")
            break

main()