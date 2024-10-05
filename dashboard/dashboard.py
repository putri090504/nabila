import pandas as pd
import matplotlib.pyplot as plt

# Data pertama yang disediakan (untuk hubungan PM2.5, PM10, dan variabel cuaca)
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

# Plot data pertama (PM2.5, PM10, dan variabel cuaca)
plt.figure(figsize=(14, 7))

# Plot PM2.5 vs TEMP
plt.subplot(2, 2, 1)
plt.scatter(df1['TEMP'], df1['PM2.5'], color='blue')
plt.title('PM2.5 vs Suhu')
plt.xlabel('Suhu (°C)')
plt.ylabel('PM2.5')

# Plot PM10 vs TEMP
plt.subplot(2, 2, 2)
plt.scatter(df1['TEMP'], df1['PM10'], color='green')
plt.title('PM10 vs Suhu')
plt.xlabel('Suhu (°C)')
plt.ylabel('PM10')

# Plot PM2.5 vs PRES
plt.subplot(2, 2, 3)
plt.scatter(df1['PRES'], df1['PM2.5'], color='red')
plt.title('PM2.5 vs Tekanan')
plt.xlabel('Tekanan (hPa)')
plt.ylabel('PM2.5')

# Plot PM10 vs WSPM (Kecepatan Angin)
plt.subplot(2, 2, 4)
plt.scatter(df1['WSPM'], df1['PM10'], color='purple')
plt.title('PM10 vs Kecepatan Angin')
plt.xlabel('Kecepatan Angin (m/s)')
plt.ylabel('PM10')

plt.tight_layout()

# Menampilkan grafik pertama
plt.show()

# Plot data kedua (perubahan PM2.5 dari jam 0 hingga 23)
plt.figure(figsize=(10, 6))
plt.plot(df2['hour'], df2['PM2.5'], marker='o', color='b', label='PM2.5')
plt.title('Perubahan Nilai PM2.5 Selama 24 Jam')
plt.xlabel('Jam')
plt.ylabel('Nilai PM2.5')
plt.xticks(df2['hour'])  # Menampilkan semua jam di sumbu x
plt.grid()
plt.legend()

# Menampilkan grafik kedua
plt.tight_layout()
plt.show()

# Menampilkan hasil persentase perubahan
print(f"Persentase perubahan nilai PM2.5 dari jam 0 hingga jam 23: {persentase_perubahan:.2f}%")
