nip = input("Input NIP : ")
nama = input("Input Nama : ")
tgllahir = input("Tanggal lahir (dd-mm-yyyy): ")
ahli_1 = input("Keahlian 1 : ")
ahli_2 = input("Keahlian 2 : ")
ahli_3 = input("Keahlian 3 : ")
keahlian = tuple([ahli_1, ahli_2, ahli_3])
gaji = int(input("Gaji Pokok :"))
komisi = int(input("Komisi :"))
total_gaji = gaji + komisi
pajak = float(0.1 * total_gaji)


from datetime import datetime
tanggal = datetime.strptime(tgllahir, "%d-%m-%Y")
print("NIP anda : ", nip)
print("Nama anda : ", nama)
print("Tgllahir anda : ", tanggal)
print("Keahlian anda : ", keahlian)
print("Gaji Pokok : ", gaji)
print("Komisi : ", komisi)
print("Total gaji : ", total_gaji)
print("Pajak : ", pajak)