Sistem rental mobil - Kresna Dewa Kumbara

Dalam program ini terdapat 6 Menu yang menggunakan sistem CRUD di Python.

1. Menu daftar mobil akan membaca data dari database (dictonary) dan mencetak data
   tersebut. Di menu tersebut saya memberi 2 pilihan, yaitu cetak data secara keseluruhan 
   atau dengan dicari oleh sebuah primary key (Plat No. Mobil)
   (V2 : Data dapat disortir sesuai Tahun, Kapasitas dan Biaya)

3. Menu sewa mobil akan membaca data dengan parameter tertentu yaitu: apakah
   saat ini mobil sedang dipakai atau tidak, yang ditunjukan di kolom 'Status'.
   Di menu ini, user dapat menyewa mobil dengan memberi 3 input, yaitu Plat No. Mobil,
   Tanggal sewa dan Jaminan. Jika input user sesuai dengan seluruh parameter yang sudah
   ditetapkan, maka proses sewa mobil akan sukses.

4. Hampir sama dengan menu sewa mobil, Menu pengembalian mobil bekerja sebaliknya, dimana
   parameter yang ditetapkan adalah Status mobil saat ini sedang dipakai. Karena pengembalian
   dibaca secara realtime, maka tidak ada input yang harus diberikan, selain konfirmasi.
   (V2 : Penambahan menu pembayaran untuk dapat mengembalikan mobil dengan sukses)

5. Menu tambah mobil adalah bagian Create dari sistem CRUD, dimana user dapat menambah
   mobil-mobil baru dengan memberi input yang sesuai. Input yang dibutuhkan untuk menu
   ini adalah 'Brand', 'Jenis', 'Tahun', 'Plat No.', 'Kapasitas'. Status mobil pada saat
   dibuat akan menjadi 'Tersedia' secara otomatis.

6. Menu update mobil berfungsi untuk merubah data yang sudah ada di database. Seluruh data
   yang ada diprogram dapat Update, jika user memberi input sesuai parameter. Seperti: untuk
   Update 'Plat No.' user harus memberi input dengan parameter 2 character diawal harus berupa
   alphabet dan di split dengan spasi, lalu dilanjutkan dengan 4 character yang bersifat angka
   dan akhirnya 3 character akhir yang harus berupa alphabet. Disetiap prompt akan ada contoh
   yang dapat diikuti oleh user.

7. Menu hapus mobil digunakan untuk menghapus data sebuah mobil secara keseluruhan, berbeda
   dengan menu update dimana kita secara tidak langsung menghapus dan memberi data baru,
   di menu ini data mobil, seperti 'Status', 'Jenis', 'Plat No.' akan hilang sesuai dengan
   mobil yang dipilih.

Dengan itu saya harap penjelasan ini cukup untuk membantu user menggunakan program ini.

Terima kasih,

Kresna Dewa Kumbara - JCDS 2302 004
    
