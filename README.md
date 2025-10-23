# 🌐 Web Checker – Powered by Google Safe Browsing API

Web Checker adalah aplikasi berbasis **Streamlit** yang memungkinkan pengguna untuk memeriksa keamanan suatu URL menggunakan **Google Safe Browsing API**.  
Aplikasi ini dapat mendeteksi apakah situs web berpotensi mengandung **malware, phishing, atau konten berbahaya lainnya**.

---

## 🚀 Fitur Utama
✅ Cek keamanan URL secara real-time.  
✅ Menggunakan Google Safe Browsing API.  
✅ Antarmuka sederhana dan ringan dengan Streamlit.  
✅ API Key aman melalui fitur *Streamlit Secrets* (tidak terlihat publik).  

---

## 🧩 Struktur Proyek

📁 web-checker/
│
├── app.py # File utama Streamlit
├── requirements.txt # Daftar dependency
└── README.md # Dokumentasi proyek

---

⚙️ Instalasi Lokal

Kamu bisa menjalankan aplikasi ini secara lokal sebelum di-deploy.

# 1. Clone repositori
git clone https://github.com/username/web-checker.git
cd web-checker

# 2. (Opsional) Buat virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Install dependensi
pip install -r requirements.txt

# 4. Jalankan Streamlit
streamlit run app.py

---

☁️ Deploy ke Streamlit Cloud

Upload proyek ini ke GitHub.

Masuk ke https://share.streamlit.io
.

Hubungkan akun GitHub dan pilih repo web-checker.

Tambahkan API Key kamu melalui menu “Settings → Secrets” di dashboard Streamlit.

Klik Deploy, dan aplikasi siap digunakan publik 🎉

---

🧑‍💻 Kontributor

Dibuat dengan ❤️ oleh Anugrah Jihad
🔗 GitHub: https://github.com/AnugrahJihad
