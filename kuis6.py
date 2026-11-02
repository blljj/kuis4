from datetime import datetime

tanggal = datetime.now().strftime("%d-%m-%Y")
print("Tanggal Peminjaman :", tanggal)

# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM: ")
status_anggota = input("Apakah anggota perpustakaan? (Y/N): ").upper()
jumlah_buku = int(input("Jumlah buku yang sedang dipinjam: "))
status_denda = input("Apakah memiliki denda? (Y/N): ").upper()

# Menentukan kelayakan peminjaman
if status_anggota == "N":
    status_peminjaman = "Tidak diperbolehkan meminjam"
    sisa_kuota = 0

elif status_denda == "Y":
    status_peminjaman = "Tidak diperbolehkan meminjam"
    sisa_kuota = 0

elif jumlah_buku >= 5:
    status_peminjaman = "Kuota peminjaman habis"
    sisa_kuota = 0

else:
    status_peminjaman = "Boleh meminjam buku"

sisa_kuota = 5 - jumlah_buku

# Menyimpan data ke dalam dictionary
peminjaman = {
    "tanggal": tanggal,
    "nim": nim,
    "nama": nama,
    "status_anggota": status_anggota,
    "jumlah_buku": jumlah_buku,
    "status_denda": status_denda,
    "sisa_kuota": sisa_kuota,
    "status_peminjaman": status_peminjaman
}

print("\n=== DETAIL PEMINJAMAN ===")
print("Tanggal Peminjaman  :", peminjaman["tanggal"])
print("Nama Mahasiswa      :", peminjaman["nama"])
print("Nim                 :", peminjaman["nim"])
print("Status Anggota      :", peminjaman["status_anggota"])
print("Jumlah Buku         :", peminjaman["jumlah_buku"])
print("Status Denda        :", peminjaman["status_denda"])
print("Sisa Kouta          :", peminjaman["sisa_kuota"])
print("Status Peminjaman   :", peminjaman["status_peminjaman"])