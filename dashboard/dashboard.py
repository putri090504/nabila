import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur gaya visual seaborn
sns.set(style='dark')

# Membuat DataFrame dari data PM2.5 dan PM10
data = {
    'hour': list(range(24)),
    'PM2.5': [
        93.994679, 91.150499, 87.262760, 83.141916, 79.469492, 
        76.089656, 72.451231, 70.648785, 71.177790, 72.382608, 
        74.306758, 74.660721, 74.424473, 73.397832, 72.589171, 
        71.389551, 70.961471, 72.937423, 74.913556, 79.647937, 
        86.262444, 91.742778, 95.092609, 96.414948
    ],
    'PM10': [
        118.253369, 112.300723, 105.226472, 98.153504, 92.124045,
        87.713158, 84.179889, 84.102608, 88.883530, 91.714221,
        92.108490, 90.720187, 88.856544, 87.331984, 88.054851,
        89.380479, 90.167765, 93.919118, 100.345861, 109.264577,
        117.802295, 123.102893, 124.347666, 124.472224
    ]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menghitung persentase perubahan nilai PM2.5 dari jam 0 hingga jam 23
nilai_awal = df['PM2.5'].iloc[0]
nilai_akhir = df['PM2.5'].iloc[-1]
persentase_perubahan = ((nilai_akhir - nilai_awal) / nilai_awal) * 100

# Menampilkan aplikasi Streamlit
st.title('Dashboard Analisis Kualitas Udara')

# Menampilkan logo perusahaan di sidebar
st.sidebar.image("shunyi.png", use_column_width=True)  # Ganti dengan URL gambar jika diperlukan

# Menampilkan persentase perubahan PM2.5
st.subheader('Persentase Perubahan PM2.5')
st.write(f"Persentase perubahan nilai PM2.5 dari jam 0 hingga jam 23: {persentase_perubahan:.2f}%")

# Membuat grafik perubahan nilai PM2.5
st.subheader('Grafik Perubahan PM2.5 Selama 24 Jam')
plt.figure(figsize=(12, 6))
plt.plot(df['hour'], df['PM2.5'], marker='o', color='b', label='PM2.5')
plt.title('Perubahan Nilai PM2.5 Selama 24 Jam')
plt.xlabel('Jam')
plt.ylabel('Nilai PM2.5')
plt.xticks(df['hour'])  # Menampilkan semua jam di sumbu x
plt.grid()
plt.legend()
plt.tight_layout()
st.pyplot(plt)

# Membuat grafik untuk PM2.5 dan PM10
plt.figure(figsize=(12, 6))
plt.plot(df['hour'], df['PM2.5'], marker='o', color='b', label='PM2.5')
plt.plot(df['hour'], df['PM10'], marker='s', color='r', label='PM10')
plt.title('Perubahan Nilai PM2.5 dan PM10 Selama 24 Jam', fontsize=20)
plt.xlabel('Jam', fontsize=15)
plt.ylabel('Konsentrasi (µg/m³)', fontsize=15)
plt.xticks(df['hour'])  # Menampilkan semua jam di sumbu x
plt.grid()
plt.legend()
plt.tight_layout()

# Menampilkan grafik PM2.5 dan PM10
st.subheader('Grafik Perubahan Nilai PM2.5 dan PM10')
st.pyplot(plt)

# Menyimpulkan dari grafik
st.subheader('Kesimpulan')
if persentase_perubahan > 0:
    st.write("Terjadi peningkatan konsentrasi PM2.5 dari jam 0 hingga jam 23.")
else:
    st.write("Terjadi penurunan konsentrasi PM2.5 dari jam 0 hingga jam 23.")

# Analisis grafik PM2.5 dan PM10
st.write("Dari grafik, dapat dilihat bahwa PM10 memiliki konsentrasi yang lebih tinggi dibandingkan dengan PM2.5, "
         "menunjukkan bahwa partikel yang lebih besar lebih banyak di udara. Fluktuasi nilai menunjukkan variasi "
         "kualitas udara yang mungkin disebabkan oleh aktivitas manusia atau faktor lingkungan.")
