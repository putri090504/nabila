import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style for seaborn
sns.set(style='darkgrid')

# Load data
prsa_shunyi_df = pd.read_csv('C:/Users/ASUS/Downloads/nabila_bila/nabila/data/PRSA_Data_Shunyi_20130301-20170228.csv')

# Filter data for the year 2016
prsa_shunyi_df['year'] = prsa_shunyi_df['year'].astype(int)
data_2016 = prsa_shunyi_df[prsa_shunyi_df['year'] == 2016]

# Monthly average PM2.5
monthly_data_2016 = data_2016[['month', 'PM2.5']]
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
ordered_monthdf = pd.DataFrame(months, columns=['month'])

# Mapping month numbers to month names
map_dict = {i + 1: month for i, month in enumerate(months)}
monthly_data_2016.loc[:, 'month'] = monthly_data_2016['month'].map(map_dict)
monthly_average = monthly_data_2016.groupby('month').median()
monthly_average = pd.merge(ordered_monthdf, monthly_average, left_on='month', right_index=True)
monthly_average = np.round(monthly_average, 1)
monthly_average = monthly_average.set_index('month')

# Streamlit dashboard header
st.title('Dashboard Analisis Kualitas Udara Kota Shunyi')

# Monthly PM2.5 visualization
st.subheader('Rata-Rata Konsentrasi PM2.5 di Udara Kota Shunyi pada Tahun 2016')
fig, ax = plt.subplots(figsize=(12, 5))
with plt.style.context('ggplot'):
    ax = monthly_average.plot(
        kind='bar', 
        color='blue', 
        legend=False, 
        linewidth=.9, 
        edgecolor='black', 
        ax=ax
    )
    ax.set_xlabel('Bulan', fontsize=14)
    ax.set_ylabel('Konsentrasi PM2.5 (µg/m³)', fontsize=14)
    ax.set_title('Rata-Rata Konsentrasi PM2.5 di Udara \ndi Kota Shunyi pada Tahun 2016', fontsize=16)
    ax.grid(axis='x')
    plt.tight_layout()

st.pyplot(fig)

# Conclusion for question 1
st.write("""
**Kesimpulan Pertanyaan 1**: Analisis konsentrasi PM2.5 di Kota Shunyi pada tahun 2016 menunjukkan fluktuasi bulanan yang jelas, dengan nilai rata-rata lebih tinggi pada bulan Januari dan Februari. 
Peningkatan ini kemungkinan disebabkan oleh faktor-faktor seperti pembakaran bahan bakar selama musim dingin, yang berdampak pada kualitas udara. 
Temuan ini menggarisbawahi pentingnya memahami pola musiman dalam perencanaan kebijakan kesehatan masyarakat dan pengendalian polusi udara.
""")

# Hourly average PM2.5
hourly_data = prsa_shunyi_df[['hour', 'PM2.5']]
hrs = [f'{str(i).zfill(2)}.00' for i in range(24)]
hour_dict = {i: j for i, j in enumerate(hrs)}

hourly_data = hourly_data.groupby('hour').median().reset_index()
hourly_data['hour'] = hourly_data['hour'].map(hour_dict)

# Hourly PM2.5 visualization
st.subheader('Rata-Rata Konsentrasi PM2.5 per Jam di Kota Shunyi')
fig, ax = plt.subplots(figsize=(12, 5))
with plt.style.context('ggplot'):
    ax = plt.scatter(hourly_data['hour'], hourly_data['PM2.5'], color='blue', s=100)
    plt.ylabel('Konsentrasi PM2.5 (µg/m³)', fontsize=14)
    plt.xlabel('Jam', fontsize=14)
    plt.title('Rata-Rata Konsentrasi PM2.5 di Udara di Kota Shunyi tiap Jam', fontsize=16)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()

st.pyplot(fig)

# Conclusion for question 2
st.write("""
**Kesimpulan Pertanyaan 2**: Analisis konsentrasi PM2.5 per jam di Kota Shunyi menunjukkan bahwa tingkat polusi cenderung meningkat selama jam sibuk, terutama pada pagi dan sore hari, 
yang dapat dihubungkan dengan aktivitas transportasi dan industri. Sebaliknya, konsentrasi PM2.5 lebih rendah di malam hari ketika aktivitas manusia berkurang. 
Informasi ini penting untuk merancang strategi mitigasi yang efektif dan meningkatkan kualitas udara.
""")
