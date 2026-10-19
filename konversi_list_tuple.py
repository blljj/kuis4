# Data mahasiswa dalam List
data1 = input("Input data ke-1 : ")
data2 = input("Input data ke-2 : ")
data3 = input("Input data ke-3 : ")

mahasiswa = [ data1, data2, data3 ]

# Casting List ke Tuple
data_mahasiswa = tuple(mahasiswa)

# Menampilkan hasil
print("Data List  :", mahasiswa)
print("Data Tuple :", data_mahasiswa)
print("Tipe Data  :", type(data_mahasiswa))