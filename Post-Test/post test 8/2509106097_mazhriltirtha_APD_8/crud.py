from prettytable import PrettyTable
from data import laptop_data

def tampilkan_data():
    """Menampilkan data dengan PrettyTable."""
    print("\n=== Data Laptop ===")
    if not laptop_data:
        print("Belum ada data.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Merk", "Tipe", "Tahun"]
        for id_laptop, data in laptop_data.items():
            tabel.add_row([id_laptop, data['merk'], data['tipe'], data['tahun']])
        print(tabel)
    input("\nTekan Enter untuk kembali...")

def tambah_laptop(merk, tipe, tahun):
    """Tambah data laptop baru."""
    global laptop_data
    new_id = max(laptop_data.keys()) + 1 if laptop_data else 1
    laptop_data[new_id] = {'merk': merk, 'tipe': tipe, 'tahun': tahun}
    print("Data berhasil ditambahkan!")

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

def update_laptop(id_update, merk, tipe, tahun):
    """Update data laptop berdasarkan ID."""
    if id_update in laptop_data:
        laptop_data[id_update] = {'merk': merk, 'tipe': tipe, 'tahun': tahun}
        print("Data berhasil diupdate!")
    else:
        print("ID tidak ditemukan.")

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
