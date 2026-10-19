from datetime import datetime

teks = input("Masukkan tanggal dan waktu: ")

tanggal_waktu = datetime.strptime(
    teks, "%d-%b-%Y %H:%M:%S"
)

print("Hasil:", tanggal_waktu)
print("Tipe data:", type(tanggal_waktu))