# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| [nama 1] | [nim] | [pitfall/bagian yang dikerjakan] |
| [nama 2] | [nim] | [pitfall/bagian yang dikerjakan] |
| [nama 3] | [nim] | [pitfall/bagian yang dikerjakan] |

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

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
