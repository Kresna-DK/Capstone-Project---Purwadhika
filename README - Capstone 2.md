LINK TABLEAU PUBLIC:

https://public.tableau.com/app/profile/kresna.kumbara/viz/SupermarketDemographicTrendAnalysis/DB0-Demographics

CAPSTONE 2 - SUPERMARKET DEMOGRAPHIC AND PRODUCT ANALYSIS

Didalam analisa data set supermarket ini, saya berusaha untuk menunjukan dan membagi jenis-jenis demografi pelanggan yang mungkin berdampak pada pembelian produk dan sukses kampanye yang diberlakukan oleh supermarket ini.

- Evaluasi Data
Pertama saya melakukan evaluasi dataset untuk melihat tipe data dan apakah ada data yang tidak memiliki nilai (value), proses yang saya gunakan adalah fungsi .info() untuk melihat jenis data dan fungsi .isna() dan matrix missingno untuk visualisasi data yang tidak memiliki nilai. Lalu saya menggunakan funsi .duplicated() untuk melihat apakah ada data yang memiliki nilai yang duplikat dan juga menggunakan .describe() untuk melihat info nilai angka didalam dataset tersebut.

- Pembersihan Data
Lalu saya membuat list proses yang akan saya lakukan untuk membersihkan dataset tersebut, yaitu mengganti tipe data menjadi tipe yang sesuai (tanggal menjadi Datetime), membersihkan nilai diluar trend (outliers), menghapus kolom yang memiliki nilai yang sama di setiap barisnya (.drop()) dan membuat kelompok dari beberapa kolom agar data tersebut dapat di kategorikan.

- Analisa Data
1. Setelah itu saya melakukan data analisis untuk melihat korelasi diantara beberapa faktor penting didalam dataset tersebut, saya menggunakan pendapatan, umur, status dan edukasi pelanggan sebagai nilai untuk mendefinisikan demografi paling banyak dari data pelanggan yang ada.

2. Kegunaan analisa produk yang saya lakukan adalah untuk melihat produk apa yang paling populer dan produk apa yang tidak terlalu laku. Dari data tersebut saya juga dapat membuat kategori demografi yang condong membeli produk tersebut.

3. Hal terakhir yang saya analisa adalah bagaimana respon para pelanggan terhadap kampanye (promosi) yang sudah dilakukan oleh supermarket ini dan demografi yang memiliki respon terbaik.

- Konklusi dan Rekomendasi
Untuk penutup saya juga memberi beberapa langkah yang bisa dilakukan oleh supermarket ini untuk meningkatkan jumlah respon pada kampanye yang akan datang, kemungkinan untuk meningkatkan pembelian produk tertentu dengan cara fokus ke demografi yang lebih spesifik atau berusaha mendapatkan pembelian dari demografi lain.
