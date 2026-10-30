# Program Sistem_peringatan_gempa_dan_tsunami.py

# Memberikan peringatan kepada warga di sekitar pantai tentang 
# gempa yang baru terjadi untuk berbagai tingkatintensitas gempa serta
# memperkirakan tinggi gelombang tsunami yang akan datang

# Kamus

# opsi, n_data, i = integer
# confirm, back, text, x = string
# reduksi_intensitas_mutlak, magnitudo, reduksi_intensitas_lokal,
# deep, jarak, f = float
# data, data_gempa, data_polos, dampak = list
# menu(), fi(text), olah_data(), peringatan(data), main() = function

# Algoritma

def menu():
    
    while True:

        print("""
        
=========================================================
          Selamat Datang di sistem peringatan gempa dan tsunami!
=========================================================
Silahkan pilih menu dibawah!

1. Kirim notifikasi peringatan gempa dan tsunami

2. Keluar

(Cukup tulis angka menu aja)
=========================================================
""")
    
        opsi = fi("Tulis menu yang ingin anda mau disini: ")

        while opsi != 2 and opsi != 1:

            opsi = fi("Masukkan angka 1 atau 2 untuk mengakses menu! ")

        if opsi == 1:

            print("\n Membuka menu kirim notifikasi peringatan")
            
        else:

            confirm = input("Apakah anda yakin (Ya/Tidak): ")

            if confirm.lower().strip() == "ya":

                print("\nSampai berjumpa lagi")

            else:

                continue
        break
            
    return opsi       
#fungsi untuk menyingkat float(input)    
def fi(text):

    while True:

        try:

            f = float(input(text).replace(",", "."))
            
            if f < 0:

                print("angka tidak boleh negatif!")
                continue

            break

        except ValueError:

            print("Masukkan nilai yang valid")
    
    return f

def olah_data():

    data = [0, 0, 0, 0, 0, 0, 0, 0]
    # data 1 = bool tsunami, data 2 = state gempa, data 3 = kedalaman <=80
    # data 4 = nilai m, data 5 = nilai run-up ,data 6 = magnitudo prediksi, data 7 = Tipe Tsunami, data 8 = nilai maks dari magnitudo real
    dampak = ["Gempa lemah", "Gempa menengah", "Gempa kuat", "Gempa besar", "Gempa sangat besar"]
    data_gempa = []
    data_polos = []

    while True:

        n_data = fi("\nAda berapa data realtime intensitas gempa(SR) yang dimiliki: ")

        if n_data % 1 != 0:

            print("\nMasukkan bilangan bulat saja!")
            continue

        else:

            break

    if n_data // 1 == 0:

        confirm = str(input("""\napakah anda yakin tidak ada data yang dimiliki(ya/tidak)
(menjawab "tidak" atau selain ya akan mengembalikan anda ke menu): """))

        if confirm.lower().strip() == "ya":

            print("\nSelamat tinggal")
            return "keluar"

        else:

            print("\nmengembalikan anda menu awal")
            return "ulang"

    reduksi_intensitas_mutlak = fi("\nBerapa faktor reduksi intensitas mutlak(SR) di tempat yang ingin diperingatkan: ")

    for i in range(int(n_data//1)):
            
            magnitude = fi(f"\nberapa besar gempa yang terjadi(SR) di lokasi {i+1}: ")
            reduksi_intensitas_lokal = fi(f"\nBerapa besar faktor reduksi intensitas di tempat pengambilan data {i+1}: ")
            data_polos.append(round(magnitude, 7))
            data_gempa.append(round(magnitude-reduksi_intensitas_lokal, 7))

    data[7] = max(data_polos)

    if data[7] == 0:

        return data 

    magnitude = round(max(data_gempa) + reduksi_intensitas_mutlak, 7)

    if magnitude <= 0:

        magnitude = 0
        data[5] = round(magnitude, 7)
        return data
    
    data[5] = round(magnitude, 7)
    
    deep = fi("\nberapa kedalaman gempanya (Km): ")

    if magnitude < 4:

        data[1] = dampak[0]

    elif 4 <= magnitude <5.4:

        data[1]= dampak[1]

    elif 5.4 <= magnitude < 6.9:

        data[1]= dampak[2]
        data[2]= 1

    elif 6.9 <= magnitude < 7.9:

        data[1]= dampak[3]
        data[2]=1

    else:

        data[1]= dampak[4]
        data[2]=1

    if data[2]==1 and deep<=80:

        data[0]=1
        #Mencari Imamura
        data[3] = round(2.661*magnitude-16.44, 7)

        if data[3] <= -1:

            data[4] = "< 0.5 m"

        elif data[3] <= 0:

            data[4] = "1 m"

        elif data[3] <=1:

            data[4] = "2 m"

        elif data[3] <=2:

            data[4] = "4-6 m"

        elif data[3] <= 3:

            data[4] = "10-30 m"

        else:

            data[4] = "> 30 m"

        jarak = fi("\nBerapa jarak data diperoleh dengan pusat gempa(Km): ")

        if jarak> 1000:

            data[6] = "Tsunami Jarak Jauh"

        else:

            data[6] = "Tsunami lokal"

        

    return data

def peringatan(data):

    if data[7] == 0:

        print("\nTidak ada gempa (baik fisik maupun dari data) yang menunjukkan adanya tanda-tanda gempa")

    else:

        if data[0] == 1:

            print(f"""\nPeringatan! Telah terjadi {data[1]} dengan intensitas sebesar {data[5]} SR dan potensi {data[6]} dengan Run-up sekitar {data[4]}.
Mohon untuk ikuti instruksi ahli dan jangan panik!""")

        elif data[0]== 0:

            if data[5] >= 4 :

                print(f"""\nPeringatan! Telah terjadi {data[1]} dengan intensitas sebesar {data[5]} SR.
Mohon untuk jangan panik dan berlindung di tempat aman""")
                
            elif data[5]==0:

                print("\nTidak ada gempa fisik yang terdeteksi, tetapi ada data seismik yang mendeteksi gelombang gempa. ")
    
            else:

                print(f"""\nPeringatan! Telah terjadi {data[1]} dengan intensitas sebesar {data[5]} SR.
Mohon untuk jangan panik dan lanjutkan aktivitas""")
       
def main():

    while True:

        if menu()==1:

            x = olah_data()

            if x == "keluar":

                break

            elif x == "ulang":

                continue

            peringatan(x)
            back = input("Ingin kembali ke menu awal(Ya/Tidak)? ")

            if back.strip().lower() == "ya":

                continue

            else:

                print("Selamat tinggal")
                break
  
        else:

            break
        
if __name__ == "__main__":

    main()