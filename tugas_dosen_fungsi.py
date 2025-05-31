# Fungsi untuk membalik setiap kata dalam kalimat
def reverse_per_kata(kalimat):
    # Memisahkan kata-kata dalam kalimat
    kata_list = kalimat.split()
    hasil = []
    for kata in kata_list:
        hasil.append(kata[::-1])  # Membalik kata
    return ' '.join(hasil)

# Fungsi untuk mengurutkan kata dalam kalimat sesuai indeks urutan
def urutkan_kalimat(kalimat, urutan):
    # Pisah kata dan buat list berdasarkan urutan
    kata_list = kalimat.split()
    hasil = []
    for idx in urutan:
        hasil.append(kata_list[idx - 1])  # Indeks dimulai dari 1
    return ' '.join(hasil)

# Fungsi untuk mengganti huruf vokal dengan simbol
def ganti_vokal(kalimat, opsi):
    # Mapping pengganti vokal
    vokal_kecil = {'a': '4', 'e': '110', 'i': '03', 'o': '00', 'u': '|_|'}
    vokal_besar = {'A': '4', 'E': '11', 'I': 'U', 'O': 'F3', 'U': '00'}
    hasil = ''
    
    for huruf in kalimat:
        if opsi == 1 and huruf in vokal_kecil:
            hasil += vokal_kecil[huruf]
        elif opsi == 2 and huruf in vokal_besar:
            hasil += vokal_besar[huruf]
        else:
            hasil += huruf
    return hasil

# ===========================
# Pengujian semua fungsi
# ===========================

# Uji reverse_per_kata
print("Uji reverse_per_kata:")
print(reverse_per_kata("AKU CINTA KAMU"))  # Output: "UKA ATNIC UMAK"

# Uji urutkan_kalimat
print("\nUji urutkan_kalimat:")
kalimat = "HARI INI SEDANG BELAJAR PYTHON"
urutan = [5, 1, 4, 3, 2]
print(urutkan_kalimat(kalimat, urutan))  # Output: "PYTHON HARI BELAJAR SEDANG INI"

# Uji ganti_vokal
print("\nUji ganti_vokal opsi 1:")
print(ganti_vokal("Aku Cinta Kamu", 1))  # Output: "Ak|_| Cint4 K4m|_|"

print("\nUji ganti_vokal opsi 2:")
print(ganti_vokal("Aku Cinta Kamu", 2))  # Output: "4ku Cinta Kamu"
