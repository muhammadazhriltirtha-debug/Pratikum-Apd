import os

user_data = [
    ['admin', 'admin123', 'admin'],
    ['azhril', 'azhril123', 'user']
]

laptop_data = [
    [1, 'Asus', 'ROG Zephyrus', 2025],
    [2, 'Acer', 'Predator Helios', 2025]
    ]


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
        found = False
        for user in user_data:
            if user[0] == username and user[1] == password:
                login_status = True
                current_user = username
                current_role = user[2]
                found = True
                break
        if not found:
            input("Login gagal. Tekan Enter untuk kembali...")
        else:
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
                        for laptop in laptop_data:
                            print(f"ID: {laptop[0]}, Merk: {laptop[1]}, Tipe: {laptop[2]}, Tahun: {laptop[3]}")
                    input("\nTekan Enter untuk kembali...")

                elif menu == '2' and current_role == 'admin':
                    merk = input("Masukkan merk laptop: ")
                    tipe = input("Masukkan tipe laptop: ")
                    tahun = input("Masukkan tahun rilis: ")
                    if tahun.isdigit():
                        new_id = 1 if len(laptop_data) == 0 else laptop_data[-1][0] + 1
                        laptop_data.append([new_id, merk, tipe, int(tahun)])
                        input("Data berhasil ditambahkan. Tekan Enter...")
                    else:
                        input("Tahun tidak valid. Tekan Enter...")

                elif menu == '3' and current_role == 'admin':
                    id_update = input("Masukkan ID laptop yang ingin diupdate: ")
                    found = False
                    if id_update.isdigit():
                        for laptop in laptop_data:
                            if laptop[0] == int(id_update):
                                merk = input("Merk baru: ")
                                tipe = input("Tipe baru: ")
                                tahun = input("Tahun baru: ")
                                if tahun.isdigit():
                                    laptop[1] = merk
                                    laptop[2] = tipe
                                    laptop[3] = int(tahun)
                                    input("Data berhasil diupdate. Tekan Enter...")
                                else:
                                    input("Tahun tidak valid. Tekan Enter...")
                                found = True
                                break
                    if not found:
                        input("Data tidak ditemukan. Tekan Enter...")

                elif menu == '4' and current_role == 'admin':
                    id_hapus = input("Masukkan ID laptop yang ingin dihapus: ")
                    found = False
                    if id_hapus.isdigit():
                        for i in range(len(laptop_data)):
                            if laptop_data[i][0] == int(id_hapus):
                                laptop_data.pop(i)
                                input("Data berhasil dihapus. Tekan Enter...")
                                found = True
                                break
                    if not found:
                        input("Data tidak ditemukan. Tekan Enter...")

                elif menu == '5':
                    login_status = False
                    current_user = ''
                    current_role = ''
                    input("Logout berhasil. Tekan Enter...")

                else:
                    input("Menu tidak valid atau akses ditolak. Tekan Enter...")

    elif menu_awal == '2':
        new_user = input("Masukkan username baru: ")
        new_pass = input("Masukkan password: ")
        role = ''
        while role != 'admin' and role != 'user':
            role = input("Masukkan role (admin/user): ").lower()
        already_exists = False
        for user in user_data:
            if user[0] == new_user:
                already_exists = True
                break
        if already_exists:
            input("Username sudah digunakan. Tekan Enter...")
        else:
            user_data.append([new_user, new_pass, role])
            input("Register berhasil! Tekan Enter untuk kembali...")

    elif menu_awal == '3':
        print("Keluar dari program...")
        break

    else:
        input("Pilihan tidak valid. Tekan Enter untuk kembali...")

