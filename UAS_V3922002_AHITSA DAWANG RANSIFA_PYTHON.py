#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests # Digunakan untuk mengirim permintaan HTTP ke halaman web.
from bs4 import BeautifulSoup # Digunakan untuk mem-parsing dokumen HTML. 
import csv # Digunakan untuk membaca dan menulis data dalam format CSV

web_url = 'https://www.bukalapak.com/c/perawatan-kecantikan/alat-kecantikan?page' # Menyimpan link web bukalapak yang akan discraping ke variabel.


data = []  # List kosong untuk menyimpan data produk.

for page in range(1, 6): # Melakukan perulangan untuk scraping pada halaman 1 hingga 5.
    url = web_url + str(page)  # Digunakan untuk menggabungkan URL dasar dengan nomor halaman yang sedang diproses.
    req = requests.get(url)  # Digunakan untuk mengirim permintaan HTTP GET ke URL bukalapak.
    soup = BeautifulSoup(req.text, 'html.parser')  # Digunakan untuk membuat objek dari konten HTML yang diperoleh dari respons HTTP menggunakan parser HTML bawaan.
    product_items = soup.find_all('div', {'class': 'bl-product-card'})  # Digunakan untuk mencari semua elemen dalam halaman web yang memiliki tag <div> dan class 'bl-product-card'.
    
    for item in product_items: # Melakukan perulangan untuk mengambil masing-masing item yng telah dicari di variabel product_items.
        
        # Mengambil nama, alamat, harga, dan rating produk dari elemen-elemen yang ditemukan.
        name = item.find('a', {'class': 'bl-link'}).text.strip() # Digunakan untuk mengekstrak teks dari elemen <a> yang memiliki class 'bl-link'.
        address = item.find('span', {'class': 'mr-4 bl-product-card__location bl-text bl-text--body-14 bl-text--subdued bl-text--ellipsis__1'}).text.strip() # Digunakan untuk mengekstrak teks dari elemen <span> yang memiliki class yang spesifik dalam suatu elemen item.
        price = item.find('p', {'class': 'bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1'}).text.strip() # Digunakan untuk mengekstrak teks dari elemen <p> yang memiliki class yang spesifik dalam suatu elemen item.
        rating = item.find('p', {'class': 'bl-text bl-text--body-14 bl-text--subdued'}).text.strip() # Digunakan untuk mengekstrak teks dari elemen <p> yang memiliki class yang spesifik dalam suatu elemen item.
        data.append([name, address, price, rating])  # Menyimpan data dalam list data.
        
csv_file = 'data_alatkecantikan.csv'  # Deklarasi nama file CSV untuk menyimpan data.

with open(csv_file, 'w', newline='', encoding='utf-8') as file: # Membuka file csv_file dengan mode write ('w') untuk menulis data.
    writer = csv.writer(file) # Digunakan untuk membuat objek penulis (writer) dari modul CSV yang akan digunakan untuk menulis data ke dalam file CSV.
    writer.writerow(['Name', 'Address', 'Price', 'Rating'])  # Digunakan untuk menulis baris header ke dalam file CSV.
    writer.writerows(data)  # Digunakan untuk menulis multiple baris data ke dalam file CSV yang sedang dibuka.


# In[26]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_alatkecantikan.csv')

# Histogram
plt.figure(figsize=(11, 6))
plt.hist(data['Price'], bins=10, edgecolor='black')
plt.title('Histogram Distribusi Harga Alat Kecantikan')
plt.xlabel('Harga (IDR)')
plt.ylabel('Frekuensi')
plt.tight_layout()
plt.savefig('Histogram_alatkecantikkan_uas.jpg', dpi=300, bbox_inches='tight')
plt.show()


# In[29]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_alatkecantikan.csv')

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(data['Rating'].value_counts(), labels=data['Rating'].unique(), autopct='%1.1f%%')
plt.title('Pie Chart Distribusi Rating Alat Kecantikan')
plt.axis('equal')
plt.tight_layout()
plt.savefig('piechart_alatkecantikkan_uas.jpg', dpi=300, bbox_inches='tight')
plt.show()


# In[30]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_alatkecantikan.csv')

# Bar Chart
plt.figure(figsize=(12, 7))
plt.bar(data['Name'], data['Price'])
plt.title('Bar Chart Harga Alat Kecantikan')
plt.xlabel('Nama')
plt.ylabel('Harga (IDR)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Barchart_alatkecantikkan_uas.jpg', dpi=300, bbox_inches='tight')
plt.show()


# In[ ]:




