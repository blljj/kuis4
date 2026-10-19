nip = input("NIP : ")
nama = input("Nama Pegawai : ")
jabatan = input("Jabatan : ")
tgllahir = input("Tanggal lahir (dd-mm-yyyy): ")
tglkerja = input("Tanggal mulai bekerja (dd-mm-yyyy hh:mm:ss): ")
umur = int(input("Umur : "))
gaji = int(input("Gaji Pokok :"))
tunjangan = int(input("Tunjangan :"))
total_penghasilan = gaji * tunjangan 

identitas = (nip, nama, jabatan, tgllahir)
data = (umur, gaji, tunjangan, total_penghasilan)

pegawai = {
    "nim": identitas[0],
    "nama": identitas[1],
    "jabatan": identitas[2],
    "tgllahir": tgllahir,
    "tglmulai": tglkerja,
    "umur": umur,
}

from datetime import datetime
tanggal = datetime.strptime(tglkerja, "%d-%m-%Y")
tanggal = datetime.strptime(tgllahir, "%d-%m-%Y")

print("\n=== DATA MAHASISWA ===")
print("NIP  : ", nip)
print("Nama : ", nama)
print("Jabatan : ", jabatan)
print("Tanggal lahir : ", tgllahir)
print("Mulai Bekerja : ", tanggal)
print("Umur : ", umur)
print("Gaji Pokok : ", gaji)
print("Tunjangan : ", tunjangan)
print("Total penghasilan : ", total_penghasilan)

print("\n=== TIPE DATA ===")
print(type(pegawai["tgllahir"]))
print(type(pegawai["tglmulai"]))
print(type(pegawai["umur"]))
print(type(identitas["identitas"]))
print(type(data["penghasilan"]))     
print(type(pegawai["data pegawai"]))