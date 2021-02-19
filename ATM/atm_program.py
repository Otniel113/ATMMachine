import random
import datetime
from customer import Customer


atm = Customer(id) #Membuat Objek dari kelas Customer

while True: #Perulangan sebagai program utama
    id = int(input('Masukkan nomor PIN : '))
    attempt = 0

    while (id != atm.getCustPin()) and (attempt < 3):   #Perulangan untuk konfirmasi PIN 
        id = int(input('Pin salah, tolong masukkan nomor PIN yang benar : '))
        attempt += 1

        if attempt >= 3:    #Berhenti jika salah memasukkan PIN sebanyak >= 3
            print('Error, karena telah salah memasukan PIN sebanyak 3 kali')
            exit()

    while True: #Perulangan untuk menu
        print('\n========Selamat datang di ATM Bersama (jrenggg)========')
        print('Silakan pilih menu : ')
        print('1. Cek Saldo')
        print('2. Debet')
        print('3. Simpan')
        print('4. Ganti PIN')
        print('5. Keluar')
        pil = int(input('Silakan masukkan pilihan Anda : '))

        if pil == 1 :
            print('\nAnda memilih menu Cek Saldo')
            print('Saldo Anda adalah : Rp.' + str(atm.getCustBalance()))    #Print Saldo

        elif pil == 2:
            print('\nAnda memilih menu Debet')
            nominal = int(input('Masukkan banyaknya yang ingin diambil : Rp.'))
            verif = input('Apakah Anda yakin akan mengambil uang sebanyak Rp.' + str(nominal) + ' ? y/n \n')

            if verif == 'y':    #konfirmasi
                print('Saldo awal Anda adalah : Rp.' + str(atm.getCustBalance()))
            else:
                print('Masukan karakter yang valid!')
                break

            if nominal <= atm.getCustBalance(): #Hanya bisa diambil jika nominal lebih kecil sama dgn saldo
                atm.debet(nominal)
                print('Transaksi berhasil!')
                print('Sisa saldo Anda sekarang adalah : Rp.' + str(atm.getCustBalance()))
            else:   #Saldo tidak mencukupi
                print('Maaf, saldo Anda tidak mencukupi')

        elif pil == 3:
            print('\nAnda memilih menu Simpan')
            nominal = int(input('Masukkan banyaknya yang ingin disimpan : Rp.'))
            verif = input('Apakah Anda yakin akan menyimpan uang sebanyak Rp.' + str(nominal) + ' ? y/n \n')

            if verif == 'y':    #konfirmasi
                print('Saldo awal Anda adalah : Rp.' + str(atm.getCustBalance()))
                atm.simpan(nominal)
                print('Sisa saldo Anda sekarang adalah : Rp.' + str(atm.getCustBalance()))
            else:
                print('Masukan karakter yang valid!')
                break

        elif pil == 4:
            print('\nAnda memilih menu Ganti PIN')
            pin_lama = int(input('Maukkan nomor PIN yang lama : '))

            while pin_lama != atm.getCustPin():     #Cek PIN yang diinput sama dengan PIN sekarang
                pin_lama = int(input('PIN Anda salah, silakan masukkan PIN lagi :'))
                
            pin_baru = int(input('Silakan masukkan PIN baru : '))
            print('PIN berhasil diubah')
            verif_pinBaru = int(input('Silakan konfirmasi lagi PIN yang baru : '))

            while verif_pinBaru != pin_baru:        #Cek verifikasi PIN baru apakah sama dengan PIN baru
                verif_pinBaru = int(input('PIN salah, silakan konfirmasi lagi PIN yang baru : '))

            atm.custPin = pin_baru
            print('PIN telah berhasil dikonfirmasi')

        elif pil == 5:
            print('\nResi tercetak secara otomatis')
            print('Harap simpan tanda terima ini sebagai bukti transaksi yang sah')
            print('Nomor Rekord: ' + str(random.randint(100000, 1000000)))
            print('Tanggal : ' + str(datetime.datetime.now()))
            print('Saldo Anda : Rp.' + str(atm.getCustBalance()))
            print('Terimakasih telah menggunakan ATM Bersama')
            exit()
        else:
            print('\nTolong masukkan angka yang valid!')