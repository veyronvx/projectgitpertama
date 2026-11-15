def daftar_matkul():
    matkul = ["Jhoan","Pablo","Montoya","Santiago","Ramon"]
    print("Daftar Mata Kuliah:")
    for i, m in enumerate(matkul, start=1):
        print(f"{i}. {m}")

daftar_matkul()