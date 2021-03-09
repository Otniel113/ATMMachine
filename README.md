
# ATMMachine
## Deskripsi Singkat
Sebuah proyek dengan membuat program mesin ATM secara Object Oriented

## File dan Kelas
1. atm_card.py berisi Kelas ATMCard
2. customer.py berisi Kelas Customer yang merupakan anak kelas dari ATMCard
3. atm_program.py berisi program utama (driver)

## Overview
Pada awal program, user diminta untuk memasukkan PIN (default = 1234). Jika salah sampai 3 kali, maka program akan keluar.
Setelah user akan memilih fitur-fitur dari menu (yang akan di bahas selanjutnya)

## Fitur-fitur
1. Cek Saldo      = Untuk mengecek saldo sekarang (default = 10000)
2. Debet          = Untuk mengambil uang (mengurangi saldo)
3. Simpan         = Untuk menyimpan uang (menambah saldo)
4. Ganti PIN      = Mengganti PIN default
5. Keluar         = Keluar dari program dan mencetak resi
