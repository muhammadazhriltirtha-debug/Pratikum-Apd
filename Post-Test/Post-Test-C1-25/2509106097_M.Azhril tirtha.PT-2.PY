# Input dari user
nama = input("Masukkan nama lengkap: ")
nim = input("Masukkan NIM: ")
harga_laptop = float(input("Masukkan harga laptop (Rp): "))

# Data diskon tiap merek
merek = ["Acer", "Asus", "Lenovo"]
diskon_persen = [5, 7, 10]

# Menghitung harga setelah diskon untuk tiap merek
diskon_rupiah = [harga_laptop * (persen / 100) for persen in diskon_persen]
harga_setelah_diskon = [harga_laptop - diskon for diskon in diskon_rupiah]

# Output
print("\n" + "="*60)
print(f"{nama} dengan NIM {nim} ingin membeli laptop seharga Rp {harga_laptop:,.0f}")
print("="*60)
print(f"{'Merek':<10} {'Diskon (%)':<12} {'Harga Akhir (Rp)':>20}")
print("-"*60)

for i in range(len(merek)):
    print(f"{merek[i]:<10} {diskon_persen[i]:<12} Rp {harga_setelah_diskon[i]:>17,.0f}")

print("="*60)
