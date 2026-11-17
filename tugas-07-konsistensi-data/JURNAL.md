# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi
- Argumen yang dipertimbangkan: Sistem FoodGo menggunakan dua server replika, yaitu Jakarta dan Bandung, yang menyimpan data saldo pelanggan. Kelompok mempertimbangkan Sequential Consistency dan Eventual Consistency berdasarkan kebutuhan konsistensi data dalam transaksi e-wallet. Eventual Consistency memungkinkan perbedaan data sementara selama proses replikasi berlangsung. Kondisi tersebut dapat menyebabkan server Bandung membaca saldo yang belum diperbarui ketika pelanggan baru saja melakukan top-up melalui Jakarta. Akibatnya, transaksi dapat ditolak meskipun saldo pelanggan sebenarnya mencukupi. Hal ini menjadi pertimbangan penting karena data saldo berkaitan langsung dengan transaksi keuangan sehingga membutuhkan ketepatan informasi yang lebih tinggi dibandingkan data seperti jumlah likes di media sosial.
- Kesimpulan akhir & alasan: Berdasarkan hasil diskusi, kelompok memilih Sequential Consistency sebagai model konsistensi utama karena sistem perlu menjaga urutan operasi agar pembaruan saldo dapat diperhitungkan sebelum dilakukan pembacaan berikutnya. Selain itu, kelompok mengusulkan pendekatan Client-Centric Consistency dengan menerapkan Read-Your-Writes. Pendekatan ini menggunakan versioning untuk memeriksa apakah data saldo pada server tujuan sudah sesuai dengan versi terbaru. Apabila server Bandung masih memiliki versi lama, sistem akan mengalihkan permintaan pembacaan ke server Jakarta yang sudah memiliki pembaruan saldo. Dengan demikian, pelanggan tetap dapat memperoleh informasi saldo setelah melakukan top-up meskipun proses replikasi belum selesai.

## Simulasi (jika dikerjakan)
Hasil skenario naif vs Read-Your-Writes:
- Skenario Naif
Pada skenario ini, pelanggan melakukan top-up sebesar Rp50.000 melalui server Jakarta. Server Jakarta berhasil memperbarui saldo pelanggan menjadi Rp50.000 dengan versi 1. Namun, proses replikasi menuju server Bandung mengalami keterlambatan selama 2 detik. Ketika pelanggan mencoba membaca saldo melalui server Bandung sebelum replikasi selesai, sistem masih menampilkan saldo Rp0 karena data terbaru belum diterima. Setelah proses replikasi selesai, server Bandung berhasil memperbarui saldo menjadi Rp50.000 dengan versi 1. Hasil pengujian ini menunjukkan terjadinya inconsistent read karena server Bandung masih memberikan data lama meskipun saldo telah diperbarui di Jakarta.
- Skenario Read-Your-Writes
Pada skenario ini, pelanggan melakukan top-up tambahan sebesar Rp20.000 melalui server Jakarta sehingga saldo bertambah menjadi Rp70.000 dengan versi 2. Ketika pelanggan mencoba membaca saldo melalui server Bandung, sistem memeriksa versi data dan menemukan bahwa server Bandung belum memiliki versi terbaru yang dibutuhkan. Oleh karena itu, mekanisme Read-Your-Writes mengalihkan permintaan pembacaan ke server Jakarta. Hasilnya, pelanggan berhasil memperoleh saldo terbaru sebesar Rp70.000 dengan versi 2 tanpa harus menunggu proses replikasi selesai. Setelah proses replikasi berlangsung, server Bandung juga berhasil memperbarui saldo menjadi Rp70.000 dengan versi 2. Hasil pengujian ini menunjukkan bahwa mekanisme Read-Your-Writes berhasil mengatasi masalah pembacaan data lama pada skenario tersebut.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
