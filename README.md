# Belajar Analisis Data dengan Python Dicoding

## Project Analisis Data

Repository ini berisi proyek analisis data yang saya kerjakan. Deployment di Streamlit <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo"></img>

## Deskripsi

Proyek ini bertujuan untuk menganalisis data dari Air Quality Dataset dan menghasilkan wawasan serta informasi berguna.

## Struktur Direktori

/data: Menyimpan data dalam format .csv.
/dashboard: Berisi main.py untuk membuat dashboard hasil analisis.
notebook.ipynb: Digunakan untuk analisis data.


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

