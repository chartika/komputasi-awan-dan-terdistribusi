# Jurnal Proses — Tugas 4

## Jalur yang dipilih
- MQ, alasan: notifikasi ke Kurir tidak butuh respons langsung, jadi lebih cocok asinkron. Dengan RabbitMQ, modul Pembayaran cukup mengirim pesan tanpa menunggu modul Kurir, jadi transaksi tetap cepat dan pesan tidak hilang walaupun Kurir sedang mati.

## Kendala teknis
- Error saat setup (mis. koneksi RabbitMQ ditolak, port bentrok): -

## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: Awalnya consumer menyala dan menerima 3 event (user1, user2, user3) secara langsung. Setelah itu consumer dimatikan dengan Ctrl+C, lalu publisher dijalankan 2 kali sehingga ada 6 event yang terkirim saat tidak ada consumer aktif. Ketika consumer dinyalakan lagi, ke-6 event tersebut langsung diterima dan diproses secara berurutan (user1, user2, user3, lalu user1, user2, user3 lagi) dengan jumlah dan nominal yang sama seperti yang dikirim publisher. Artinya tidak ada pesan yang hilang meskipun consumer sedang mati, karena pesan tetap tersimpan di antrean 'pembayaran_berhasil' sampai consumer aktif kembali.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 13-10-2026 | Chat GPT | Apa keunggulan jalur a dan b | Pilih RPC jika proses membutuhkan jawaban langsung, seperti pengecekan saldo sebelum pembayaran, pilih Message Queue jika proses bisa dilakukan belakangan dan tidak boleh menghambat modul pengirim, seperti notifikasi pembayaran kepada kurir.| - |
