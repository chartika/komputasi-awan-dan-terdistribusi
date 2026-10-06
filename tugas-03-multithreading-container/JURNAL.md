# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: **11 dari 100 pesanan**.
- Percobaan dilakukan dengan menggunakan 10 worker thread yang memproses 100 pesanan secara konkuren. Pada percobaan awal, `processed_count` digunakan bersama dengan seluruh thread tanpa menggunakan mekanisme sinkronisasi.
- Hasil counter menjadi lebih kecil dari jumlah pesanan sebenarnya karena terjadinya **race condition**. Beberapa thread dapat membaca nilai `processed_count` yang sama pada waktu yang hampir bersamaan. Setelah itu, masing-masing thread menambahkan nilai tersebut dan menyimpannya kembali. Akibatnya, pembaruan dari salah satu thread dapat tertimpa oleh thread lainnya.
- Jeda `time.sleep(0.001)` pada proses pembaruan counter membuat kemungkinan beberapa thread membaca nilai yang sama menjadi lebih besar, sehingga race condition dapat terlihat pada hasil percobaan.

    **Bukti Percobaan Tanpa Lock**
    ![Output tanpa Lock](bukti/output_tanpa_lock.png) 

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: **100 dari 100 pesanan**.
- Perbaikan dilakukan dengan menggunakan `threading.Lock()` untuk melindungi bagian kode yang melakukan pembacaan dan pembaruan `processed_count`.
- Dengan menggunakan `Lock`, hanya satu thread yang dapat melakukan perubahan terhadap counter pada satu waktu. Thread lain harus menunggu sampai thread yang sedang menggunakan Lock selesai.
- Setelah Lock diterapkan, pembaruan nilai `processed_count` tidak lagi saling tertimpa sehingga seluruh 100 pesanan dapat tercatat dengan benar.

    **Bukti Percobaan Dengan Lock**
    ![Output dengan Lock](bukti/output_dengan_lock.png)

## Kendala Docker
- Kendala ditemukan ketika melakukan proses build Docker. Docker Desktop awalnya tidak dapat menjalankan Docker Engine dan muncul pesan **`Docker Desktop is unable to start`**.
- Setelah dilakukan pengecekan, WSL sebelumnya belum tersedia pada sistem sehingga Docker Desktop belum dapat menggunakan WSL 2 sebagai backend.
- WSL kemudian dipasang dan dikonfigurasi. Setelah itu Docker Desktop dapat dijalankan kembali dan statusnya berubah menjadi **Engine running**.
- Setelah Docker Engine berhasil berjalan, proses build image dan menjalankan container dapat dilakukan dengan perintah:

```bash
docker build -t foodgo-order-sim .
docker run --rm foodgo-order-sim
```

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
