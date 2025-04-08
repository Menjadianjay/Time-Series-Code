'''
TUGAS 2 _ TIME SERIES
JOSEPH SERI APRILLIO DE ORNAY_225314118
'''

import pandas as pd
import matplotlib.pyplot as plt

data_path = r"srcs\tugas2\bank-full.csv"
df = pd.read_csv(data_path, sep=";", usecols=["balance", "day", "month"])

df["year"] = None
tahun_sekarang = 2008
bulan_sebelum = None

for idx, row in df.iterrows():
    bulan_sekarang = row["month"]
    if bulan_sebelum == "dec" and bulan_sekarang == "jan":
        tahun_sekarang += 1
    df.at[idx, "year"] = tahun_sekarang
    bulan_sebelum = bulan_sekarang

mapping_bulan = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
}

df["month"] = df["month"].map(mapping_bulan)
df["date"] = pd.to_datetime(df[["year", "month", "day"]])
df = df.drop(["day", "month", "year"], axis=1)

df["ema_9"] = df["balance"].ewm(span=9, adjust=False).mean()
df["ema_21"] = df["balance"].ewm(span=21, adjust=False).mean()
df["ema_55"] = df["balance"].ewm(span=55, adjust=False).mean()

plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["balance"], color="gray", label="Saldo")
plt.plot(df["date"], df["ema_9"], color="blue", label="EMA 9")
plt.plot(df["date"], df["ema_21"], color="green", label="EMA 21")
plt.plot(df["date"], df["ema_55"], color="red", label="EMA 55")

plt.title("Rerata Tabungan Nasabah (2008-2010)")
plt.xlabel("Tanggal")
plt.ylabel("Saldo")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.show()

'''
Pada kesempatan kali ini saya menggunakan data yang sama dengan tugas sebelumnya. 
Data yang digunakan adalah data rerata tabungan nasabah dari tahun 2008 hingga 2010.
Pada tugas ini saya menambahkan perhitungan EMA (Exponential Moving Average) dengan periode 9, 21, dan 55.
'''
