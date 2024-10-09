# Belajar Analisis Data dengan Python Dicoding

## Project Analisis Data

Repository ini berisi proyek analisis data yang saya kerjakan, dengan deployment menggunakan Streamlit <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo"></img>.

## Deskripsi

Proyek ini bertujuan untuk menganalisis data dari Air Quality Dataset. Tujuan akhir adalah menghasilkan wawasan dan informasi berharga dari data yang dianalisis.

## Struktur Direktori
/data: Berisi data yang digunakan dalam proyek dalam format .csv.
/dashboard: Berisi file main.py yang digunakan untuk membuat dashboard hasil analisis.
notebook.ipynb: File ini digunakan untuk melakukan analisis data.


## Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt


## Setup Environment - Shell/Terminal
mkdir analisis_data_dicoding
cd analisis_data_dicoding
pipenv install
pipenv shell
pip install -r requirements.txt


## Run steamlit app
streamlit run dashboard.py

