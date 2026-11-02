
#input data_produk
nama_produk = input ("Sepatu Kulit")
kode_produk = input ("B39")


stok_awal =int(input("Stok Awal: "))
harga_produk =int(input("Harga Produk: "))

berat_produk = float(input("Berat Produk: "))
status_produk = input ("Status Produk : ")
ukuran = ['40, 41, 42. 43']
jumlah_produksi = int(input("Jumlah Produksi : "))
total_produksi = int(input("Total Produksi : "))
jumlah_terjual = int(input("Jumlah Terjual : "))

sisa_produksi = total_produksi - jumlah_terjual

data_produk ={
    "Nama Produk": nama_produk,
    "Kode Produk": kode_produk,
    "Stok Awal": stok_awal,
    "Harga Produk": harga_produk,
    "Berat Produk": berat_produk,
    "Status Produk": status_produk,
    "Ukuran": ukuran,
    "Jumlah Produksi": jumlah_produksi,
    "Total Produksi" : total_produksi,
    "Jumlah Terjual": jumlah_terjual,
    "Sisa Produk": sisa_produksi
}

print("Nama Produksi:", data_produk["nama produksi"])
print("Kode Produksi:", data_produk["kode produksi"])

