def daftar_matkul():
    matkul = ["coc", "pbo", "basis data", "web"]
    print("Daftar Mata Kuliah:")
    for i, m in enumerate(matkul, start=1):
        print(f"{i}. {m}")

daftar_matkul()

print("\nDaftar Mata Kuliah dengan Indeks:")