# Meminta input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Menyimpan data ke file
with open("nilai_mahasiswa.txt", "w") as file:
    for i in range(jumlah):
        print(f"\nMahasiswa ke-{i+1}")
        nama = input("Nama          : ")
        tugas = float(input("Nilai Tugas   : "))
        uts = float(input("Nilai UTS     : "))
        uas = float(input("Nilai UAS     : "))

        # Simpan dengan format CSV
        file.write(f"{nama},{tugas},{uts},{uas}\n")

# Membaca kembali file dan menampilkan rekap
print("\n=== REKAP NILAI MAHASISWA ===")
print("Nama\tTugas\tUTS\tUAS\tRata2")

with open("nilai_mahasiswa.txt", "r") as file:
    for baris in file:
        data = baris.strip().split(",")
        nama = data[0]
        tugas = float(data[1])
        uts = float(data[2])
        uas = float(data[3])

        rata2 = (tugas + uts + uas) / 3
        print(f"{nama}\t{tugas:.0f}\t{uts:.0f}\t{uas:.0f}\t{rata2:.2f}")