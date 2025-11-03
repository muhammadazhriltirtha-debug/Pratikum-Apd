import os
import data
import auth
import crud


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Selamat Datang di Sistem Data Laptop 2025 ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ")

    if menu_awal == '1':
        auth.login()

        while data.login_status:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nLogin sebagai: {data.current_user} ({data.current_role})")
            print("=== Menu Utama ===")
            print("1. Lihat Data Laptop")
            if data.current_role == 'admin':
                print("2. Tambah Data Laptop")
                print("3. Update Data Laptop")
                print("4. Hapus Data Laptop (rekursif)")
                print("5. Logout")

            menu = input("Pilih menu: ")
        

            if menu == '1':
                crud.tampilkan_data()

            elif menu == '2' and data.current_role == 'admin':
                crud.menu_tambah()

            elif menu == '3' and data.current_role == 'admin':
                crud.menu_update()

            elif menu == '4' and data.current_role == 'admin':
                crud.hapus_laptop_rekursif()
                input("Tekan Enter untuk kembali...")

            elif menu == '5':
                auth.logout()

            else:
                input("Menu tidak valid atau akses ditolak. Tekan Enter...")

    elif menu_awal == '2':
        auth.register()

    elif menu_awal == '3':
        print("Keluar dari program...")
        break

    else:
        input("Pilihan tidak valid. Tekan Enter untuk kembali...")