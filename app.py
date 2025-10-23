import streamlit as st
import requests
from urllib.parse import urlparse
from datetime import datetime

# =============================
# Konfigurasi dasar Streamlit
# =============================
st.set_page_config(
    page_title="🛡️ Web Safety Checker",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Google Safe Browsing URL Checker")
st.markdown("Periksa apakah sebuah situs aman menggunakan **Google Safe Browsing API**.")
st.info("💡 **Tips:** Masukkan domain (misal: `youtube.com`) atau URL lengkap (`https://youtube.com`)")

# =============================
# Ambil API key secara aman
# =============================
api_key = st.secrets.get("api", {}).get("google_safe_browsing")

# =============================
# Fungsi validasi URL
# =============================
def validate_and_format_url(url):
    """Validasi dan format URL dengan benar"""
    url = url.strip()
    
    # Tambahkan https:// jika tidak ada protokol
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Validasi struktur URL
    try:
        parsed = urlparse(url)
        if not parsed.netloc:
            return None
        return url
    except Exception:
        return None

# =============================
# Fungsi cek keamanan URL
# =============================
def check_url_safety(url, api_key):
    """Cek keamanan URL menggunakan Google Safe Browsing API"""
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
    payload = {
        "client": {
            "clientId": "streamlit-app",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": [
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE",
                "POTENTIALLY_HARMFUL_APPLICATION"
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }
    
    try:
        response = requests.post(api_url, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "⏱️ Request timeout. Silakan coba lagi."}
    except requests.exceptions.HTTPError as e:
        if response.status_code == 400:
            return {"error": "❌ API key tidak valid atau format request salah."}
        elif response.status_code == 429:
            return {"error": "⚠️ Terlalu banyak request. Coba lagi nanti."}
        return {"error": f"❌ HTTP Error {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"🌐 Network error: Periksa koneksi internet Anda."}
    except Exception as e:
        return {"error": f"❌ Unexpected error: {str(e)}"}

# =============================
# Inisialisasi session state untuk history
# =============================
if 'history' not in st.session_state:
    st.session_state.history = []

# =============================
# Input utama pengguna
# =============================
st.subheader("🔗 Masukkan URL yang ingin diperiksa:")

# Gunakan form untuk better UX (Enter untuk submit)
with st.form("url_form"):
    url = st.text_input(
        "URL",
        placeholder="Contoh: youtube.com atau https://google.com",
        label_visibility="collapsed"
    )
    submitted = st.form_submit_button("🔍 Periksa Keamanan", use_container_width=True)

if submitted:
    if not api_key:
        st.error("❌ API key tidak ditemukan! Hubungi administrator.")
    elif not url:
        st.warning("⚠️ Silakan masukkan URL terlebih dahulu.")
    else:
        # Validasi dan format URL
        formatted_url = validate_and_format_url(url)
        
        if not formatted_url:
            st.error("❌ Format URL tidak valid. Contoh yang benar: `google.com` atau `https://google.com`")
        else:
            with st.spinner(f"🔍 Memeriksa keamanan `{formatted_url}`..."):
                result = check_url_safety(formatted_url, api_key)
            
            # Tampilkan hasil
            if "error" in result:
                st.error(result["error"])
            elif "matches" in result and result["matches"]:
                st.error("🚨 **URL INI TIDAK AMAN!**")
                st.warning(f"Google Safe Browsing mendeteksi ancaman pada: `{formatted_url}`")
                
                # Tampilkan detail ancaman
                for idx, match in enumerate(result["matches"], 1):
                    with st.expander(f"⚠️ Ancaman #{idx}: {match.get('threatType', 'Unknown')}", expanded=True):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write("**Jenis Ancaman:**")
                            st.write(f"`{match.get('threatType', 'N/A')}`")
                        with col2:
                            st.write("**Platform:**")
                            st.write(f"`{match.get('platformType', 'N/A')}`")
                        
                        st.write("**Kategori:**")
                        st.write(f"`{match.get('threatEntryType', 'N/A')}`")
                
                # Simpan ke history
                st.session_state.history.append({
                    "url": formatted_url,
                    "safe": False,
                    "threat_count": len(result["matches"]),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            else:
                st.success("✅ **URL ini AMAN!**")
                st.info(f"`{formatted_url}` tidak ditemukan dalam database ancaman Google Safe Browsing.")
                
                # Simpan ke history
                st.session_state.history.append({
                    "url": formatted_url,
                    "safe": True,
                    "threat_count": 0,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

# =============================
# Sidebar: Riwayat dan Info
# =============================
with st.sidebar:
    st.header("ℹ️ Informasi")
    st.markdown("""
    **Google Safe Browsing** melindungi miliaran perangkat setiap hari dengan:
    - 🦠 Deteksi malware
    - 🎣 Identifikasi phishing
    - ⚠️ Peringatan software berbahaya
    """)
    
    st.divider()
    
    # Tampilkan history
    if st.session_state.history:
        st.header("📋 Riwayat Pengecekan")
        
        # Tombol clear history
        if st.button("🗑️ Hapus Riwayat", use_container_width=True):
            st.session_state.history = []
            st.rerun()
        
        # Tampilkan 10 pengecekan terakhir
        for item in reversed(st.session_state.history[-10:]):
            status_icon = "✅" if item["safe"] else "🚨"
            status_text = "Aman" if item["safe"] else f"Tidak Aman ({item['threat_count']} ancaman)"
            
            with st.container():
                st.markdown(f"""
                **{status_icon} {item['url'][:35]}{"..." if len(item['url']) > 35 else ""}**  
                <small>Status: {status_text}</small>  
                <small style='color: gray;'>{item['timestamp']}</small>
                """, unsafe_allow_html=True)
                st.divider()

# =============================
# Footer
# =============================
st.markdown("---")
st.caption("Dibuat oleh Anugrah Jihad dengan ❤️ menggunakan Streamlit + Google Safe Browsing API.")
st.caption("⚠️ **Disclaimer:** Hasil pengecekan berdasarkan database Google Safe Browsing. Selalu gunakan pertimbangan pribadi saat mengunjungi situs web.")
