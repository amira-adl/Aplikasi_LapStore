import streamlit as st

# Konfigurasi halaman HARUS paling atas
st.set_page_config(page_title="LapStore Login", page_icon="💻", layout="centered")

# Tambahan CSS agar tampilan berwarna
st.markdown("""
    <style>
        /* Warna latar belakang utama */
        .stApp {
            background-color: #f1f3f6;
            background-image: linear-gradient(135deg, #f1f3f6 0%, #e0e7ff 100%);
        }

        /* Judul utama */
        .css-10trblm {
            color: #2c3e50;
        }

        /* Sidebar */
        .css-1d391kg {
            background-color: #eef1f8;
            border-right: 2px solid #ccc;
        }

        /* Widget box */
        .stTextInput > div > div > input {
            background-color: #ffffff;
            border: 1px solid #ccc;
            color: #333333;
        }

        .stButton>button {
            background-color: #4a90e2;
            color: white;
            border: None;
            border-radius: 5px;
            padding: 8px 16px;
        }

        .stButton>button:hover {
            background-color: #357ABD;
        }

        /* Success box */
        .stAlert[data-testid="stAlert-success"] {
            background-color: #d4edda;
            border-color: #c3e6cb;
            color: #155724;
        }

        /* Error box */
        .stAlert[data-testid="stAlert-error"] {
            background-color: #f8d7da;
            border-color: #f5c6cb;
            color: #721c24;
        }

        /* Warning box */
        .stAlert[data-testid="stAlert-warning"] {
            background-color: #fff3cd;
            border-color: #ffeeba;
            color: #856404;
        }

        /* Subheader warna */
        h2 {
            color: #1a237e;
        }
    </style>
""", unsafe_allow_html=True)

# Import modul lainnya
from auth import login_user, register_user
from database import create_user_table, create_tables, alter_table_add_kategori
from dashboard import show_dashboard
from kelola import show_kelola_produk
from transaksi import show_transaksi
from enkripsi import run_enkripsi_page
from dekripsi import run_dekripsi_csv_page

# Inisialisasi database
create_user_table()
create_tables()
alter_table_add_kategori()

# Session user
if "user" not in st.session_state:
    st.session_state["user"] = None

# Halaman setelah login
if st.session_state["user"]:
    st.sidebar.success(f"👤 {st.session_state['user']}")
    menu = st.sidebar.selectbox(
        "Menu",
        [
            "📊 Statistik Penjualan",
            "🛒 Kelola Produk",
            "🧾 Riwayat Transaksi",
            "🔐 Enkripsi Data",
            "🔓 Dekripsi Data",
            "🚪 Logout"
        ]
    )

    if menu == "📊 Statistik Penjualan":
        show_dashboard(st)
    elif menu == "🛒 Kelola Produk":
        show_kelola_produk()
    elif menu == "🧾 Riwayat Transaksi":
        show_transaksi()
    elif menu == "🔐 Enkripsi Data":
        run_enkripsi_page()
    elif menu == "🔓 Dekripsi Data":
        run_dekripsi_csv_page()
    elif menu == "🚪 Logout":
        st.session_state["user"] = None
        st.rerun()

# Halaman login dan daftar
else:
    st.title("💻 LapStore – Platform Produk Teknologi")
    menu = st.sidebar.selectbox("Menu", ["Login", "Daftar"])

    if menu == "Login":
        st.subheader("Masuk ke Platform")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(username, password):
                st.success(f"Selamat datang, {username}!")
                st.session_state["user"] = username
                st.rerun()
            else:
                st.error("Username atau password salah.")

    elif menu == "Daftar":
        st.subheader("Buat Akun Baru")
        username = st.text_input("Buat Username")
        password = st.text_input("Buat Password", type="password")
        confirm = st.text_input("Ulangi Password", type="password")

        if st.button("Daftar"):
            if password != confirm:
                st.warning("Password tidak cocok!")
            elif register_user(username, password):
                st.success("Registrasi berhasil. Silakan login.")
            else:
                st.error("Username sudah terdaftar.")
