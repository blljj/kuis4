from datetime import datetime

nama = input("Nama mahasiswa : ")
nim = input("NIM : ")
umur = int(input("Umur : "))
ipk = float(input("IPK : "))

hobi_1 = input("Hobi 1 : ")
hobi_2 = input("Hobi 2 : ")
#menyimpan sebagai list
hobi = [hobi_1, hobi_2]

berat_badan=  float(input("Berat Badan : "))
tinggi_badan =  float(input("Tinggi Badan : "))
#menyimpan sebagai tuple
bb_tb = (berat_badan, tinggi_badan)
teks_lahir = input("Tanggal lahir (dd-mm-yyyy): ")

tanggal_lahir = datetime.strptime(teks_lahir, "%d-%m-%Y")

identitas = (nim, nama)
akademik = [umur, ipk]

mahasiswa = {
    "nim": identitas[0],
    "nama": identitas[1],
    "umur": akademik[0],
    "ipk": akademik[1],
    "hobi": hobi,
    "bb_tb": bb_tb,
    "tanggal_lahir": tanggal_lahir
}

tanggal_format = mahasiswa["tanggal_lahir"].strftime("%d-%b-%Y")

print("\n=== DATA MAHASISWA ===")
print("NIM :", mahasiswa["nim"])
print("Nama :", mahasiswa["nama"])
print("Umur :", mahasiswa["umur"])
print("IPK :", mahasiswa["ipk"])
print("Hobi : ", mahasiswa["hobi"])
print("Berat Badan, Tinggi Badan : ", mahasiswa["bb_tb"]),
print("Tanggal lahir:", tanggal_format)

print("data identitas : ", identitas)
print("data akademik : ", akademik)
print("data mahasiswa : ", mahasiswa)

print("\n=== TIPE DATA ===")
print(type(mahasiswa["nim"]))
print(type(mahasiswa["umur"]))
print(type(mahasiswa["ipk"]))
print(type(mahasiswa["hobi"]))
print(type(mahasiswa["bb_tb"]))     
print(type(mahasiswa["tanggal_lahir"]))
print(type(identitas))
print(type(akademik))
print(type(mahasiswa))