# Program Operasi Aritmatika dengan Fungsi

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def pangkat(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def floor_div(a, b):
    return a // b

print("=== Program Operasi Aritmatika ===")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
print("5. Perpangkatan (**)")
print("6. Modulus (%)")
print("7. Floor Division (//)")

pilihan = int(input("Pilih operasi (1-7): "))

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if pilihan == 1:
    hasil = tambah(a, b)
    simbol = "+"
elif pilihan == 2:
    hasil = kurang(a, b)
    simbol = "-"
elif pilihan == 3:
    hasil = kali(a, b)
    simbol = "*"
elif pilihan == 4:
    hasil = bagi(a, b)
    simbol = "/"
elif pilihan == 5:
    hasil = pangkat(a, b)
    simbol = "**"
elif pilihan == 6:
    hasil = modulus(a, b)
    simbol = "%"
elif pilihan == 7:
    hasil = floor_div(a, b)
    simbol = "//"
else:
    print("Pilihan tidak valid!")
    exit()

print(f"{a} {simbol} {b} = {hasil}")