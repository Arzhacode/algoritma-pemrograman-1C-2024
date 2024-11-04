def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    n = input("Masukkan angka (harus positif) untuk menghitung bilangan Fibonacci: ")
    if n.isdigit():  
        n = int(n)
        if n < 0:
            print("Input tidak valid. Mohon masukkan angka positif.")
        else:
            hasil = fibonacci(n)
            print(f"Bilangan Fibonacci ke-{n} adalah {hasil}")
            break  # Keluar dari loop setelah hasil dihitung
    else:
        print("Input tidak valid. Mohon masukkan angka positif.")
