
import streamlit as st

# Konfigurasi halaman HARUS paling atas
st.set_page_config(
    page_title="LapStore Login",
    page_icon="💻",
    layout="centered"
)

# Tema Pink Lembut LapStore
st.markdown("""
    <style>
        /* Latar belakang utama */
        .stApp {
            background: linear-gradient(
                135deg,
                #FFF1F7 0%,
                #FCE7F3 50%,
                #FDF2F8 100%
            );
            color: #831843;
        }

        /* Area konten */
        [data-testid="stMain"] {
            background: transparent;
        }

        /* Judul dan heading */
        h1, h2, h3, h4, h5, h6 {
            color: #9D174D !important;
        }

        /* Teks umum */
        .stApp p,
        .stApp label,
        .stApp .stMarkdown {
            color: #831843;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #FBCFE8 0%,
                #FCE7F3 100%
            );
            border-right: 2px solid #F9A8D4;
        }

        [data-testid="stSidebar"] * {
            color: #831843;
        }

        /* Input username, password, dan teks */
        .stTextInput input,
        .stNumberInput input,
        .stTextArea textarea {
            background-color: #FFFFFF !important;
            color: #831843 !important;
            border: 1px solid #F9A8D4 !important;
            border-radius: 10px !important;
        }

        /* Efek fokus pada input */
        .stTextInput input:focus,
        .stNumberInput input:focus,
        .stTextArea textarea:focus {
            border: 2px solid #DB2777 !important;
            box-shadow: 0 0 0 2px #FCE7F3 !important;
        }

        /* Tombol utama dan unduh */
        .stButton > button,
        .stDownloadButton > button {
            background-color: #DB2777 !important;
            color: #FFFFFF !important;
            border: 1px solid #BE185D !important;
            border-radius: 10px !important;
            padding: 8px 18px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out;
        }

        /* Hover tombol */
        .stButton > button:hover,
        .stDownloadButton > button:hover {
            background-color: #BE185D !important;
            color: #FFFFFF !important;
            border-color: #9D174D !important;
        }

        /* Tombol saat ditekan */
        .stButton > button:active,
        .stDownloadButton > button:active {
            background-color: #9D174D !important;
        }

        /* Dropdown menu */
        div[data-baseweb="select"] {
            background-color: #FFFFFF;
            border-radius: 8px;
        }

        div[data-baseweb="popover"],
        div[data-baseweb="menu"] {
            background-color: #FFFFFF;
        }

        /* Notifikasi sukses */
        [data-testid="stAlert"][kind="success"] {
            background-color: #FCE7F3;
            border: 1px solid #F9A8D4;
            border-radius: 10px;
        }

        /* Notifikasi error */
        [data-testid="stAlert"][kind="error"] {
            background-color: #FFF1F2;
            border: 1px solid #FDA4AF;
            border-radius: 10px;
        }

        /* Notifikasi peringatan */
        [data-testid="stAlert"][kind="warning"] {
            background-color: #FFF7ED;
            border: 1px solid #FDBA74;
            border-radius: 10px;
        }

        /* Notifikasi informasi */
        [data-testid="stAlert"][kind="info"] {
            background-color: #FDF2F8;
            border: 1px solid #F9A8D4;
            border-radius: 10px;
        }

        /* Tabel dan dataframe */
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            border: 1px solid #F9A8D4;
            border-radius: 10px;
            overflow: hidden;
        }

        /* Container dengan border */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-color: #F9A8D4;
            border-radius: 12px;
        }

        /* Garis pemisah */
        hr {
            border-color: #F9A8D4 !important;
        }

        /* File uploader */
        [data-testid="stFileUploader"] {
            background-color: #FFF7FB;
            border: 1px dashed #F472B6;
            border-radius: 12px;
            padding: 10px;
        }

        /* Progress bar */
        [data-testid="stProgress"] > div > div {
            background-color: #DB2777;
        }

        /* Link */
        .stApp a {
            color: #BE185D !important;
        }

        /* Placeholder input */
        input::placeholder,
        textarea::placeholder {
            color: #BE8BA6 !important;
        }

        /* Footer Streamlit */
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)


# Import modul lainnya
from auth import login_user, register_user
from database import (
    create_user_table,
    create_tables,
    alter_table_add_kategori
)
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
