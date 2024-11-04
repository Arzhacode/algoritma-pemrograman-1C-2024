def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

# Meminta input dari pengguna
while True:
    total_input = input("Masukkan angka non-negatif untuk menghitung faktorial: ")
    
    if total_input.isdigit():  
        angka = int(total_input)
        if angka < 0:
            print("Mohon masukkan angka non-negatif.")
        else:
            hasil = faktorial(angka)
            print(f"{angka}! = {hasil}")
            break  # Keluar dari loop setelah hasil dihitung
    else:
        print("Input tidak valid. Mohon masukkan angka bulat.")
