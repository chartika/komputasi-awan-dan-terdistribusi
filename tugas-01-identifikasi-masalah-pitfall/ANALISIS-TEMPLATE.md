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

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
