# 📊 Visualisasi Data Marketing ![Tableau Logo](https://img.icons8.com/color/48/000000/tableau-software.png) - [TABLEAU](https://www.tableau.com/)

Repositori ini berisi mengenai proyek analisis menggunakan python serta penggunaan tableau sebagai alat bantu untuk visualisasi. Proyek ini bertujuan untuk mengeksplorasi suatu data kemudian memberikan analisis mengenai data yang sedang dilakukan analisis dan pada akhirnya akan divisualisasikan menggunakan tableau. Repositori ini mencakup file Jupyter Notebook yang menjelaskan proses secara menyeluruh, mulai dari eksplorasi data hingga menghasilkan visualisasi yang informatif.

## Daftar Isi 🔗 📥

1. Link Terkait Project
2. Project Overview
3. Latar Belakang Masalah
4. Problem Statement
5. Penjabaran Masalah
6. Metode yang Digunakan
7. Kesimpulan Analisa
8. Rekomendasi
9. File yang Tersedia
10. Cara Menggunakan Projek Ini
11. Libraries
12. Author


## Link Terkait Project 📁
[DataSet Link](https://www.kaggle.com/datasets/ahsan81/superstore-marketing-campaign-dataset?select=superstore_data.csv)

[Dashboard Visualization](https://public.tableau.com/app/profile/maulana.achsan/viz/MarketingDataProject/Dashboard3#2)

## Project Overview 📝

Data adalah salah satu alat terbaik untuk membuat keputusan yang tepat. Pada proyek ini, kami bertujuan untuk menganalisis data dari tim marketing, mengekstraksi insight yang berharga serta memberikan panduan yang dapat membantu menentukan langkah strategis mereka ke depan. Langkah-langkah utama yang akan kami lakukan meliputi:
1. Mengimpor library dan mengeksplorasi dataset.
2. Memvisualisasikan data agar dapat diinterpretasikan dengan jelas.
3. Menganalisis hasil visualisasi untuk memberikan rekomendasi dan tindakan strategis bagi tim marketing ke depannya.

## Latar Belakang Masalah 🔍

Sebagai perusahaan supermarket yang berada di jerman. Perusahaan ini mempunyai nilai pasar sebesar 100 Miliar Euro. Posisi perusahaan ini di market adalah market follower yang artinya berada di papan tengah dari klasemen persaingan pasar supermarket. Perusahaan ini sering melakukan strategi mempertahankan pasar dengan adanya diskon dan penawaran iklan menarik  lainnya. Karena perusahaan ini berada di tengah pasar perusahaan berusaha untuk melakukan kampanye iklan yang tidak melebihi budget sekaligus efektif dan efisien. 

Tahun lalu perusahaan telah melakukan kampanye iklan diskon akhir tahun. Data dari tahun lalu berhasil disimpan sangat baik oleh perusahaan dan kali ini saya mendapatkan data random sampling dari data kampanye iklan tahun lalu. Perusahaan memberi instruksi kepada saya selaku data analyst didalam perusahaan tersebut untuk menganalisis data dari kampanye iklan tahun lalu tersebut. 

## Problem Statement 💭

SPECIFIC : Menaikkan response rate iklan perusahaan untuk marketing campaign yang berupa diskon akhir tahun. 

MEASURABLE : Menaikkan response rate sebesar 15%. 

ACHIEVABLE : Dengan pertimbangan kita sebagai market follower,sumber daya yang dimiliki dan data iklan tahun lalu yang kita miliki maka kita optimis bisa menaikkan response rate sebesar 15%. 

RELEVANT : Dengan kenaikan response rate iklan ini diharapkan akan memperkuat posisi kita di pasar serta juga memanfaatkan momentum akhir tahun untuk mendapatkan eksposure dan menambah penjualan kita di tahun ini.

TIME-BOUND : Program kampanye iklan ini akan dilakukan dimulai awal 10 desember dan berakhir 31 desember. 

Problem Statement : Menaikkan response rate iklan diskon akhir tahun dari supermarket Indoapril sebesar 15% dengan waktu sampai akhir tahun untuk memperkokoh posisi kita dalam pasar dan menambah penjualan di tahun ini. 

## Penjabaran Masalah 

1.  Berapa persentase response rate tahun lalu? >>> (Visualisasi)
2.  Apakah income class dibawah dari median income class lebih sering merespon iklan kita? >>> (Visualisasi)
3.  Generasi mana yang memiliki respon paling banyak? >>> (Visualisasi)
4.  Apakah rata-rata orang dengan kepemilikan gelar cenderung memiliki respon rate rendah terhadap iklan kita? >>> (Visualisasi)
5.  Bagaimana rata-rata respon iklan terhadap orang-orang sudah menikah atau hidup bersama pasangan ?  apakah mereka cenderung lebih sering melakukan response terhadap iklan kita? >>> (Visualisasi) 
6.  Adakah korelasi antara jumlah anak dengan respon iklan ? Sebagai pertimbangan dengan orang yang mempunyai anak maka biaya hidup lebih besar dan itu akan membuat mereka cenderung untuk merespon iklan iklan dari kita ? >>> (Deskriptif)
7.  Apakah ada perbedaan rata 2 response rate iklan terhadap golongan orang2 yang mempunyai recency <= 10 dan diatas 10  ? Jadi kita akan melakukan testing untuk membuktikan secara statistik bagaimana perbedaan respon iklan terhadap terakhir pembelian user di supermarket itu? >>>(Inferensial) 
8. Bagaimana total proporsi penjualan produk per bulan ? Produk mana yang berhasil terjual paling banyak ? 
9. Dimana customer banyak membeli produk kita ? 

## Metode yang Digunakan 

1. Statistik Inferensial
2. Statistik Deskriptif
3. Visualisasi Data

## Kesimpulan Analisa 

1. Response rate tahun lalu 15%.
2. Median dari income adalah 50000 euro per tahun. 
3. Gen X menjadi orang-orang yang memiliki reponse rate tertinggi dibandingkan yang lainnya. 
4. Orang dengan gelar cenderung memiliki responsifitas terhadap diskon akhir tahun lalu
5. Orang single mempunyai response rate terhadap iklan lebih tinggi dibanding yang berkeluarga dan memiliki pasangan. 
6. Tidak ada korelasi antara punya anak dan response rate
7. Recency Rate rendah atau sering ke supermarket akan merespon dengan baik diskon akhir tahun. 
8. Perlunya fokus untuk melakukan marketing kepada segmen wine dan segmen daging 
9. Penjualan Store dan penjualan melalui web mendapatkan lebih dari 60% dari total penjualan. 

## Rekomendasi 

### Insight

Untuk Pemilihan produk diskon maka kita memerlukan pertimbangan generasi dari pelanggan kita dahulu. Setelah itu kita harus menampilkan konten iklan kita cenderung konten-konten untuk orang berpendidikan mulai dari visualnya dan kemudian aktor atau figur gambarnya. Setelah itu coba pilih segmen segmen produk yang menengah ke atas karena yang merespon diskon adalah orang dengan income rate diatas median. Jangan terlalu diskon produk-produk murah yang mempunyai segmen orang dengan pasar segmen menengah ke bawah. Dengan ini kita akan mendapatkan kesesuaian antara produk dan target market yang cocok. 
Lebih baik kita fokuskan diskon kepada pelanggan pelanggan yang memiliki recency rate dibawah 10 dibandingkan pelanggan yang memiliki recency di atas 10. Sudah terbukti diskon kita di akhir tahun lebih terespon kepada orang-orang yang memiliki recency rate yang rendah. 
Memberikan diskon atau marketing campaign kepada segmen tertentu yang lebih besar misalkan daging dan wine. Diharapkan dengan ini maka orang-orang akan aware dengan adanya diskon yang tinggi sehingga akan ada kenaikan dari response rate iklan kita. Kita perlu juga fokus kepada store dan website untuk melakukan kampanye nanti, meskipun tidak dipungkiri deals yang terjual dan katalog memberikan 40% total penjualan juga.  


## File yang Tersedia 

Profiling_Customer_Segment.ipynb >> Proses Analisis menggunakan Python 

maulana_achsan_df.csv  >> data yang bersih 

superstore_data.csv >> raw data

## Cara Menggunakan Projek Ini

1. Clone repositori ini ke dalam lokal Anda
2. Jalankan Jupyter Notebook untuk mengikuti alur analisis data
3. Tableau digunakan sebagai alat utama untuk membuat visualisasi, bisa dilihat melalui website atau aplikasi.
 
## Libraries

Pandas
Scipy
Seaborn 
Matplotlib

## Author

[Author](https://www.linkedin.com/in/asan133/)


