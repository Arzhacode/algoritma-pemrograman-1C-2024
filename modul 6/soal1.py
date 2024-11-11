# SOAL 1

# Fungsi untuk input data karyawan
def input_karyawan():
    karyawan_list = []
    
    # Input 5 data karyawan
    for i in range(5):
        print(f"\nData Karyawan ke-{i+1}:")
        
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")

        # Menyimpan data dalam bentuk tuple
        karyawan = (nip, nama, alamat, departemen, jabatan)
        karyawan_list.append(karyawan)

    return karyawan_list

# Fungsi untuk menampilkan seluruh data karyawan
def tampilkan_data(karyawan_list):
    print("\nDaftar Karyawan:")
    for karyawan in karyawan_list:
        print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

# Fungsi untuk pencarian data berdasarkan atribut tertentu
def cari_data(karyawan_list, pencarian, atribut_index):
    print(f"\nHasil pencarian berdasarkan atribut {atribut_index}: '{pencarian}':")
    found = False
    for karyawan in karyawan_list:
        if pencarian.lower() in karyawan[atribut_index].lower():  # Perbandingan case-insensitive
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
            found = True
    if not found:
        print("Data tidak ditemukan.")


karyawan_list = input_karyawan()  
tampilkan_data(karyawan_list)  

# Pencarian berdasarkan atribut
print("\nPencarian Data Karyawan")
atribut = input("Masukkan atribut yang ingin dicari (nip, nama, alamat, departemen, jabatan): ").lower()

if atribut == 'nip':
    atribut_index = 0
elif atribut == 'nama':
    atribut_index = 1
elif atribut == 'alamat':
    atribut_index = 2
elif atribut == 'departemen':
    atribut_index = 3
elif atribut == 'jabatan':
    atribut_index = 4
else:
    print("Atribut tidak valid. Program dihentikan.")
    exit()  # Program KELUAR jika tidak valid

pencarian = input(f"Masukkan nilai {atribut} yang ingin dicari: ")

# Mencari data berdasarkan atribut yang dipilih
cari_data(karyawan_list, pencarian, atribut_index)
