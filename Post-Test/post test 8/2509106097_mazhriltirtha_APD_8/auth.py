import data

def login():
    """Fungsi login dengan error handling."""
    global login_status, current_user, current_role
    username = input("Username: ")
    password = input("Password: ")


    if username in data.user_data and data.user_data[username]['password'] == password:
        data.login_status = True
        data.current_user = username
        data.current_role = data.user_data[username]['role']
    else:
        input("Login gagal! Tekan Enter untuk kembali...")

def register():
    """Fungsi register dengan error handling."""
    try:
        new_user = input("Masukkan username baru: ")
        if new_user in data.user_data:
            input("Username sudah digunakan. Tekan Enter...")
            return
        new_pass = input("Masukkan password: ")
        role = ''
        while role not in ['admin', 'user']:
            role = input("Masukkan role (admin/user): ").lower()
        data.user_data[new_user] = {'password': new_pass, 'role': role}
        input("Register berhasil! Tekan Enter untuk kembali...")
    except Exception as e:
        print("Terjadi kesalahan:", e)

def logout():
    """Prosedur untuk logout."""
    global login_status, current_user, current_role
    data.login_status = False
    data.current_user = ''
    data.current_role = ''
    input("Logout berhasil! Tekan Enter...")