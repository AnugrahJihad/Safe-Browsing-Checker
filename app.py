import streamlit as st
import requests
from urllib.parse import urlparse

# =============================
# Konfigurasi dasar Streamlit
# =============================
st.set_page_config(page_title="🛡️ Web Safety Checker", layout="centered")

st.title("🛡️ Google Safe Browsing URL Checker")
st.markdown("Periksa apakah sebuah situs aman menggunakan **Google Safe Browsing API**.")

# =============================
# Ambil API key secara aman
# =============================
api_key = st.secrets.get("api", {}).get("google_safe_browsing")

# =============================
# Fungsi cek keamanan URL
# =============================
def check_url_safety(url, api_key):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"

    payload = {
        "client": {"clientId": "streamlit-app", "clientVersion": "1.0"},
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

    response = requests.post(api_url, json=payload)
    if response.status_code != 200:
        return {"error": f"Error: {response.status_code} - {response.text}"}

    return response.json()

# =============================
# Input utama pengguna
# =============================
st.subheader("🔗 Masukkan URL yang ingin diperiksa:")
url = st.text_input("Contoh: youtube.com")

if st.button("Periksa Keamanan"):
    if not api_key:
        st.error("❌ Tidak ada API key! Masukkan di sidebar atau simpan di secrets.")
    elif not url:
        st.warning("⚠️ Silakan masukkan URL terlebih dahulu.")
    else:
        with st.spinner("🔍 Memeriksa URL..."):
            result = check_url_safety(url, api_key)

        if "matches" in result and result["matches"]:
            st.error("🚨 URL ini TIDAK AMAN!")
            for match in result["matches"]:
                st.write(f"- **Ancaman:** {match['threatType']}")
                st.write(f"- **Platform:** {match['platformType']}")
                st.write(f"- **Kategori:** {match['threatEntryType']}")
        elif "error" in result:
            st.error(result["error"])
        else:
            st.success("✅ URL ini aman menurut Google Safe Browsing.")

st.markdown("---")
st.caption("Dibuat dengan ❤️ menggunakan Streamlit + Google Safe Browsing API.")




