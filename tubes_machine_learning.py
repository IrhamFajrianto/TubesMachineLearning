# -*- coding: utf-8 -*-
"""TUBES_Machine_Learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kIIvRPgxEz3pgm3jwkNyFYCuTiuxV6Nt
"""

# Import library
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
data = pd.read_csv('/content/audi.csv')  # Ganti dengan path dataset Anda

# Tampilkan lima data teratasuntuk memastikan dataset terbaca
print(data.head())

# Data preprocessing
# Tambahkan kolom 'age' untuk mengganti 'year'
data['age'] = 2024 - data['year']  # Misalnya tahun sekarang 2024
data.drop(columns=['year'], inplace=True)  # Hapus kolom 'year' karena sudah diolah

# Konversi fitur kategorikal ke numerik menggunakan One-Hot Encoding before handling missing values
data = pd.get_dummies(data, columns=['model', 'transmission', 'fuelType'], drop_first=True)

# Tangani missing values (jika ada) after oencone-hot ding
data.fillna(data.median(), inplace=True) # Now that all columns are numeric, median can be calculated

# Split data menjadi fitur (X) dan target (y)
X = data.drop(columns=['price'])  # Semua kolom kecuali harga
y = data['price']  # Target prediksi

# Split dataset menjadi train set dan test set (80:20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi dan training model Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediksi pada data test
y_pred = model.predict(X_test)

# Evaluasi model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

# Contoh prediksi
sample_data = X_test.iloc[0:5]  # Ambil 5 data dari test set
sample_prediction = model.predict(sample_data)
print("Sample Prediksi Harga Mobil:")
print(sample_prediction)

import kagglehub

# Download latest version
path = kagglehub.dataset_download("adityadesai13/used-car-dataset-ford-and-mercedes")

print("Path to dataset files:", path)