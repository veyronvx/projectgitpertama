def daftar_matkul():
    matkul = ["Matematika", "Fisika", "Kimia", "Biologi", "Sejarah"]
    print("Daftar Mata Kuliah:")
    for i, m in enumerate(matkul, start=1):
        print(f"{i}. {m}")

daftar_matkul()