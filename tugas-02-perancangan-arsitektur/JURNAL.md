# Jurnal Proses — Tugas 2

## [29 September 2026]
- Opsi arsitektur yang dipertimbangkan: Service-Oriented Architecture (SOA) dan Publish-Subscribe
- Kenapa akhirnya pilih [SOA/Pub-Sub]: kami akhirnya memutuskan memilih untuk menggunakan kedua arsitektur tersebut karana setiap modul memiliki kebutuhan yang berbeda-beda. SOA berfungsi untuk memisahkan fungsi utama FoodGo menjadi beberapa service yang bisa dikembangkan dan dideploy secara mandiri. Sedangkan Publish-service digunakan untuk komunikasi berbasis event secara asynchronous antar-servis.
- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): 

Kondisi Lama (Versi 1):
Seluruh komponen aplikasi FoodGo, yaitu pesanan, pembayaran, katalog resto, serta kurir/notifikasi, masih tergabung dalam satu aplikasi monolitik. Saat terjadi perubahan atau deployment pada satu bagian, bagian lainnya dapat ikut terdampak.

Kondisi Baru (Versi 2 - Kombinasi SOA + Pub-Sub):
Komponen FoodGo dipisahkan menjadi beberapa service yang memiliki fungsi masing-masing, yaitu service katalog resto, service pesanan, service pembayaran, service resto, dan service kurir/notifikasi. Pelanggan berkomunikasi dengan service katalog resto untuk melihat menu dan dengan service pesanan untuk membuat pesanan secara sinkron menggunakan request-response. Selanjutnya, service pesanan berkomunikasi dengan service pembayaran secara sinkron untuk memproses pembayaran dan menerima status pembayaran. Setelah pembayaran berhasil, service pesanan melakukan publish event OrderPaid secara asinkron ke message broker. Event tersebut kemudian diterima oleh service resto dan service kurir/notifikasi melalui mekanisme subscribe secara asinkron. 
Perubahan ini dilakukan karena tidak semua proses dalam FoodGo membutuhkan cara komunikasi yang sama. Pemesanan dan pembayaran membutuhkan respons secara langsung, sedangkan informasi pembayaran yang berhasil perlu diteruskan kepada beberapa service. Oleh karena itu, SOA digunakan untuk memisahkan fungsi FoodGo menjadi beberapa service, sedangkan Publish-Subscribe digunakan untuk menyampaikan event OrderPaid melalui Message Broker tanpa mengharuskan Service Pesanan berkomunikasi secara langsung dengan setiap service penerima.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
