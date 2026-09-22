# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| [nama 1] | [nim] | [pitfall/bagian yang dikerjakan] |
| [nama 2] | [nim] | [pitfall/bagian yang dikerjakan] |
| [Nur Aisyah Luhur Pambudi] | [103072430015] | [The Network is Reliable] |

## Pitfall 1: [nama pitfall] — ditulis oleh [nama]

**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]

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
