# 🛒 Seblak Price Analysis ![Price Analysis Store]("image_represent_dummy.webp") 

Repositori ini berisi mengenai proyek analisis mengenai harga seblak di marketplace di Tokopedia. Data yang kami gunakan merupakan data asli yang kita dapatkan dari scraping website tokopedia 
pada hari tersebut. Proyek ini digunakan sebagai representasi skill dari penulis mengenai skill analisis dan juga metode metode statistik yang akan digunakan nantinya.  

## Daftar Isi 🔗 📥

1. Dataset Source 
2. Project Overview 
3. Latar Belakang Masalah 
4. Problem Statement 
5. Metode yang Digunakan 
6. Kesimpulan Analisa 
7. Rekomendasi 
8. File yang Tersedia 
9. Cara Menggunakan Project Ini
10. Libraries 
11. Author 

## Dataset Source 🏷️

Dataset yang kita gunakan merupakan dataset original langsung scraping dari website tokopedia dan dilakukan scraping pada bulan agustus 2024 [tokopedia_source](https://www.tokopedia.com/search?st=&q=seblak&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=). 

## Project Overview 📈

Proyek ini berfokus pada analisis awal untuk menentukan strategi harga produk seblak di salah satu e-commerce terkemuka di Indonesia. Kami melakukan ekstraksi data langsung dari sumbernya dan menganalisis segmen pasar yang tepat, serta menentukan rentang harga optimal untuk memasuki pasar e-commerce Indonesia. Analisis ini bertujuan memberikan wawasan strategis guna memaksimalkan peluang penjualan produk seblak secara efektif.

## Latar Belakang Masalah 🚧

Kami berencana memasuki pasar e-commerce Indonesia dengan fokus menjual produk seblak. Beberapa aspek penting, seperti segmen pasar, harga seblak yang kompetitif, dan lokasi dasar operasional, masih perlu ditentukan. Pada tahap awal, kami hanya akan memasarkan produk secara online. Namun, memahami kondisi pasar seblak di Indonesia bukanlah hal yang mudah. Oleh karena itu, kami berupaya melakukan analisis mendalam untuk mendapatkan wawasan yang lebih jelas mengenai pasar ini.

## Problem Statement 

METODE STAR

#### SPECIFIC 

Mencetak gross sales memadai untuk jualan kita yang baru mulai untuk memastikan usaha kita tetap berjalan ke depannya

#### MEASURABLE 
Mencetak gross sales sebesar 10 juta dengan jualan seblak online sistem dropshipping. 

#### ACHIEVABLE
Dengan mempertimbangkan posisi kita sebagai penjual online dan produk kita bisa dikirim online untuk seluruh indonesia maka saya yakin goals kita mencetak gross sales 10 juta bisa dicapai

#### RELEVANT
Adanya gross sales 10 juta sangat relevan untuk bisnis kita yang lagi dibangun karena kita harus mencari pelanggan dulu di awal namun juga kita harus membuktikan bahwa jualan kita ini menghasilkan sales untuk keberlangsungan usaha.

#### TIME-BOUND 
Target ini akan direalisasikan dalam waktu 2 bulan dari bulan ini. 

#### Problem Statement 
##### Mencetak Gross Sales sebesar Rp 10 juta dalam waktu 2 bulan untuk memastikan keberlangsungan usaha rintisan (startup) seblak online kita.

## Metode yang Digunakan 💻

Statistik Inferensial 
Statistik Deskriptif 
Visualisasi Data 


## Kesimpulan Analisa ✅

1. Median harga seblak di angka 15000 rupiah sedangkan rata-rata harga jauh di angka 30000. Jadi bisa berasumsi tipikal harga produk seblak itu berada di angka 15000 an. 
2. Median produk terjual di angka 80, namun setelah kita asumsikan data ini normal dan kita melakukan uji test kita bisa mendapatkan hasil bahwa kita yakin dengan derajat signifikan 95% bahwa kita bisa menjual seblak 400 unit per bulan karena rentang produk terjual masih di angka 350 - 540. 
3. Rating rata2 4,4 dan median 4,9. Untuk memastikan bahwa kita mencapai target 10 juta, maka ada target untuk kita untuk mendapat bintang 5 atau mempertahankan 4,9. karena kebanyakan data penjual berkumpul di titik 4,9. 
4. Harga di jabodetabek dan luar jabodetabek berbeda karena kita tinggal di jabodetabek sebaiknya kita fokus untuk menggarap pasar lokal dulu dan mengambil supplier kita dari jabodetabek saja untuk memastikan bahwa layanan kita cepat sampai. 
5. Produk terjual tidak terpengaruh harga sama sekali. Bisa kita mengambil segmen manapun tanpa peduli potensi pasar, karena potensi pasar sama-sama memungkinkan. 

## Rekomendasi 📝

Pengambilan segmen pasar yang lebih premium dikarenakan korelasi antara produk terjual dan harga tidak berkorelasi. Sangat possible untuk mendapatkan 10 juta perbulan gross omset dengan asumsi penjualan kita 400 unit. Lebih baik untuk membuka base penjualan di area jabodetabek. Penggunaan Iklan untuk optimasi dari produk kita dan memberikan eksposure kepada customer mengenai produk-produk yang kita jual di tokopedia. 

## File yang Tersedia 📁

jupyter notebook file berisi mengenai proses analisis dari awal sampai akhir ["Price_Scraping_Seblak.ipynb"]. 

Dataframe bersih ["dataframe_cleaned.csv"] dan dataframe raw ["hasil.csv"] 

apps scrapper file ekstensi .py [scrap.py] 

## Cara Menggunakan Project Ini 🛠️

1. Clone Repositori ini ke dalam lokal anda. 

2. Jalankan file Price_Scrapping_Seblak.ipynb dan ikuti alur analisis data. 

3. Jika anda menginginkan data yang lebih baru bisa untuk dipertimbangkan menjalankan file scrapper dan mendapatkan dataframe baru 


## Libraries 🤖

Pandas Scipy Seaborn Matplotlib

## Author 🧑‍🏫

🌐[Author](https://www.linkedin.com/in/asan133/)