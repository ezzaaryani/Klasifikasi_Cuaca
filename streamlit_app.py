import streamlit as st
import pandas as pd
import joblib

import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()
foto_profile = img_to_base64("foto.png")
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

email_icon = img_to_base64("Email.png")
github_icon = img_to_base64("GitHub.png")
ig_icon = img_to_base64("IG.png")

st.set_page_config(
    page_title="Prediksi Kondisi Cuaca",
    page_icon="⛅",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_data
def load_data():
    return pd.read_csv("dataset_cuaca.csv")

@st.cache_resource
def load_model():
    return joblib.load("model_klasifikasi_cuaca.joblib")

df   = load_data()
model = load_model()

st.markdown("""
<style>
/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
}

/* DROPDOWN */
div[role="listbox"] {
    background-color: #bfdbfe !important;
}

div[role="option"] {
    background-color: #bfdbfe !important;
    color: #1e3a8a !important;
}

div[role="option"]:hover {
    background-color: #93c5fd !important;
}

/* SIDEBAR LIST (FITUR) */
section[data-testid="stSidebar"] ul {
    background: transparent !important;
}

section[data-testid="stSidebar"] li {
    background: transparent !important;
    color: #334155 !important;
    padding: 2px 0 !important;
}

/* SEMUA TEXT */
h1, h2, h3, h4, h5, h6, p, label, span, div {
    color: #000000 !important;
}

/* INPUT */
input, select {
    background: white !important;
    color: black !important;
}

/* BUTTON */
.stButton > button {
    background: #60a5fa !important;
    color: white !important;
    border-radius: 10px;
}

/* METRIC */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.85);
    border-radius: 12px;
    padding: 16px !important;
    color: black;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #bfdbfe !important;
}

/* HILANGKAN MENU */
#MainMenu, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:

    # CSS SIDEBAR
    st.markdown("""
    <style>
    .logo-icon {
        font-size: 34px; /* BESARIN/KECILIN DISINI */
        padding: 8px;
        border-radius: 10px;
    }

    .logo-text {
        display: flex;
        flex-direction: column;
    }

    .logo-title {
        font-weight: 700;
        font-size: 18px;
        color: #1e293b;
    }

    .logo-subtitle {
        font-size: 11px;
        color: #64748b;
    }

	.card-name {
    background: #3b82f6;
    color: white;
    padding: 12px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 13px;
    margin-bottom: 12px;
    text-align: center;
}    

    .card-desc {
        background: #e0f2fe;
        color: #1e3a8a;
        padding: 14px;
        border-radius: 12px;
        font-size: 12.5px;
        line-height: 1.6;
        margin-bottom: 14px;
    }

    .fitur-title {
        color: #334155;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 6px;
    }

   .fitur-list {
    font-family:sans-serif;
    color: #475569;
    font-size: 10px;
    }
       </style>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="font-weight:700; font-size:20px; color:#1e293b; display:flex; align-items:center; gap:6px;">
    <span style="font-size:32px;">⛅</span>
    <span>Weather ML App</span>
</div>
<div style="font-size:13px; color:#64748b; margin-bottom:12px;">
    Klasifikasi Kondisi Cuaca
</div>
""", unsafe_allow_html=True)

    st.markdown("""
    <div>
    <p style='font-size:12px;color:#64748b;margin-bottom:4px;'>👩‍💻 Dibuat oleh</p>
    <div class="card-name">
        Ezza Fahimah Aryani
    </div>

    <div class="card-desc">
        Aplikasi ini memprediksi kondisi Cuaca berdasarkan parameter lingkungan dan atmosfer.
    </div>

    <hr>

    <div class="fitur-title">Fitur :</div>
    <ul class="fitur-list">
        <li>Prediksi Real-time</li>
        <li>Probabilitas Hasil Prediksi</li>
        <li>Insight Model</li>
        <li>Download Dataset</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)
col1, col2 = st.columns([6,1])

with col1:
    st.markdown(
        "<h1 style='font-family:Sora,sans-serif;font-size:2rem;font-weight:700;color:#dce6f5;margin-bottom:4px;'>Prediksi Kondisi Cuaca</h1>"
        "<p style='color:#3d6e99;font-size:0.88rem;margin-bottom:20px;'>Random Forest Classifier &nbsp;·&nbsp; Machine Learning &nbsp;·&nbsp; 13.200 Data</p>",
        unsafe_allow_html=True
    )

with col2:
    st.image("logo smk, streamlit.png", width=60)

# NAVBAR
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Prediksi", "📊 Informasi", "👩‍💻 About Me", "💻 Source Code"])

# PREDIKSI
st.markdown("""
<style>
/* SELECTBOX */
div[data-baseweb="select"] > div {
    background-color: #dbeafe !important;
    border: 1px solid #93c5fd !important;
    color: #1e3a8a !important;
}

/* DROPDOWN MENU */
ul {
    background-color: #bfdbfe !important;
    color: #1e3a8a !important;
}

/* ITEM DROPDOWN */
li {
    background-color: #bfdbfe !important;
    color: #1e3a8a !important;
}

/* HOVER DROPDOWN */
li:hover {
    background-color: #93c5fd !important;
}

/* NUMBER INPUT (+ - BUTTON) */
button {
    background-color: #bfdbfe !important;
    color: #1e3a8a !important;
    border: none !important;
}

/* BUTTON + - HOVER */
button:hover {
    background-color: #93c5fd !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* SELECTBOX CONTAINER (LUAR) */
div[data-testid="stSelectbox"] > div {
    background-color: #e6f0ff !important;
    border-radius: 10px !important;
}

/* FIELD DALAM SELECTBOX */
div[data-baseweb="select"] > div {
    background-color: #e6f0ff !important;
    border: 1px solid #60a5fa !important;
    border-radius: 10px !important;
    color: #1e293b !important;
}

/* TEXT DI DALAM */
div[data-baseweb="select"] span {
    color: #1e293b !important;
}

/* ICON DROPDOWN */
div[data-baseweb="select"] svg {
    fill: #1e293b !important;
}
            
/* LIST ITEM */
li {
    background-color: #e6f0ff !important;
    color: #1e293b !important;
}

/* HOVER */
li:hover {
    background-color: #bfdbfe !important;
}

/* NUMBER INPUT */
div[data-testid="stNumberInput"] input {
    background-color: #e6f0ff !important;
    border: 1px solid #60a5fa !important;
    border-radius: 10px !important;
    color: #1e293b !important;
}
/* TAB JANGAN KEUBAH */
button[role="tab"] {
    background: transparent !important;
    border: none !important;
}

</style>
""", unsafe_allow_html=True)
with tab1:
    st.markdown(
        "<div style='font-family:Sora,sans-serif;font-weight:700;color:#dce6f5;font-size:1.05rem;margin-bottom:16px;'>🔍 Masukkan Parameter Cuaca</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p style='color:#3d6e99;font-size:0.72rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-bottom:1px solid #1a3358;padding-bottom:6px;margin-bottom:14px;'>🌡️ Parameter Atmosfer</p>", unsafe_allow_html=True)
        suhu       = st.number_input("Suhu", 0, 50, 28)
        kelembapan = st.number_input("Kelembapan (%)", 0, 100, 80)
        angin      = st.number_input("Kecepatan Angin (km)", 0, 50, 10)
        hujan      = st.number_input("Curah Hujan (%)", 0, 100, 40)
        tekanan    = st.number_input("Tekanan Atmosfer", 900, 1100, 1008)

    with col2:
        st.markdown("<p style='color:#3d6e99;font-size:0.72rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-bottom:1px solid #1a3358;padding-bottom:6px;margin-bottom:14px;'>☁️ Kondisi Lingkungan</p>", unsafe_allow_html=True)
        awan   = st.selectbox("Tutupan Awan", ["cerah", "cerah berawan", "berawan", "mendung"])
        uv     = st.number_input("Indeks UV", 0, 11, 4)
        musim  = st.selectbox("Musim", ["Musim Dingin", "Musim Panas", "Musim Semi", "Musim Gugur"])
        jarak  = st.number_input("Jarak Pandang (km)", 0, 20, 8)
        lokasi = st.selectbox("Lokasi", ["daratan", "pegunungan", "pesisir"])

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    if st.button("🔍 Hasil Prediksi Cuaca"):

        data_baru = pd.DataFrame(
            [[suhu, kelembapan, angin, hujan, awan, tekanan, uv, musim, jarak, lokasi]],
            columns=[
                "Suhu","Kelembapan","Kecepatan Angin","Curah Hujan (%)",
                "Tutupan Awan","Tekanan Atmosfer","Indeks UV",
                "Musim","Jarak Pandang (km)","Lokasi"
            ]
        )

        prediksi = model.predict(data_baru)[0]
        probas   = model.predict_proba(data_baru)[0]
        persen   = max(probas) * 100
        pbar     = int(persen)

        weather_map = {
            "cerah": ("🌤️", "Cerah", "#f0c040", "Cuaca cerah! Cocok untuk aktivitas diluar ruangan."),
            "hujan": ("🌧️", "Hujan", "#4caf80", "Hujan berpotensi turun. Bawa payung!"),
            "berawan": ("☁️", "Berawan", "#5ba3d9", "Langit berawan, teduh dan nyaman."),
            "mendung": ("🌥️", "Mendung", "#a0a8f0", "Mendung, kemungkinan hujan ringan."),
            "snowy": ("🌨️", "Snowy", "#a8c8e8", "Kemungkinan salju. Waspada jalanan licin."),
        }

        emoji, label, warna, desc = weather_map.get(
            prediksi.lower(),
            ("🌦️", prediksi, "#5ba3d9", "Kondisi cuaca stabil.")
        )

        # CARD
        st.markdown(
            f"<div style='background:#f1f3f6;border-left:6px solid #4a90e2;border-radius:16px;padding:30px 24px;text-align:center;margin-top:16px;'>"
            f"<div style='font-size:3.6rem;margin-bottom:8px;'>{emoji}</div>"
            f"<div style='font-size:1.9rem;font-weight:700;color:#000;margin-bottom:8px;'>{label}</div>"
            f"<div style='display:inline-block;background:#fff;border:1px solid #ddd;color:#333;border-radius:50px;padding:4px 16px;font-size:0.85rem;margin-bottom:12px;'>Akurasi {persen:.1f}%</div>"
            f"<div style='background:#e0e0e0;border-radius:50px;height:6px;max-width:220px;margin:0 auto 14px;'>"
            f"<div style='width:{pbar}%;height:100%;background:#4a90e2;border-radius:50px;'></div></div>"
            f"<div style='color:#333;font-size:0.9rem;'>{desc}</div>"
            f"</div>",
            unsafe_allow_html=True
        )
        if prediksi.lower() == "cerah":
            st.balloons()
        elif prediksi.lower() in ["hujan", "snowy"]:
            st.snow()
        # GRAFIK
        st.markdown("<h3>Grafik Hasil Prediksi</h3>", unsafe_allow_html=True)
        prob_df = pd.DataFrame({
            "Kondisi": model.classes_,
            "Probabilitas (%)": (probas * 100).round(2)
        })
        st.bar_chart(prob_df.set_index("Kondisi"), height=220)

# INFORMASI
with tab2:
    # METRIC 
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Data",  f"{len(df):,}")
    c2.metric("Kelas Cuaca", df["Jenis Cuaca"].nunique())
    c3.metric("Fitur Input", len(df.columns) - 1)
    c4.metric("Akurasi",     "~94%")

    st.markdown("<br>", unsafe_allow_html=True)

    # CARD UTAMA 
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="
            background:white;
            padding:24px;
            border-radius:14px;
            box-shadow:0 2px 10px rgba(0,0,0,0.08);
            border-left:5px solid #60a5fa;
        ">
            <h3>Aplikasi</h3>
            <p style="font-size:14px; line-height:1.7;">
                Aplikasi sistem prediksi cuaca berbasis <b>Machine Learning</b>
                menggunakan <b>Streamlit</b>. User dapat memasukkan parameter lingkungan
                untuk mendapatkan prediksi cuaca secara real-time.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background:white;
            padding:24px;
            border-radius:14px;
            box-shadow:0 2px 10px rgba(0,0,0,0.08);
            border-left:5px solid #38bdf8;
        ">
            <h3>Model</h3>
            <p style="font-size:14px; line-height:1.7;">
                Model terbaik yang digunakan adalah model <b>Random Forest Classifier</b>.
                Algoritma ini bekerja dengan menggabungkan banyak Decision tree sehingga
                menghasilkan prediksi yang lebih stabil dan akurat.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # PENJELASAN INPUT 
    st.markdown("<h3>Penjelasan Input</h3>", unsafe_allow_html=True)

    def card(title, desc, icon):
        return f"""
        <div style='
            background:white;
            border-radius:12px;
            padding:14px;
            margin-bottom:10px;
            border:1px solid #e5e7eb;
        '>
            <div style='font-weight:600;'>{icon} {title}</div>
            <div style='font-size:0.82rem;margin-top:6px;color:#333;'>{desc}</div>
        </div>
        """

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(card("Suhu", "Temperatur udara yang memengaruhi kondisi cuaca.", "🌡️"), unsafe_allow_html=True)
        st.markdown(card("Kecepatan Angin", "Kekuatan angin yang dapat mengubah kondisi cuaca.", "🌬️"), unsafe_allow_html=True)
        st.markdown(card("Tutupan Awan", "Persentase langit yang tertutup awan.", "☁️"), unsafe_allow_html=True)
        st.markdown(card("Indeks UV", "Intensitas radiasi ultraviolet dari matahari.", "☀️"), unsafe_allow_html=True)
        st.markdown(card("Jarak Pandang", "Jarak maksimal objek dapat terlihat.", "👁️"), unsafe_allow_html=True)

    with c2:
        st.markdown(card("Kelembapan", "Kadar uap air di udara, tinggi = potensi hujan.", "💧"), unsafe_allow_html=True)
        st.markdown(card("Curah Hujan", "Jumlah hujan yang turun.", "🌧️"), unsafe_allow_html=True)
        st.markdown(card("Tekanan Atmosfer", "Tekanan udara yang memengaruhi perubahan cuaca.", "🌡️"), unsafe_allow_html=True)
        st.markdown(card("Musim", "Konteks pola cuaca berdasarkan musim.", "🍂"), unsafe_allow_html=True)
        st.markdown(card("Lokasi", "Wilayah geografis yang memengaruhi cuaca.", "📍"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    # DATASET 
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("📋 Dataset")
    st.markdown("""
    Dataset berisi berbagai parameter cuaca yang digunakan untuk melatih model.
    Setiap baris merepresentasikan kondisi cuaca tertentu.
    """, unsafe_allow_html=True)
    st.dataframe(df)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:white;
        padding:18px;
        border-radius:12px;
        border:1px solid #e5e7eb;
        margin-bottom:10px;
    ">
        <b>⬇️ Download Dataset</b>
        <p style="font-size:13px; color:#444;">Download dataset untuk analisis atau pembelajaran.</p>
    </div>
    """, unsafe_allow_html=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download dataset_cuaca.csv",
        csv,
        "dataset_cuaca.csv",
        "text/csv"
    )
    # DISTRIBUSI
    st.markdown("<h3>📊 Distribusi Dataset</h3>", unsafe_allow_html=True)
    chart = df["Jenis Cuaca"].value_counts().reset_index()
    chart.columns = ["Cuaca", "Jumlah"]
    st.bar_chart(chart.set_index("Cuaca"), height=250)

# About Me 
with tab3:
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    col_foto, col_info = st.columns([1, 1.8])
    
    with col_foto:
        st.markdown(f"""
            <div style='display: flex; justify-content: center; padding-top: 10px;'>
                <div style='width:220px; height:220px; border-radius:50%; overflow:hidden; border:5px solid #ffffff; box-shadow: 0 10px 25px rgba(0,0,0,0.1);'>
                    <img src='data:image/png;base64,{foto_profile}' style='width:100%; height:100%; object-fit:cover;'>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_info:
        st.markdown(f"""
            <div style='font-family:Sora, sans-serif;'>
                <h1 style='margin:0; color:#2563eb; font-size:2rem;'>Ezza Fahimah Aryani</h1>
                <p style='color:#2563eb; font-size:1.2rem; font-weight:600; margin-bottom:10px;'>Machine Learning Developer</p>
                <p style='color:#475569; font-size:0.95rem; line-height:1.6;'>
                    Aplikasi ini tentang sistem prediksi kondisi cuaca berbasis <b>Machine Learning</b> yang dirancang untuk mengklasifikasikan berbagai kondisi cuaca secara otomatis 
                    dan akurat berdasarkan parameter lingkungan dan atmosfer. Sistem ini dibangun 
                    menggunakan <b>Streamlit</b> sebagai antarmuka interaktif.Model yang digunakan dalam aplikasi ini mampu menghasilkan prediksi secara 
                    <b>real-time</b> dengan tingkat akurasi yang optimal.
                </p>
                <p style='font-size:0.85rem; color:#1e293b; font-weight:700; margin-top:15px; margin-bottom:8px;'>Library yang digunakan:</p>
                <div style='margin-bottom: 20px;'>
                    <span style='background:#e2e8f0; color:#475569; border-radius:6px; padding:4px 10px; font-size:0.75rem; font-weight:600; margin-right:5px;'>Streamlit</span>
                    <span style='background:#e2e8f0; color:#475569; border-radius:6px; padding:4px 10px; font-size:0.75rem; font-weight:600; margin-right:5px;'>Scikit-Learn</span>
                    <span style='background:#e2e8f0; color:#475569; border-radius:6px; padding:4px 10px; font-size:0.75rem; font-weight:600; margin-right:5px;'>Pandas</span>
                    <span style='background:#e2e8f0; color:#475569; border-radius:6px; padding:4px 10px; font-size:0.75rem; font-weight:600; margin-right:5px;'>NumPy</span>
                    <span style='background:#e2e8f0; color:#475569; border-radius:6px; padding:4px 10px; font-size:0.75rem; font-weight:600;'>Python</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div style='margin-top:20px;'>
                <div style='display:flex; align-items:center; gap:12px; margin-bottom:10px;'>
                    <img src='data:image/png;base64,{email_icon}' style='width:22px;'>
                    <span style='font-size:0.9rem; color:#475569;'>ezzafahimaharyani@gmail.com</span>
                </div>
                <div style='display:flex; align-items:center; gap:12px; margin-bottom:10px;'>
                    <img src='data:image/png;base64,{github_icon}' style='width:22px;'>
                    <a href='https://github.com/ezzaaryani' target='_blank' style='font-size:0.9rem; color:#2563eb; text-decoration:none;'>@ezzaaryani</a>
                </div>
                <div style='display:flex; align-items:center; gap:12px;'>
                    <img src='data:image/png;base64,{ig_icon}' style='width:22px;'>
                    <a href='https://instagram.com/ezzafhmh_a' target='_blank' style='font-size:0.9rem; color:#2563eb; text-decoration:none;'>@ezzafhmh_a</a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
            <div style="
                background:white;
                padding:20px;
                border-radius:14px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08);
                border-left:5px solid #38bdf8;
                min-height: 120px;
            ">
                <h3 style="margin-top:0; color:#1e293b; font-size:1.1rem;">🎯 Model</h3>
                <p style="font-size:14px; line-height:1.6; color:#475569; margin-bottom:0;">
                    Model ini menggunakan algoritma <b>Random Forest Classifier</b>
            </div>
            """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div style="
                background:white;
                padding:20px;
                border-radius:14px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08);
                border-left:5px solid #38bdf8;
                min-height: 120px;
            ">
                <h3 style="margin-top:0; color:#1e293b; font-size:1.1rem;">📊 Dataset</h3>
                <p style="font-size:14px; line-height:1.6; color:#475569; margin-bottom:0;">
                <b>13.200</b> sampel data, <b>10</b> Fitur teknis dan <b>4</b> Kelas target.
                </p>
            </div>
            """, unsafe_allow_html=True)
# SOURCE CODE TAB
with tab4:
    st.markdown("### Source Code Jupyter Notebook")
    st.markdown(
        "Berikut adalah code tahapan pembuatan model Machine Learning dari awal hingga akhir "
        "berdasarkan notebook yang digunakan."
    )
    # 1. LOAD DATASET
    with st.expander("1. Load Dataset"):
        st.code("""import pandas as pd
        df = pd.read_csv("dataset_cuaca.csv")
        df.head()""", language="python")

        st.write("Output:")
        st.dataframe(df.head(), use_container_width=True)

    # 2. SHAPE
    with st.expander("2. Menampilkan Jumlah Baris dan Kolom"):
        st.code("""df.shape""", language="python")

        st.write("Output:")
        st.write(df.shape)

    # 3. NAMA KOLOM
    with st.expander("3. Menampilkan Nama Kolom"):
        st.code("""df.columns""", language="python")

        st.write("Output:")
        st.write(df.columns)

    # 4. INFO DATASET
    with st.expander("4. Informasi Dataset"):
        st.code("""df.info()""", language="python")

        st.write("Output:")
        info_df = pd.DataFrame({
            "Kolom": df.columns,
            "Tipe Data": df.dtypes.values,
            "Non-Null Count": df.count().values
        })

        st.dataframe(info_df, use_container_width=True)

    # 5. DESCRIBE
    with st.expander("5. Statistik Data"):
        st.code("""df.describe()""", language="python")

        st.write("Output:")
        st.dataframe(df.describe(), use_container_width=True)

    # 6. DTYPES
    with st.expander("6. Menampilkan Tipe Data setiap kolom"):
        st.code("""df.dtypes""", language="python")

        st.write("Output:")
        st.write(df.dtypes)

    # 7. ENCODING
    with st.expander("7. Encoding Data Kategori"):
        st.code("""from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["Tutupan Awan"] = le.fit_transform(df["Tutupan Awan"])
df["Musim"] = le.fit_transform(df["Musim"])
df["Lokasi"] = le.fit_transform(df["Lokasi"])
df["Jenis Cuaca"] = le.fit_transform(df["Jenis Cuaca"])""", language="python")

        st.write("Output:")
        st.dataframe(df.head(), use_container_width=True)

    # 8. HEAD
    with st.expander("8. Menampilkan 5 baris pertama dari Dataset"):
        st.code("""df.head()""", language="python")

        st.write("Output:")
        st.dataframe(df.head(), use_container_width=True)

    # 9. SAMPLE
    with st.expander("9. Data secara acak (random) dari dataset"):
        st.code("""df.sample(5, random_state=42)""", language="python")

        st.write("Output:")
        st.dataframe(df.sample(5, random_state=42), use_container_width=True)

    # 10. TAIL
    with st.expander("10. Menampilkan 5 baris terakhir dari dataset"):
        st.code("""df.tail()""", language="python")

        st.write("Output:")
        st.dataframe(df.tail(), use_container_width=True)

    # 11. MISSING VALUE
    with st.expander("11. Menampilkan Cek Missing Value"):
        st.code("""df.isnull().sum()""", language="python")

        st.write("Output:")
        st.write(df.isnull().sum())

    # 12. DUPLIKAT
    with st.expander("12. Menghitung jumlah data duplikat"):
        st.code("""df.duplicated().sum()""", language="python")

        st.write("Output:")
        st.write(df.duplicated().sum())

    # 13. VISUALISASI
    with st.expander("13. Visualisasi Data (Scatter Plot)"):
        st.code("""import matplotlib.pyplot as plt

cerah = df[df["Jenis Cuaca"] == "Cerah"]
berawan = df[df["Jenis Cuaca"] == "Berawan"]
hujan = df[df["Jenis Cuaca"] == "Hujan"]

plt.figure(figsize=(6,5))

plt.scatter(cerah["Suhu"], cerah["Kelembapan"], color="blue", label="Cerah")
plt.scatter(berawan["Suhu"], berawan["Kelembapan"], color="pink", label="Berawan")
plt.scatter(hujan["Suhu"], hujan["Kelembapan"], color="red", label="Hujan")

plt.xlabel("Suhu")
plt.ylabel("Kelembapan")
plt.title("Suhu vs Kelembapan")
plt.legend()
plt.show()""", language="python")

        st.write("Output:")

        import matplotlib.pyplot as plt

        cerah = df[df["Jenis Cuaca"] == "Cerah"]
        berawan = df[df["Jenis Cuaca"] == "Berawan"]
        hujan = df[df["Jenis Cuaca"] == "Hujan"]

        fig, ax = plt.subplots(figsize=(6,5))

        ax.scatter(cerah["Suhu"], cerah["Kelembapan"], color="blue", label="Cerah")
        ax.scatter(berawan["Suhu"], berawan["Kelembapan"], color="pink", label="Berawan")
        ax.scatter(hujan["Suhu"], hujan["Kelembapan"], color="red", label="Hujan")

        ax.set_xlabel("Suhu")
        ax.set_ylabel("Kelembapan")
        ax.set_title("Suhu vs Kelembapan")
        ax.legend()

        st.pyplot(fig)

    # 14. LOGISTIC REGRESSION
    with st.expander("14. Model LogisticRegression"):
        st.code("""from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

df = pd.read_csv("dataset_cuaca.csv")

print(df.head())
print("\nTipe Data:\n", df.dtypes)

X = df[[
    "Suhu","Kelembapan","Kecepatan Angin","Curah Hujan (%)",
    "Tutupan Awan","Tekanan Atmosfer","Indeks UV",
    "Musim","Jarak Pandang (km)","Lokasi"
]]

y = df["Jenis Cuaca"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

numeric_columns = [
    "Suhu","Kelembapan","Kecepatan Angin","Curah Hujan (%)",
    "Tekanan Atmosfer","Indeks UV","Jarak Pandang (km)"
]

categorical_columns = [
    "Musim","Lokasi","Tutupan Awan"
]

preprocessing = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_columns),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)
    ]
)

