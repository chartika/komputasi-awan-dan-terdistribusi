# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Pada awalnya, pencarian successor belum memperhatikan kondisi wrap-around, yaitu ketika hash kurir lebih besar dari ID node terbesar.
- Cara memperbaikinya: Menambahkan kondisi wrap-around pada fungsi find_successor supaya ketika hash kurir melebihi ID node terbesar, pencarian dilanjutkan kembali dari node dengan ID terkecil dalam ring.

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: Awalnya terdapat empat node, yaitu 40, 102, 136, dan 177. kemudian, node 123 (Medan) bergabung ke dalam ring. setelah itu, kurir-012 dengan hash 116 berpindah dari node 136 ke node 123.
- Hasil sebelum & sesudah node keluar: Selanjutnya, node 102 (Jakarta-2) keluar dari ring. setelah node tersebut keluar, kurir-001 dengan hash 50 berpindah dari node 102 ke Node 123.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 03/11/2026 | ChatGPT | Apa yang terjadi pada mapping ketika node baru bergabung atau keluar dari ring? | Penjelasan mengenai perubahan tanggung jawab mapping ketika terjadi perubahan topologi. | Digunakan sebagai referensi untuk menentukan skenario pengujian join dan leave. |
