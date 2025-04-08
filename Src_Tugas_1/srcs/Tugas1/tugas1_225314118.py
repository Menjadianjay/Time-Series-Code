# -*- coding: utf-8 -*-
"""
TIME SERIES 
PLOT DATA RERATA TABUNGAN NASABAH DARI TAHUN 2008 HINGGA TAHUN 2010
*   JOSEPH SERI APRILLIO DE ORNAY
*   225314118
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os 

data_path=r'srcs\tugas1\bank-full-copy.csv'

df=pd.read_csv(data_path,sep=';', usecols=['balance','day','month'])

df.info()

df['year'] = None
tahun_sekarang = 2008
bulan_sebelum = None

for idx, row in df.iterrows():
    bulan_sekarang = row['month']
    if bulan_sebelum == 'dec' and bulan_sekarang == 'jan':
        tahun_sekarang += 1
    df.at[idx, 'year'] = tahun_sekarang
    bulan_sebelum = bulan_sekarang

df.tail()

mapping_bulan = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

df['month'] = df['month'].map(mapping_bulan)
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

print(df[['balance', 'day', 'month', 'year', 'date']].head())

df = df.drop(['day', 'month', 'year'], axis=1)
x = df['date']
y = df['balance']
plt.figure(figsize=(12, 6))
plt.plot(x , y, color='orange', linewidth=1)
plt.title("Rerata Tabungan Nasabah Periode 2008-2010", fontsize=14)
plt.xlabel("Tanggal", fontsize=12)
plt.ylabel("Nilai", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

df.to_csv('srcs\tugas1\x08ank-full-copy.csv', index=False)
""""
Saya menggunakan data perbankan untuk melihat ilustrasi fluktuasi tabungan dari berbagai nasabah yang terdata dari may 2008 sampai november 2010. 
Hal ini berguna dalam menentukan kelayakan kredit seorang nasabah berdasarkan kondisi keuangan nasabah. 
Jika bannk dapat mengetahui tingkat kesehatan keuangan dari masing-masing nasabah, maka bank dapat memberikan penawaran tertentu bagi para nasabah dengan kondisi kesehatan keuangan yang sesuai. 
Misalnya menawarkan menjadi nasabah premium yang tentunya memberikan keuntungan kepeada kedua belah pihak. Singkatnya dengan mengetahui average yearly balance dari masing masing nasabah yang dapat membantu bank dalam analisis risiko, strategi pemasaran, manajemen likuiditas, dan penilaian nasabah untuk kredit atau investasi.

Data diambil dari bank UCL Dataset dengan judul "Bank Marketing". Saya menambahkan kolom tahun sehingga dapat menampilkan format data yang lengkap dengan rentang 2008 hingga 2010.
"""