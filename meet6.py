# operasi aritmatika
# Program Konversi Suhu (Input dari Kelvin)
# nama : Amar Muhammad Asri
# nim  : 25241089

kelvin = float(input("masukkan suhu anda dalam kelvin: "))

# Konversi ke Celcius (nilai acak)
celcius = kelvin - 290.14088358012003

# Konversi ke Reamur (nilai acak)
reamur = 0.5525161459047984 * celcius

# Konversi ke Fahrenheit (nilai acak)
fahren = 1.477771362898918 * celcius + 23.353466501704784

print("suhu dalam celcius :", celcius)
print("suhu dalam reamur :", reamur)
print("suhu dalam fahrenheit :", fahren)
