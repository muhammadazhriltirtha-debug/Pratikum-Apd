import os

user_data = {
    'admin': {'password': '097', 'role': 'admin'},
    'azhril': {'password': '97', 'role': 'user'}
}

laptop_data = {
    1: {'merk': 'Asus', 'tipe': 'ROG Zephyrus', 'tahun': 2025},
    2: {'merk': 'Acer', 'tipe': 'Predator Helios', 'tahun': 2025}
}

login_status = False
current_user = ''
current_role = ''

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Selamat Datang di Sistem Data Laptop 2025 ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ")

    if menu_awal == '1':
        username = input("Username: ")
        password = input("Password: ")

        if username in user_data and user_data[username]['password'] == password:
            login_status = True
            current_user = username
            current_role = user_data[username]['role']
        else:
            input("Login gagal! Tekan Enter untuk kembali...")
            continue

        while login_status:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nLogin sebagai: {current_user} ({current_role})")
            print("=== Menu Utama ===")
            print("1. Lihat Data Laptop")
            if current_role == 'admin':
                print("2. Tambah Data Laptop")
                print("3. Update Data Laptop")
                print("4. Hapus Data Laptop")
            print("5. Logout")

            menu = input("Pilih menu: ")

            if menu == '1':
                print("\n=== Data Laptop ===")
                if len(laptop_data) == 0:
                    print("Belum ada data.")
                else:
                    for id_laptop, data in laptop_data.items():
                        print(f"ID: {id_laptop}, Merk: {data['merk']}, "
                              f"Tipe: {data['tipe']}, Tahun: {data['tahun']}")
                input("\nTekan Enter untuk kembali...")

            elif menu == '2' and current_role == 'admin':
                merk = input("Masukkan merk laptop: ")
                tipe = input("Masukkan tipe laptop: ")
                tahun = input("Masukkan tahun rilis: ")

                if tahun.isdigit():
                    new_id = max(laptop_data.keys()) + 1 if laptop_data else 1
                    laptop_data[new_id] = {'merk': merk, 'tipe': tipe, 'tahun': int(tahun)}
                    input("Data berhasil ditambahkan! Tekan Enter...")
                else:
                    input("Tahun tidak valid. Tekan Enter...")

            elif menu == '3' and current_role == 'admin':
                id_update = input("Masukkan ID laptop yang ingin diupdate: ")

                if id_update.isdigit() and int(id_update) in laptop_data:
                    merk = input("Merk baru: ")
                    tipe = input("Tipe baru: ")
                    tahun = input("Tahun baru: ")
                    if tahun.isdigit():
                        laptop_data[int(id_update)] = {
                            'merk': merk, 'tipe': tipe, 'tahun': int(tahun)
                        }
                        input("Data berhasil diupdate! Tekan Enter...")
                    else:
                        input("Tahun tidak valid. Tekan Enter...")
                else:
                    input("Data tidak ditemukan. Tekan Enter...")
                          
            elif menu == '4' and current_role == 'admin':
                id_hapus = input("Masukkan ID laptop yang ingin dihapus: ")

                if id_hapus.isdigit() and int(id_hapus) in laptop_data:
                    del laptop_data[int(id_hapus)]
                    input("Data berhasil dihapus! Tekan Enter...")
                else:
                    input("Data tidak ditemukan. Tekan Enter...")

            elif menu == '5':
                login_status = False
                current_user = ''
                current_role = ''
                input("Logout berhasil! Tekan Enter...")

            else:
                input("Menu tidak valid atau akses ditolak. Tekan Enter...")

    elif menu_awal == '2':
        new_user = input("Masukkan username baru: ")

        if new_user in user_data:
            input("Username sudah digunakan. Tekan Enter...")
            continue

        new_pass = input("Masukkan password: ")
        role = ''
        while role not in ['admin', 'user']:
            role = input("Masukkan role (admin/user): ").lower()

        user_data[new_user] = {'password': new_pass, 'role': role}
        input("Register berhasil! Tekan Enter untuk kembali...")


    elif menu_awal == '3':
        print("Keluar dari program...")
        break

    else:
        input("Pilihan tidak valid. Tekan Enter untuk kembali...")
