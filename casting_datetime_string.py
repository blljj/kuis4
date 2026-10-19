from datetime import datetime

sekarang = datetime.now()

tanggal_string = sekarang.strftime("%d-%m-%Y")
waktu_string = sekarang.strftime("%d-%m-%Y %H:%M:%S")

print("Tanggal:", tanggal_string)
print("Tanggal dan waktu:", waktu_string)
print("Tipe data:", type(waktu_string))