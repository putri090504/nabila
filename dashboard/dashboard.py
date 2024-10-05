import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Data untuk analisis PM2.5 dan PM10
data = {
    'year': [2014, 2016, 2016, 2017, 2015],
    'month': [2, 8, 1, 1, 11],
    'day': [7, 7, 15, 18, 14],
    'hour': [1, 3, 18, 21, 4],
    'PM2.5': [100.0, 41.0, 100.0, 80.0, 240.0],
    'PM10': [84.0, 41.0, 121.0, 103.0, 240.0],
    'TEMP': [-2.1, 25.4, 1.3, -1.325, 7.3],
    'PRES': [1026.9, 1002.3, 1013.7, 1028.0, 1013.6],
    'WSPM': [1.8, 3.2, 0.8, 1.2, 1.0],
}

# Membuat DataFrame untuk analisis PM2.5 dan PM10
df_pm = pd.DataFrame(data)

# Menghitung rata-rata PM2.5 dan PM10 per tahun
rata_rata_pm = df_pm.groupby('year').mean()[['PM2.5', 'PM10']]

# Plot rata-rata PM2.5 dan PM10 per tahun
plt.figure(figsize=(10, 5))
plt.plot(rata_rata_pm.index, rata_rata_pm['PM2.5'], marker='o', label='Rata-rata PM2.5', color='blue')
plt.plot(rata_rata_pm.index, rata_rata_pm['PM10'], marker='s', label='Rata-rata PM10', color='green')
plt.title('Tren Rata-rata Konsentrasi PM2.5 dan PM10 (2013-2017)')
plt.xlabel('Tahun')
plt.ylabel('Konsentrasi (µg/m³)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Plot hubungan antara PM2.5, PM10, dan variabel cuaca
plt.figure(figsize=(14, 7))

# Plot PM2.5 vs TEMP
plt.subplot(2, 2, 1)
plt.scatter(df_pm['TEMP'], df_pm['PM2.5'], color='blue')
plt.title('PM2.5 vs Suhu')
plt.xlabel('Suhu (°C)')
plt.ylabel('PM2.5')

# Plot PM10 vs TEMP
plt.subplot(2, 2, 2)
plt.scatter(df_pm['TEMP'], df_pm['PM10'], color='green')
plt.title('PM10 vs Suhu')
plt.xlabel('Suhu (°C)')
plt.ylabel('PM10')

# Plot PM2.5 vs PRES
plt.subplot(2, 2, 3)
plt.scatter(df_pm['PRES'], df_pm['PM2.5'], color='red')
plt.title('PM2.5 vs Tekanan')
plt.xlabel('Tekanan (hPa)')
plt.ylabel('PM2.5')

# Plot PM10 vs WSPM (Kecepatan Angin)
plt.subplot(2, 2, 4)
plt.scatter(df_pm['WSPM'], df_pm['PM10'], color='purple')
plt.title('PM10 vs Kecepatan Angin')
plt.xlabel('Kecepatan Angin (m/s)')
plt.ylabel('PM10')

plt.tight_layout()
plt.show()

# Data untuk analisis perubahan PM2.5
data_jam = {
    'hour': list(range(24)),
    'PM2.5': [
        93.994679, 91.150499, 87.262760, 83.141916, 79.469492, 
        76.089656, 72.451231, 70.648785, 71.177790, 72.382608, 
        74.306758, 74.660721, 74.424473, 73.397832, 72.589171, 
        71.389551, 70.961471, 72.937423, 74.913556, 79.647937, 
        86.262444, 91.742778, 95.092609, 96.414948
    ]
}

# Membuat DataFrame untuk perubahan jam
df_jam = pd.DataFrame(data_jam)

# Menghitung persentase perubahan nilai PM2.5 dari jam 0 hingga jam 23
nilai_awal = df_jam['PM2.5'].iloc[0]
nilai_akhir = df_jam['PM2.5'].iloc[-1]
persentase_perubahan = ((nilai_akhir - nilai_awal) / nilai_awal) * 100

# Menampilkan hasil
st.title('Dashboard Analisis Kualitas Udara')

# Menampilkan persentase perubahan PM2.5
st.subheader('Persentase Perubahan Nilai PM2.5 dari Jam 0 hingga Jam 23')
st.write(f"Persentase perubahan nilai PM2.5: {persentase_perubahan:.2f}%")

# Membuat grafik perubahan nilai PM2.5
plt.figure(figsize=(10, 6))
plt.plot(df_jam['hour'], df_jam['PM2.5'], marker='o', color='b', label='PM2.5')
plt.title('Perubahan Nilai PM2.5 Selama 24 Jam')
plt.xlabel('Jam')
plt.ylabel('Nilai PM2.5')
plt.xticks(df_jam['hour'])  # Menampilkan semua jam di sumbu x
plt.grid()
plt.legend()
plt.tight_layout()

# Menampilkan grafik PM2.5
st.subheader('Grafik Perubahan Nilai PM2.5 Selama 24 Jam')
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
