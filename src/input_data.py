def input_daftar_nilai():
    nilai_list = []
    print("--- Input Data Nilai Siswa ---")
    print("Ketikkan angka nilai satu per satu. Ketik 'selesai' untuk mengakhiri.")
    
    while True:
        inp = input("Masukkan nilai: ").strip()
        if inp.lower() == 'selesai':
            break
        try:
            val = float(inp)
            if 0 <= val <= 100:
                nilai_list.append(val)
            else:
                print("[Error] Input tidak valid! Harap masukkan angka yang benar.")
        except ValueError:
            print("[Error] Input tidak valid! Harap masukkan angka yang benar.")
            
    return nilai_list