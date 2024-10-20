from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd 

# list kosong untuk menampung hasil scraping setiap value
nama_barang= []
harga_barang= []
nama_toko = []
kota_toko = []
terjual = []
rating_toko = []

# pambuatan dataframe untuk nampung hasil 
df=pd.DataFrame()
#instance Driver

driver = webdriver.Chrome()





for i in range(1,11):
    # nunjukin akan ngambil data dari link mana
    url="https://www.tokopedia.com/search?page={}&q=seblak&search_id=202408230011197B9C09C920D16A129YHT&source=universe&srp_component_id=02.07.01.01&st=product".format(i)
    #nyuruh driver untuk akses tautannya
    driver.get(url)
    sleep(3)


    for scroll in range(15):
        driver.execute_script("window.scrollBy(0,350)") #sekali scroll 350 pixel
        sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #nama_produk
    for i in soup.find_all('div',{"class":"css-5wh65g"}):
        elemen1 = i.find('div',{"class":"VKNwBTYQmj8+cxNrCQBD6g=="}) 
        if elemen1 == None : 
            nama_barang.append(None)
        else : 
            text = elemen1.get_text().strip()
            if text == '':
                nama_barang.append(None)
            else:
                nama_barang.append(text)
    
    #harga barang
    for i in soup.find_all('div',{"class":"css-5wh65g"}):
        elemen1 = i.find ('div',{"class":"ELhJqP-Bfiud3i5eBR8NWg=="}) 
        if elemen1 == None : 
            harga_barang.append(None)
        else : 
            text = elemen1.get_text().strip()
            if text == '':
                harga_barang.append(None)
            else:
                harga_barang.append(text) 
    
    # nama toko
    for i in soup.find_all('div',{"class":"css-5wh65g"}):
        elemen1 =  i.find('span',{"class":"X6c-fdwuofj6zGvLKVUaNQ== -9tiTbQgmU1vCjykywQqvA== flip"}) 
        if elemen1 == None : 
            nama_toko.append(None)
        else : 
            text = elemen1.get_text().strip()
            if text == '':
                nama_toko.append(None)
            else:
                nama_toko.append(text) 

    #kota toko

    for i in soup.find_all('div',{"class":"css-5wh65g"}):
        elemen1 = i.find ('span',{"class":"-9tiTbQgmU1vCjykywQqvA== flip"}) 
        if elemen1 == None : 
            kota_toko.append(None)
        else : 
            text = elemen1.get_text().strip()
            if text == '':
                kota_toko.append(None)
            else:
                kota_toko.append(text) 

    # jumlah terjual 

    for i in soup.find_all('div',{"class":"css-5wh65g"}):
        sold = i.find('span',{"class":"eLOomHl6J3IWAcdRU8M08A=="})  
        if sold is None:
            terjual.append(None)
        else:
            text = sold.get_text().strip()
            # Jika teks kosong, tambahkan '0'
            if text == '':
                terjual.append(None)
            else:
                terjual.append(text)

    #rating toko
    
    for i in soup.find_all('div', {"class": "css-5wh65g"}):
    # Cari elemen dengan class tertentu di dalam setiap kontainer
        rating_elem = i.find('span', {"class": "nBBbPk9MrELbIUbobepKbQ=="})
        
        # Jika elemen tidak ditemukan, tambahkan '0'
        if rating_elem is None:
            rating_toko.append(None)
        else:
            text = rating_elem.get_text().strip()
            # Jika teks kosong, tambahkan '0'
            if text == '':
                rating_toko.append(None)
            else:
                rating_toko.append(text)

        
df['nama_produk'] = nama_barang
df['harga']= harga_barang
df['nama_toko'] = nama_toko
df['kota'] =kota_toko
df['terjual'] = terjual
df['rating'] = rating_toko


df.to_csv("hasil.csv",index=False)




#kerangka htmlnya disimpan dalam variabel html namun masih sebaris



