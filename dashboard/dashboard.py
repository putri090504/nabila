import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Judul dashboard
st.title("Dashboard Pengamatan Konsentrasi PM2.5 dan PM10")

# Menampilkan logo di sidebar
st.sidebar.image("shunyi.png", use_column_width=True)

# Data kedua (untuk perubahan PM2.5 dari jam 0 hingga 23)
data2 = {
    'hour': list(range(24)),
    'PM2.5': [
        93.994679, 91.150499, 87.262760, 83.141916, 79.469492, 
        76.089656, 72.451231, 70.648785, 71.177790, 72.382608, 
        74.306758, 74.660721, 74.424473, 73.397832, 72.589171, 
        71.389551, 70.961471, 72.937423, 74.913556, 79.647937, 
        86.262444, 91.742778, 95.092609, 96.414948
    ]
}

# Membuat DataFrame kedua
df2 = pd.DataFrame(data2)

# Menghitung persentase perubahan nilai PM2.5 dari jam 0 hingga jam 23
nilai_awal = df2['PM2.5'].iloc[0]
nilai_akhir = df2['PM2.5'].iloc[-1]
persentase_perubahan = ((nilai_akhir - nilai_awal) / nilai_awal) * 100

# Plot data kedua (perubahan PM2.5 dari jam 0 hingga 23)
st.subheader("Perubahan Nilai PM2.5 Selama 24 Jam")
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(df2['hour'], df2['PM2.5'], marker='o', color='b', label='PM2.5')
ax2.set_title('Perubahan Nilai PM2.5 Selama 24 Jam')
ax2.set_xlabel('Jam')
ax2.set_ylabel('Nilai PM2.5')
ax2.set_xticks(df2['hour'])  # Menampilkan semua jam di sumbu x
ax2.grid()
ax2.legend()

# Menampilkan grafik kedua di Streamlit
st.pyplot(fig2)

# Menampilkan hasil persentase perubahan
st.write(f"Persentase perubahan nilai PM2.5 dari jam 0 hingga jam 23: {persentase_perubahan:.2f}%")

# Kesimpulan Pertanyaan 2
st.subheader("Kesimpulan Pertanyaan 2")
st.write(f"""
Persentase perubahan nilai PM2.5 dari jam 0 hingga jam 23 adalah {persentase_perubahan:.2f}%. 
Jika nilai PM2.5 meningkat, ini bisa menunjukkan penurunan kualitas udara. 
Jika nilainya menurun, ini bisa menunjukkan perbaikan dalam kualitas udara.
""")

# Data pertama (untuk hubungan PM2.5, PM10, dan variabel cuaca)
data1 = {
    'year': [2014, 2016, 2016, 2017, 2015],
    'month': [2, 8, 1, 1, 11],
    'day': [7, 7, 15, 18, 14],
    'hour': [1, 3, 18, 21, 4],
    'PM2.5': [100.0, 41.0, 100.0, 80.0, 240.0],
    'PM10': [84.0, 41.0, 121.0, 103.0, 240.0],
    'TEMP': [-2.1, 25.4, 1.3, -1.325, 7.3],
    'PRES': [1026.9, 1002.3, 1013.7, 1028.0, 1013.6],
    'WSPM': [1.8, 3.2, 0.8, 1.2, 1.0],
    'wd': ['SE', 'NNE', 'SSE', 'SE', 'NNE'],
}

# Membuat DataFrame pertama
df1 = pd.DataFrame(data1)

# Plot data pertama (PM2.5, PM10, dan variabel cuaca)
st.subheader("Grafik Hubungan PM2.5, PM10, dan Variabel Cuaca")
fig, ax = plt.subplots(2, 2, figsize=(14, 7))

# Plot PM2.5 vs TEMP
ax[0, 0].scatter(df1['TEMP'], df1['PM2.5'], color='blue')
ax[0, 0].set_title('PM2.5 vs Suhu')
ax[0, 0].set_xlabel('Suhu (°C)')
ax[0, 0].set_ylabel('PM2.5')

# Plot PM10 vs TEMP
ax[0, 1].scatter(df1['TEMP'], df1['PM10'], color='green')
ax[0, 1].set_title('PM10 vs Suhu')
ax[0, 1].set_xlabel('Suhu (°C)')
ax[0, 1].set_ylabel('PM10')

# Plot PM2.5 vs PRES
ax[1, 0].scatter(df1['PRES'], df1['PM2.5'], color='red')
ax[1, 0].set_title('PM2.5 vs Tekanan')
ax[1, 0].set_xlabel('Tekanan (hPa)')
ax[1, 0].set_ylabel('PM2.5')

# Plot PM10 vs WSPM (Kecepatan Angin)
ax[1, 1].scatter(df1['WSPM'], df1['PM10'], color='purple')
ax[1, 1].set_title('PM10 vs Kecepatan Angin')
ax[1, 1].set_xlabel('Kecepatan Angin (m/s)')
ax[1, 1].set_ylabel('PM10')

# Menampilkan grafik pertama di Streamlit
st.pyplot(fig)

# Kesimpulan Pertanyaan 1
st.subheader("Kesimpulan Pertanyaan 1")
st.write("""
Suhu dan Tekanan Udara tampaknya memiliki hubungan dengan konsentrasi polutan (PM2.5 dan PM10). 
Pada suhu yang lebih rendah dan tekanan yang lebih tinggi, konsentrasi polutan cenderung meningkat. 
Kecepatan angin tidak menunjukkan pengaruh yang jelas terhadap konsentrasi PM10 dalam data ini. 
Faktor cuaca seperti suhu dan tekanan mungkin mempengaruhi pengendapan atau penyebaran partikel polutan di udara, 
yang dapat menyebabkan peningkatan polusi udara pada kondisi cuaca tertentu.
""")
