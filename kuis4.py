# Studi kasus = sistem pengelolaan data produk

# Data data produk menggunakan Tuple
data_produk = ("P001", "Hp Oppo", "Elektronik")

# Data harga produk menggunakan List
harga_produk = [8500000, 7500000, 9500000, 8800000, 7800000]

# Data data menggunakan Dictionary
data = {
    "kode_produk": data_produk[0],
    "nama_produk": data_produk[1],
    "kategori": data_produk[2],
    "harga": harga_produk
}
print("==========================================")
print("       DATA SEBELUM MANIPULASI")
print("==========================================")


print("kode_produk            :", data["kode_produk"])
print("nama_produk           :", data["nama_produk"])
print("kategori  :", data["kategori"])
print("harga    :", data["harga"])

# Menambahkan nilai baru
data["harga"].append(4500000)
data["harga"].append(2500000)
print(data)

# mengubah nilai baru
indeks = data["harga"].index(7500000)
data["harga"][indeks] = 3225000

# Menghapus nilai
data["harga"].remove(7500000)

print("==========================================")
print("     DATA SETELAH MANIPULASI")
print("==========================================")

print("kode_produk            :", data["kode_produk"])
print("nama_produk           :", data["nama_produk"])
print("kategori  :", data["kategori"])
print("harga    :", data["harga"])

# Menghitung jumlah nilai
jumlah_data_harga = len(data["harga"])
total_harga = sum(data["harga"])
harga_rata_rata = total_harga / jumlah_data_harga
harga_tertinggi = max(data["harga_tertinggi"])
harga_terendah = min(data["harga_terendah"])

print("\==========================================")
print("       HASIL PERHITUNGAN NILAI")
print("==========================================")

print("Jumlah data harga    :", jumlah_data_harga)
print("Total harga     :", total_harga)
print("Harga rata-rata       :", harga_produk)
print("Harga tertinggi :", harga_tertinggi)
print("Harga terendah  :", harga_terendah)
