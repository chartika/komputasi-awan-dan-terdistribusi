# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| [Chartika Jenyansa Pangaribuan] | [103072400026] | [Latency Is Zero] |
| [nama 2] | [nim] | [pitfall/bagian yang dikerjakan] |
| [nama 3] | [nim] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: [Latency Is Zero] — ditulis oleh [Chartika Jenyansa Pangaribuan]

**Bukti di skenario:** [modul pesanan memanggil modul pembayaran dan menunggu respon tanpa adanya batas waktu (timeout) sehingga mengakibatkan sistem aplikasi menjadi lambat."]

**Kenapa ini keliru:** [Komunikasi antar modul melalui jaringan tidak berjalan dengan lancar dan cepat. Ketika banyak pengguna yang melakukan pemesanan secara bersamaan maka modul pembayaran akan membutuhkan waktu yang lama untuk memproses pembayaran dan modul pesanan akan terus menunggu sampai mendapatkan respon dari modul pembayaran, karena tidak adanya timeout.]

**Dampak ke FoodGo:** [Saat modul pembayaran terhambat karena menunggu respon, modul pesanan juga akan ikut terhambat dengan permintaan yang terus bertambah. Hal tersebuut mengakibatkan sistem menjadi semakin lambat dan mengalami timeout.]

**Solusi desain awal:** [Menggunakan sistem asynchronous dimana modul pesanan tidak perlu membuat pengguna menunggu seluruh proses selesai, pesanan dapat dicatat terlebih dahulu dan mengirimkan informasi bahwa pembayaran perlu diproses dan modul pembayaran dapat langsung memproses pembayaran.]

**Trade-off:** [Penerapan sistem asynchronous membuat pengguna tidak selalu mendapatkan hasil pembayaran secara langsung. Status pesanan bisa saja awalnya masih "menunggu pembayaran" dan baru berubah setelah proses pembayaran berhasil. Selain itu, sistem menjadi lebih kompleks karena harus menangani pesanan yang terlambat, gagal, atau diproses tidak berurutan.]

---

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Pitfall 3: The Network is Reliable — ditulis oleh Aisyah

**Bukti di skenario:** Tim menemukan bahwa kode mereka menulis asumsi seperti _# network is always reliable, no need for retry_

**Kenapa ini keliru:** Jaringan komputer pada sistem terdistribusi bersifat _nondeterministic_ (tidak selalu dapat diprediksi). Sementara itu, FoodGo menganggap jaringan selalu dapat diandalkan. Padahal, komunikasi antar-service dapat mengalami berbagai kegagalan, seperti packet loss, respons tidak sampai, connection failure, atau koneksi yang terputus. Oleh karena itu, sistem terdistribusi perlu dirancang agar tetap dapat menangani kemungkinan terjadinya kegagalan komunikasi.

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
   - Retry pada proses pembayaran perlu dikombinasikan dengan _idempotency_. Dengan mekanisme ini, Payment Service dapat mengenali bahwa request yang dikirim ulang merupakan transaksi yang sama, sehingga percobaan ulang tidak menyebabkan transaksi pembayaran diproses lebih dari satu kali.

**Trade-off:** Penggunaan _retry_ dapat meningkatkan beban sistem karena request yang gagal akan dikirim ulang. Jika dilakukan berulang kali tanpa jeda atau batas percobaan, jumlah request dapat semakin banyak dan justru membebani service yang sedang mengalami masalah.

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
