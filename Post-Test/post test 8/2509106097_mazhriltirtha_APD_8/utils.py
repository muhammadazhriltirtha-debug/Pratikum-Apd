import datetime

def tampilkan_waktu():
    """Menampilkan waktu saat ini (bonus library datetime)."""
    now = datetime.datetime.now()
    print(f"\n Waktu sekarang: {now.strftime('%A, %d %B %Y %H:%M:%S')}")
