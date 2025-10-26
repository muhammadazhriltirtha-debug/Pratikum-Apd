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

def tampilkan_data():
    """Menampilkan semua data laptop (prosedur tanpa return)."""
    print("\n=== Data Laptop ===")
    if len(laptop_data) == 0:
        print("Belum ada data.")
    else:
        for id_laptop, data in laptop_data.items():
            print(f"ID: {id_laptop}, Merk: {data['merk']}, "
                  f"Tipe: {data['tipe']}, Tahun: {data['tahun']}")
    input("\nTekan Enter untuk kembali...")


def logout():
    """Prosedur untuk logout."""
    global login_status, current_user, current_role
    login_status = False
    current_user = ''
    current_role = ''
    input("Logout berhasil! Tekan Enter...")

def tambah_laptop(merk, tipe, tahun):
    """Fungsi menambah data laptop baru (dengan parameter)."""
    global laptop_data
    new_id = max(laptop_data.keys()) + 1 if laptop_data else 1
    laptop_data[new_id] = {'merk': merk, 'tipe': tipe, 'tahun': tahun}
    return True


def update_laptop(id_update, merk, tipe, tahun):
    """Fungsi update data laptop (dengan parameter)."""
    if id_update in laptop_data:
        laptop_data[id_update] = {'merk': merk, 'tipe': tipe, 'tahun': tahun}
        return True
    return False

def menu_tambah():
    """Fungsi tanpa parameter untuk tambah laptop dengan input pengguna."""
    try:
        merk = input("Masukkan merk laptop: ")
        tipe = input("Masukkan tipe laptop: ")
        tahun = int(input("Masukkan tahun rilis: "))
        if tambah_laptop(merk, tipe, tahun):
            input("Data berhasil ditambahkan! Tekan Enter...")
    except ValueError:
        input("Tahun harus berupa angka! Tekan Enter...")


def menu_update():
    """Fungsi tanpa parameter untuk update data laptop."""
    try:
        id_update = int(input("Masukkan ID laptop yang ingin diupdate: "))
        merk = input("Merk baru: ")
        tipe = input("Tipe baru: ")
        tahun = int(input("Tahun baru: "))
        if update_laptop(id_update, merk, tipe, tahun):
            input("Data berhasil diupdate! Tekan Enter...")
        else:
            input("Data tidak ditemukan! Tekan Enter...")
    except ValueError:
        input("Input tidak valid! Tekan Enter...")

def hapus_laptop_rekursif():
    """Fungsi rekursif untuk menghapus beberapa data laptop."""
    try:
        id_hapus = int(input("Masukkan ID laptop yang ingin dihapus (0 untuk berhenti): "))
        if id_hapus == 0:
            return
        elif id_hapus in laptop_data:
            del laptop_data[id_hapus]
            print("Data berhasil dihapus!")
        else:
            print("ID tidak ditemukan.")
        hapus_laptop_rekursif()
    except ValueError:
        print("Input harus angka!")
        hapus_laptop_rekursif()

def login():
    """Fungsi login dengan error handling."""
    global login_status, current_user, current_role
    username = input("Username: ")
    password = input("Password: ")

    if username in user_data and user_data[username]['password'] == password:
        login_status = True
        current_user = username
        current_role = user_data[username]['role']
    else:
        input("Login gagal! Tekan Enter untuk kembali...")


def register():
    """Fungsi register dengan error handling."""
    try:
        new_user = input("Masukkan username baru: ")
        if new_user in user_data:
            input("Username sudah digunakan. Tekan Enter...")
            return
        new_pass = input("Masukkan password: ")
        role = ''
        while role not in ['admin', 'user']:
            role = input("Masukkan role (admin/user): ").lower()
        user_data[new_user] = {'password': new_pass, 'role': role}
        input("Register berhasil! Tekan Enter untuk kembali...")
    except Exception as e:
        print("Terjadi kesalahan:", e)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Selamat Datang di Sistem Data Laptop 2025 ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ")

    if menu_awal == '1':
        login()

        while login_status:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nLogin sebagai: {current_user} ({current_role})")
            print("=== Menu Utama ===")
            print("1. Lihat Data Laptop")
            if current_role == 'admin':
                print("2. Tambah Data Laptop")
                print("3. Update Data Laptop")
                print("4. Hapus Data Laptop (rekursif)")
            print("5. Logout")

            menu = input("Pilih menu: ")

            if menu == '1':
                tampilkan_data()

            elif menu == '2' and current_role == 'admin':
                menu_tambah()

            elif menu == '3' and current_role == 'admin':
                menu_update()

            elif menu == '4' and current_role == 'admin':
                hapus_laptop_rekursif()
                input("Tekan Enter untuk kembali...")

            elif menu == '5':
                logout()

            else:
                input("Menu tidak valid atau akses ditolak. Tekan Enter...")

    elif menu_awal == '2':
        register()

    elif menu_awal == '3':
        print("Keluar dari program...")
        break

    else:
        input("Pilihan tidak valid. Tekan Enter untuk kembali...")