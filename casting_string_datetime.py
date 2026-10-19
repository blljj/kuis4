from datetime import datetime

tanggal_input = input("Masukkan tanggal (dd-mm-yyyy): ")

tanggal = datetime.strptime(tanggal_input, "%d-%m-%Y")

print("Tanggal:", tanggal)
print("Tahun:", tanggal.year)
print("Bulan:", tanggal.month)
print("Hari:", tanggal.day)
print("Tipe data:", type(tanggal))