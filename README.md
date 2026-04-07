# Palm Oil Yield Prediction & Land Clustering

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat-square&logo=jupyter)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-brightgreen?style=flat-square)

## Deskripsi Proyek
Proyek ini berfokus pada analisis data agronomi kelapa sawit dan pembangunan model *Machine Learning* untuk memprediksi hasil panen (*yield*). Selain prediksi, proyek ini juga mencakup analisis korelasi antar variabel iklim/agronomi dan pemetaan klaster lahan (blok) untuk mengidentifikasi area dengan performa terbaik.

## Objektif
1. **Analisis Korelasi**: Memahami hubungan antara variabel operasional (seperti pupuk NPK, curah hujan, *sex ratio*) terhadap hasil panen.
2. **Pemodelan Prediksi**: Membangun dan mengevaluasi model prediksi *yield* (kg/ha) menggunakan algoritma **Random Forest**.
3. **Segmentasi Lahan**: Menerapkan teknik klastering dan visualisasi *Principal Component Analysis* (PCA) untuk mengelompokkan blok lahan berdasarkan karakteristik *yield* dan *sex ratio*.

## Dataset
Data historis yang digunakan dalam proyek ini (`datasetKS2.csv`) mencakup fitur-fitur berikut:
* `tanggal_panen`: Tanggal pencatatan panen.
* `luas_ha`: Luas area blok (Hektar).
* `umur_tanaman`: Umur tanaman kelapa sawit (Bulan).
* `populasi_ha`: Kerapatan pokok per hektar (SPH).
* `produksi`: Total produksi Tandan Buah Segar / TBS (Kg).
* `pupuk_npk`: Dosis aplikasi pupuk NPK (Kg).
* `curah_hujan`: Intensitas curah hujan (mm).
* `sex_ratio`: Rasio bunga betina terhadap total bunga.
* `yield_kg_ha`: Hasil panen per hektar (Target Variabel yang diekstrak dari produksi / luas area).

## Metodologi
1. **Data Preprocessing**: Pembersihan tipe data, pemformatan kolom waktu (`datetime`), dan rekayasa fitur (menghitung `yield_kg_ha`).
2. **Exploratory Data Analysis (EDA)**: Visualisasi sebaran matriks korelasi untuk menemukan faktor paling dominan terhadap produktivitas.
3. **Clustering & PCA**: Mengelompokkan blok lahan dan memvisualisasikan *Distribution of Land Clusters* untuk mengidentifikasi blok "Juara" di masing-masing klaster.
4. **Machine Learning**: Pelatihan model *Random Forest Regressor* untuk memprediksi *yield* kelapa sawit secara presisi.

## Teknologi & Library
Proyek ini dibangun menggunakan ekosistem Data Science Python:
* **Pengolahan Data**: `pandas`, `numpy`
* **Visualisasi Data**: `matplotlib`, `seaborn`
* **Machine Learning & Analisis**: `scikit-learn` (Random Forest, K-Means, PCA)

## Cara Menjalankan Proyek (Local Setup)

1. Clone repositori ini ke dalam lokal mesin Anda:
   ```bash
   git clone [https://github.com/hamdiakbarrr/PalmOil_Yield_Optimization_Analysis.git](https://github.com/hamdiakbarrr/PalmOil_Yield_Optimization_Analysis.git)
   cd PalmOil_Yield_Optimization_Analysis

## Hasil Analisis & Insight
1. Terdapat pemetaan klaster lahan yang membedakan kinerja tiap blok berdasarkan rasio seks dan hasil panen.
2. Fitur Filtering Cluster Blocks pada notebook dapat digunakan secara praktis oleh manajemen kebun untuk memilah daftar blok lahan dalam klaster tertentu dan mengurutkannya berdasarkan yield tertinggi.
