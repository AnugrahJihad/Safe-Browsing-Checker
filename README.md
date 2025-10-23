# 🌐 Web Safety Checker – Powered by Google Safe Browsing API

**Web Safety Checker** adalah aplikasi berbasis **Streamlit** yang memungkinkan pengguna memeriksa keamanan suatu URL menggunakan **Google Safe Browsing API**.  
Aplikasi ini mendeteksi apakah situs web berpotensi mengandung **malware, phishing, atau konten berbahaya lainnya**.

---

## 🚀 Fitur Utama

- 🔍 **Pengecekan Real-time** – Validasi keamanan URL secara instan  
- 🎯 **Deteksi Multi-Ancaman** – Identifikasi malware, phishing, unwanted software, dan aplikasi berbahaya  
- 📊 **Riwayat Pengecekan** – Lihat 10 pengecekan terakhir Anda  
- ⚡ **Interface Intuitif** – Desain sederhana dan mudah digunakan  
- 🧠 **Validasi URL Otomatis** – Otomatis menambahkan `https://` jika diperlukan  
- 🛡️ **Powered by Google** – Menggunakan database Google Safe Browsing yang melindungi miliaran perangkat

---

## 🎬 Demo

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/4c50cb46-a4fb-4e0a-b683-0d2370bc62a7" />

**Live Demo:** [https://safe-browse-lab.streamlit.app/](https://safe-browse-lab.streamlit.app/)

---

## 🧩 Struktur Proyek

📁 web-checker/
      ├── app.py # Aplikasi utama
      ├── requirements.txt # Dependencies
      ├── README.md # Dokumentasi (file ini)
      ├── .streamlit/
      │ └── secrets.toml # API keys (jangan commit!)
      └── .gitignore # File yang diabaikan Git

---

## ⚙️ Quick Installation

### 🛠️ Alat dan Bahan
- Python 3.8 atau lebih tinggi  
- Google Safe Browsing API Key ([Dapatkan di sini](https://developers.google.com/safe-browsing/v4/get-started))

---

### 💻 Instalasi Lokal

1. **Clone repositori**
   ```bash
   git clone https://github.com/AnugrahJihad/Safe-Browsing-Checker
   cd Safe-Browsing-Checker

2. Install dependencies
pip install -r requirements.txt

3. Setup API Key: Buat file .streamlit/secrets.toml di root project:
[api]
google_safe_browsing = "YOUR_API_KEY_HERE"

pip install -r requirements.txt

4. Jalankan aplikasi:
streamlit run app.py

---

## ☁️ Deploy ke Streamlit Cloud

Langkah-langkah:
### 1. Fork/Push repository ini ke GitHub
### 2. Buka Streamlit Cloud (https://share.streamlit.io/)
### 3. Klik "New app" dan pilih repository Anda
### 4. Setup Secrets:
      - Pergi ke Settings → Secrets
      - Tambahkan secrets berikut:
        [api]
        google_safe_browsing = "YOUR_API_KEY_HERE"
### 5. Klik Deploy, dan aplikasi siap digunakan publik

---

## 🔧 Teknologi yang Digunakan

- Streamlit - Framework web app Python
- Google Safe Browsing API v4 - Database ancaman online
- Requests - HTTP library untuk Python

---

## ⚠️ Disclaimer

Aplikasi ini menggunakan Google Safe Browsing API untuk mendeteksi ancaman. Namun, tidak ada sistem yang 100% sempurna. Selalu gunakan pertimbangan pribadi dan kehati-hatian saat mengunjungi situs web yang tidak dikenal.

---

## 🧑‍💻 Kontributor

Dibuat dengan ❤️ oleh Anugrah Jihad
🔗 GitHub: https://github.com/AnugrahJihad
