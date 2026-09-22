# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [Self Reward]

| Nama | NIM | Kontribusi |
|---|---|---|
| [Chartika Jenyansa Pangaribuan] | [103072400026] | [Latency Is Zero] |
| [Alexandria Febrianti Krisna Putri] | [103072400086] | [Single Point of Failure (SPOF)] |
| [Nur Aisyah Luhur Pambudi] | [103072430015] | [The Network is Reliable] |

## Pitfall 1: [Latency Is Zero] — ditulis oleh [Chartika Jenyansa Pangaribuan]

**Bukti di skenario:** [modul pesanan memanggil modul pembayaran dan menunggu respon tanpa adanya batas waktu (timeout) sehingga mengakibatkan sistem aplikasi menjadi lambat."]

**Kenapa ini keliru:** [Komunikasi antar modul melalui jaringan tidak berjalan dengan lancar dan cepat. Ketika banyak pengguna yang melakukan pemesanan secara bersamaan maka modul pembayaran akan membutuhkan waktu yang lama untuk memproses pembayaran dan modul pesanan akan terus menunggu sampai mendapatkan respon dari modul pembayaran, karena tidak adanya timeout.]

**Dampak ke FoodGo:** [Saat modul pembayaran terhambat karena menunggu respon, modul pesanan juga akan ikut terhambat dengan permintaan yang terus bertambah. Hal tersebuut mengakibatkan sistem menjadi semakin lambat dan mengalami timeout.]

**Solusi desain awal:** [Menggunakan sistem asynchronous dimana modul pesanan tidak perlu membuat pengguna menunggu seluruh proses selesai, pesanan dapat dicatat terlebih dahulu dan mengirimkan informasi bahwa pembayaran perlu diproses dan modul pembayaran dapat langsung memproses pembayaran.]

**Trade-off:** [Penerapan sistem asynchronous membuat pengguna tidak selalu mendapatkan hasil pembayaran secara langsung. Status pesanan bisa saja awalnya masih "menunggu pembayaran" dan baru berubah setelah proses pembayaran berhasil. Selain itu, sistem menjadi lebih kompleks karena harus menangani pesanan yang terlambat, gagal, atau diproses tidak berurutan.]

---

## Pitfall 2: Single Point of Failure (SPOF) — ditulis oleh [Alexandria Febrianti Krisna Putri]

**Bukti di skenario:** Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama.

**Kenapa ini keliru:** Karena semua modul bergantung pada satu server dan satu proses, ketika server mengalami kelebihan beban, semua modul dapat ikut terganggu. Hal ini membuat sistem sulit menangani lonjakan pesanan.

**Dampak ke FoodGo:** Saat pesanan meningkat, semua modul menggunakan server yang sama. Akibatnya, aplikasi menjadi lambat dan server bisa crash. Jika server crash, semua modul juga ikut berhenti sampai server di-restart.

**Solusi desain awal:** Solusinya FoodGo dapat menggunakan load balancing untuk membagi permintaan pengguna ke beberapa server. Jadi, beban tidak hanya ditanggung oleh satu server sehingga sistem dapat menangani peningkatan trafik dengan lebih baik.

**Trade-off:** Load balancing membutuhkan server tambahan dan pengaturan lebih, sehingga biaya dan pengelolaannya juga bertambah.

---

## Pitfall 3: The Network is Reliable — ditulis oleh Nur Aisyah Luhur Pambudi

**Bukti di skenario:** Jaringan komputer pada sistem terdistribusi bersifat nondeterministic (tidak selalu dapat diprediksi). Sementara itu, FoodGo menganggap jaringan selalu dapat diandalkan. Padahal, komunikasi antar-service dapat mengalami berbagai kegagalan, seperti packet loss, respons tidak sampai, _connection failure_, atau koneksi yang terputus. Oleh karena itu, sistem terdistribusi perlu dirancang agar tetap dapat menangani kemungkinan terjadinya kegagalan komunikasi.

**Kenapa ini keliru:** Jaringan komputer pada sistem terdistribusi bersifat nondeterministic (tidak selalu dapat diprediksi). Sementara itu, FoodGo menganggap jaringan selalu dapat diandalkan. Padahal, komunikasi antar-service dapat mengalami berbagai kegagalan, seperti packet loss, respons tidak sampai, _connection failure_, atau koneksi yang terputus. Oleh karena itu, sistem terdistribusi perlu dirancang agar tetap dapat menangani kemungkinan terjadinya kegagalan komunikasi.

**Dampak ke FoodGo:** Saat komunikasi dari modul pesanan ke modul pembayaran mengalami kegagalan, mekanisme FoodGo tidak melakukan _retry_. Akibatnya, proses pembayaran tidak dapat dilanjutkan dan proses pesanan ikut terganggu.

**Solusi desain awal:** 
1. _Retry_
    - Menggunakan _retry_ agar sistem dapat melakukan percobaan ulang ketika komunikasi antar-service gagal. Misalnya, ketika request dari modul pesanan ke modul pembayaran gagal karena gangguan jaringan, sistem dapat mencoba mengirimkan request tersebut kembali.
2. _Exponential backoff_
    - Menggunakan _exponential backoff_ untuk memberikan jeda di antara setiap percobaan _retry_. Jeda dapat dibuat semakin panjang pada setiap percobaan sehingga sistem tidak terus-menerus mengirim request ke service yang sedang mengalami gangguan dan menambah bebannya.
3. Membatasi jumlah _retry_
    - Menentukan batas maksimal _retry_, misalnya tiga kali percobaan. Dengan demikian, sistem tidak melakukan percobaan ulang tanpa batas dan _retry_ dapat difokuskan pada kemungkinan kegagalan sementara, seperti gangguan jaringan. Tidak semua jenis error perlu di-_retry_.
4. _Circuit breaker_
    - Jika Payment Service benar-benar mengalami gangguan dan banyak request terus gagal, _circuit breaker_ dapat digunakan untuk menghentikan sementara pengiriman request ke service tersebut. Request baru tidak langsung diteruskan sampai kondisi service membaik, sehingga kegagalan berulang tidak semakin membebani sistem.
5. _Idempotency_
    - _Retry_ pada proses pembayaran perlu dikombinasikan dengan _idempotency_. Dengan mekanisme ini, Payment Service dapat mengenali bahwa request yang dikirim ulang merupakan transaksi yang sama, sehingga percobaan ulang tidak menyebabkan transaksi pembayaran diproses lebih dari satu kali.

**Trade-off:** Penggunaan _retry_ dapat meningkatkan beban sistem karena request yang gagal akan dikirim ulang. Jika dilakukan berulang kali tanpa jeda atau batas percobaan, jumlah request dapat semakin banyak dan justru membebani service yang sedang mengalami masalah.

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
Jika FoodGo memperbaiki ketiga pitfall tersebut, arsitektur yang disarankan adalah arsitektur yang lebih *terpisah dan tidak bergantung pada satu server atau satu proses*. Modul seperti pesanan, pembayaran, dan notifikasi kurir dapat dibuat menjadi service yang terpisah sehingga jika salah satu service mengalami masalah, service lainnya tidak langsung ikut berhenti.

Untuk mengatasi masalah *latency, komunikasi antarservice dapat menggunakan proses asynchronous dan dilengkapi timeout. Untuk masalah **network reliability, sistem dapat menggunakan retry dengan batas tertentu agar komunikasi yang gagal dapat dicoba kembali. Sedangkan untuk **SPOF*, beban dapat dibagi ke beberapa server agar tidak hanya bergantung pada satu server.

Hal ini dapat dikaitkan dengan *Tugas 2, terutama pada architectural style **SOA* dan *Publish-Subscribe*. SOA dapat digunakan untuk memisahkan fungsi FoodGo menjadi beberapa service, sedangkan Publish-Subscribe dapat membantu service berkomunikasi melalui pesan atau event tanpa harus saling bergantung secara langsung. Dengan begitu, ketika tim kurir atau tim resto melakukan perubahan dan deployment pada modulnya, modul lain tidak harus ikut restart.