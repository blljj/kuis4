
from datetime import datetime

# 1. Input data pegawai
nip = input("NIP: ")
nama = input("Nama pegawai: ")
jabatan = input("Jabatan: ")

tanggal_lahir_input = input("Tanggal lahir (dd-mm-yyyy): ")
tanggal_mulai_input = input(
    "Tanggal mulai bekerja (dd-mm-yyyy hh:mm:ss): "
)

# 2 dan 3. Konversi tanggal menjadi Datetime
tanggal_lahir = datetime.strptime(
    tanggal_lahir_input, "%d-%m-%Y"
)

tanggal_mulai = datetime.strptime(
    tanggal_mulai_input, "%d-%m-%Y %H:%M:%S"
)

# 4. Input umur, gaji pokok, dan tunjangan
umur = int(input("Umur: "))
gaji_pokok = float(input("Gaji pokok: "))
tunjangan = float(input("Tunjangan: "))

# 5. Simpan identitas dalam tuple
identitas = (nip, nama, jabatan)

# 6. Simpan penghasilan dan umur dalam list
penghasilan = [umur, gaji_pokok, tunjangan]

# 7. Simpan seluruh data pegawai dalam dictionary
data_pegawai = {
    "NIP": nip,
    "Nama": nama,
    "Jabatan": jabatan,
    "Tanggal lahir": tanggal_lahir,
    "Tanggal mulai": tanggal_mulai,
    "Umur": umur,
    "Gaji pokok": gaji_pokok,
    "Tunjangan": tunjangan
}

# 8. Hitung total penghasilan
total_penghasilan = gaji_pokok + tunjangan

# 9. Tampilkan data pegawai
print("\n=== Data Pegawai ===")
print("NIP:", data_pegawai["NIP"])
print("Nama:", data_pegawai["Nama"])
print("Jabatan:", data_pegawai["Jabatan"])
print(
    "Tanggal lahir:",
    tanggal_lahir.strftime("%d-%b-%Y")
)
print(
    "Mulai bekerja:",
    tanggal_mulai.strftime("%d-%b-%Y %H:%M:%S")
)
print("Umur:", data_pegawai["Umur"])
print("Gaji pokok:", data_pegawai["Gaji pokok"])
print("Tunjangan:", data_pegawai["Tunjangan"])
print("Total penghasilan:", total_penghasilan)

# Menampilkan tipe data
print("\n=== Tipe Data ===")
print("Tanggal lahir:", type(tanggal_lahir))
print("Tanggal mulai:", type(tanggal_mulai))
print("Umur:", type(umur))
print("Identitas:", type(identitas))
print("Penghasilan:", type(penghasilan))
print("Data pegawai:", type(data_pegawai))