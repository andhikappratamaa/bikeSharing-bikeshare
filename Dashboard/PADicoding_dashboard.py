import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

bike_sharing = pd.read_csv("bike_sharing.csv")

st.header('Bike sharing Dashboard by Andhika :sparkles:')

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Misalkan bike_sharing adalah DataFrame yang sudah ada sebelumnya

# NO 1
st.subheader('1. Berapa jumlah pelanggan member dan non-member setiap bulan?')

season_data = bike_sharing.groupby('season_daily')['total_count_hourly'].mean()
season_names = ['Spring', 'Summer', 'Fall', 'Winter']

plt.bar(season_names, season_data)
plt.xlabel('Musim')
plt.ylabel('Jumlah Sewa')
plt.title('Analisis Sewa Sepeda Setiap Musim')
st.pyplot()
with st.expander("See explanation"):
    st.write(
        """ Penyewaan paling tinggi terjadi pada musim Fall, sebanyak 1.061.129 
        """
    )

# NO 2
st.subheader('2. Berapa jumlah pelanggan member dan non-member setiap bulan?')

# Analisis jumlah pelanggan member dan non-member setiap bulan
month_data = bike_sharing.groupby(by="month_daily").agg({
    "member_hourly": "sum",
    "nonmember_hourly": ["sum"]
})

# Visualisasi menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(15, 6))

# Visualisasi untuk Member
month_data["member_hourly"]["sum"].plot(kind='bar', color='blue', position=0.4, width=0.3, label='Member', ax=ax)

# Visualisasi untuk Non-member
month_data["nonmember_hourly"]["sum"].plot(kind='bar', color='green', position=-0.4, width=0.3, label='Non-member', ax=ax)

ax.set_title('Jumlah Sewa Sepeda Setiap Bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Pelanggan')
ax.legend()
st.pyplot()
with st.expander("See explanation"):
    st.write(
        """ Berikut adalah statistik jumlah pelanggan setiap bulan
        """
    )

# NO 3
st.subheader('3. Berapa jumlah pelanggan member dan non-member setiap bulan?')

plt.figure(figsize=(4, 7))
sns.boxplot(x="year_daily", y="total_count_hourly", data=bike_sharing)
plt.title("Perbandingan sewa sepeda pada tahun 2011 & 2012")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Sewa Sepeda")
st.pyplot()
with st.expander("See explanation"):
    st.write(
        """ Berikut adalah boxplot dari penyewaan sepeda tahun 2011 dengan 2012, terjadi peningkatan sewa sepeda pada tahun 2012
        """
    )
