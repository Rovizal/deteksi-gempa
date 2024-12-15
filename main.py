# Aplikasi Gempa Terkini

"""
Tanggal : 12 Desember 2024
Waktu : 13:36:29 WIB
Magnitudo : 4.9
Kedalaman : 10 km
Lokasi : 0.36 LS - 99.51 BT
Pusat Gempa : Pusat gempa berada di laut 57 km barat daya Lubukbasung-Agam
Keterangan : Dirasakan (Skala MMI): III-IV Padang, III-IV Agam, III-IV Padang Pariaman, III-IV Pariaman, II - III Padang Panjang, II - III Bukittinggi
"""

from bs4 import BeautifulSoup
import requests

def ektraksi_data():
    try:
        content = requests.get('https://bmkg.go.id/')
    except Exception:
        return False

    if content.status_code == 200:
        soup = BeautifulSoup(content.text,"html.parser")

        find_waktu  = soup.find("span",{"class":"waktu"})
        find_waktu = find_waktu.text.split(", ")
        waktu = find_waktu[1]
        tanggal = find_waktu[0]

        magnitudos   = soup.find("div",{"class":"col-md-6 col-xs-6 gempabumi-detail no-padding"})
        magnitudo   = magnitudos.findChildren("li")
        ls = 0
        bt = 0
        pusat = None
        keterangan = None
        kedalaman = None
        magnitudos = None
        lokasi = None

        i = 0
        for res in magnitudo:
            if i == 1:
                magnitudos =  res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                lokasi = res.text
            elif i == 4:
                pusat = res.text
            elif i == 5:
                keterangan = res.text
            i += 1
        # lokasi      = soup.find("span",{"class":"ic magnitude"})


        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudos
        hasil['kedalaman'] = kedalaman
        hasil['lokasi'] = lokasi
        hasil['pusat'] = pusat
        hasil[ 'keterangan'] = keterangan
        return hasil



def tampilkan_data(result):
    if result is False:
        print("Data tidak ditemukan")
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Pusat {result['pusat']}")
    print(f"Keterangan  {result['keterangan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ektraksi_data()
    tampilkan_data(result)
    # ektraksi_data()