model = Pipeline(
    steps=[
        ("preprocessing", preprocessing),
        ("model", LogisticRegression(max_iter=1000))
    ]
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\n=== HASIL MODEL ===")
print("Accuracy :", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))""", language="python")

        st.write("Output:")
        st.success("Accuracy : 0.8712121212121212")
        st.text("Model LogisticRegression berhasil dilatih.")

    # 15. DECISION TREE
    with st.expander("15. Model DecisionTreeClassifier"):
        st.code("""from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

df = pd.read_csv("dataset_cuaca.csv")

X = df[[
    "Suhu","Kelembapan","Kecepatan Angin","Curah Hujan (%)",
    "Tutupan Awan","Tekanan Atmosfer","Indeks UV",
    "Musim","Jarak Pandang (km)","Lokasi"
]]

y = df["Jenis Cuaca"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

numeric_columns = [
    "Suhu","Kelembapan","Kecepatan Angin","Curah Hujan (%)",
    "Tekanan Atmosfer","Indeks UV","Jarak Pandang (km)"
]

categorical_columns = ["Musim","Lokasi"]
ordinal_columns = ["Tutupan Awan"]

awan_order = ["Cerah", "Cerah Berawan", "Berawan", "Mendung"]
ordinal_order = [awan_order]

preprocessing = ColumnTransformer(
    transformers=[
        ("scaler", StandardScaler(), numeric_columns),
        ("ohe", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
       ("oe", OrdinalEncoder(), ordinal_columns)
    ]
)
model = Pipeline(
    steps=[
        ("preprocessing", preprocessing),
        ("model", DecisionTreeClassifier(random_state=42))
    ]
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy :", accuracy_score(y_test, y_pred))
print("\nClassification Report :\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix :\n", confusion_matrix(y_test, y_pred))
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print("\nScores :\n", scores)
print("\nMean Scores :", scores.mean())""", language="python")

        st.write("Output:")
        st.success("Accuracy : 0.9090909090909091")
        st.text("Model DecisionTreeClassifier berhasil dilatih.")

    # 16. RANDOM FOREST
    with st.expander("16. Model RandomForestClassifier"):
        st.code("""from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

df = pd.read_csv("dataset_cuaca.csv")

X = df[[
    "Suhu","Kelembapan","Kecepatan Angin","Curah Hujan (%)",
    "Tutupan Awan","Tekanan Atmosfer","Indeks UV",
    "Musim","Jarak Pandang (km)","Lokasi"
]]
y = df["Jenis Cuaca"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

numeric_columns = [
    "Suhu","Kelembapan","Kecepatan Angin","Curah Hujan (%)",
    "Tekanan Atmosfer","Indeks UV","Jarak Pandang (km)"
]

categorical_columns = ["Musim","Lokasi"]
ordinal_columns = ["Tutupan Awan"]

awan_order = ["Cerah", "Cerah Berawan", "Berawan", "Mendung"]
ordinal_order = [awan_order]

preprocessing = ColumnTransformer(
    transformers=[
        ("scaler", StandardScaler(), numeric_columns),
        ("ohe", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
        ("oe", OrdinalEncoder(), ordinal_columns)
    ]
)

model = Pipeline(
    steps=[
        ("preprocessing", preprocessing),
        ("model", RandomForestClassifier(random_state=42))
    ]
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy :", accuracy_score(y_test, y_pred))
print("\nClassification Report :\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix :\n", confusion_matrix(y_test, y_pred))
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print("\nScores :\n", scores)
print("\nMean Scores :", scores.mean())""", language="python")

        st.write("Output:")
        st.success("Accuracy : 0.9143939393939394")
        st.text("Model RandomForestClassifier berhasil dilatih.")

    # 17. DATA BARU
    with st.expander("17. Data Baru"):
        st.code("""data_baru = pd.DataFrame(
[[14.0, 73, 9.5, 82.0, "cerah berawan", 1010.82, 2,
"Musim Dingin", 3.5, "Daratan"]]
)""", language="python")

        st.write("Output:")

        data_baru = pd.DataFrame(
            [[14.0, 73, 9.5, 82.0, "cerah berawan",
              1010.82, 2, "Musim Dingin", 3.5, "Daratan"]],
            columns=[
                "Suhu","Kelembapan","Kecepatan Angin","Curah Hujan (%)",
                "Tutupan Awan","Tekanan Atmosfer","Indeks UV",
                "Musim","Jarak Pandang (km)","Lokasi"
            ]
        )

        st.dataframe(data_baru, use_container_width=True)

        st.success(
            "Model memprediksi Cerah dengan tingkat keyakinan 94.21%"
        )
    # 18. JOBLIB
    with st.expander("18. Simpan Model Joblib"):
        st.code("""import joblib

joblib.dump(model, "model_klasifikasi_cuaca.joblib")""", language="python")

        st.write("Output:")
        st.success("Model berhasil disimpan menjadi model_klasifikasi_cuaca.joblib")
# FOOTER
st.markdown(
    "<hr style='border:none;border-top:1px solid #1a3358;margin:36px 0 14px;'>"
    "<div style='text-align:center;color:#3d6e99;font-size:0.78rem;padding-bottom:14px;'>"
    "© 2026 <b style='color:#6b9ec7;'>Ezza Fahimah Aryani</b> &nbsp;·&nbsp; Weather Classification App"
    "</div>",
    unsafe_allow_html=True
) 