

print("=== SELAMAT DATANG DI BIOSKOP XX0.1 ===")

username_benar = "Azhril"   
password_benar = "097"  
percobaan = 0
maks_percobaan = 5
login_berhasil = False

while percobaan < maks_percobaan:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == username_benar and password == password_benar:
        print("\nLogin berhasil! Selamat datang,", username)
        login_berhasil = True
        break
    else:
        percobaan += 1
        print("Login gagal! Percobaan ke-", percobaan)
        if percobaan == maks_percobaan:
            print("Login gagal 5 kali. Program berhenti.")
            exit()


if login_berhasil:
    while True:
        print("\n=== MENU PEMBELIAN TIKET BIOSKOP XX0.1 ===")
        print("1. Tiket Reguler  - Rp 50.000")
        print("2. Tiket VIP      - Rp 100.000")
        print("3. Tiket VVIP     - Rp 150.000")
        print("4. Keluar")

        pilihan = input("Pilih jenis tiket (1-4): ")

        if pilihan == "1":
            jenis_tiket = "Reguler"
            harga_tiket = 50000
        elif pilihan == "2":
            jenis_tiket = "VIP"
            harga_tiket = 100000
        elif pilihan == "3":
            jenis_tiket = "VVIP"
            harga_tiket = 150000
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan Bioskop XX0.1!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")
            continue

        jumlah_tiket = input("Masukkan jumlah tiket yang ingin dibeli: ")

        if jumlah_tiket.isdigit():
            jumlah_tiket = int(jumlah_tiket)
            total_bayar = 0

    
            for i in range(jumlah_tiket):
                total_bayar += harga_tiket

            
            potongan = 0
            bonus = ""

            if total_bayar >= 300000:
                potongan = total_bayar * 0.12
            elif total_bayar >= 200000 and total_bayar < 300000:
                potongan = total_bayar * 0.08
            elif total_bayar >= 150000 and total_bayar < 200000:
                bonus = "Poster Film Eksklusif"

            total_akhir = total_bayar - potongan

            
            print("\n=== RINCIAN PEMBELIAN ===")
            print(f"Jenis Tiket   : {jenis_tiket}")
            print(f"Jumlah Tiket  : {jumlah_tiket}")
            print(f"Total Bayar   : Rp {total_bayar:,}")
            if potongan > 0:
                print(f"Potongan      : Rp {int(potongan):,}")
            print(f"Total Akhir   : Rp {int(total_akhir):,}")
            if bonus != "":
                print(f"Bonus         : {bonus}")
            print("============================")

        else:
            print("Input jumlah tiket harus berupa angka!")

