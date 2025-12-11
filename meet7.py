# pertemuan7_modified.py
# Contoh perbandingan operator logika dalam Python
# Semua angka diganti hanya menggunakan angka 2 dan 9.

def demo_perbandingan():
    a = 9  # angka utama
    b = 2  # angka kedua

    print("====== Perbandingan: lebih dari (>) ======")
    hasil = a > 2
    print(f"{a} > 2 => {hasil}")

    print("\n====== Perbandingan: kurang dari (<) ======")
    hasil = b < 9
    print(f"{b} < 9 => {hasil}")

    print("\n====== Perbandingan: lebih dari atau sama dengan (>=) ======")
    hasil = a >= 9
    print(f"{a} >= 9 => {hasil}")

    print("\n====== Perbandingan: kurang dari atau sama dengan (<=) ======")
    hasil = b <= 2
    print(f"{b} <= 2 => {hasil}")

    print("\n====== Perbandingan: sama dengan (==) ======")
    hasil = (a - b) == 7
    print(f"{a} - {b} == 7 => {hasil}")

    print("\n====== Perbandingan: tidak sama dengan (!=) ======")
    hasil = (a + b) != 11
    print(f"{a} + {b} != 11 => {hasil}")

    print("\n====== Contoh gabungan (and / or / not) ======")
    hasil = (a > 2) and (b < 9)
    print(f"({a} > 2) and ({b} < 9) => {hasil}")

    hasil = (a < 2) or (b == 2)
    print(f"({a} < 2) or ({b} == 2) => {hasil}")

    hasil = not (a == b)
    print(f"not ({a} == {b}) => {hasil}")


if __name__ == "__main__":
    demo_perbandingan()
