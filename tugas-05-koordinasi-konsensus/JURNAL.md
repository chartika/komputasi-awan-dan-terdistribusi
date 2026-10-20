# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-4: Kendala yang dihadapi adalah memahami alur komunikasi antar node dan proses pemilihan leader berdasarkan ID proses. Selain itu, perlu memastikan pesan ELECTION, OK, dan COORDINATOR dikirim serta diterima dengan benar agar proses pemilihan leader dapat berjalan sesuai Bully Algorithm.

## Skenario 1: Start normal
- Leader yang terpilih: Node 5 (port 5005)
- Log/observasi: Pada pengujian pertama, kelima node dijalankan menggunakan port 5001 sampai 5005. Setiap node melakukan komunikasi untuk menentukan leader. Karena Node 5 memiliki ID paling tinggi, Node 5 terpilih sebagai leader. Hal ini terlihat pada terminal Node 5 yang menampilkan log broadcast COORDINATOR, saya jadi leader. Log tersebut menunjukkan bahwa Node 5 mengumumkan dirinya sebagai leader kepada node lainnya.

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: Node 4 (port 5004).
- Berapa lama waktu sampai leader baru terdeteksi: Waktu yang dibutuhkan belum bisa dihitung secara pasti karena screenshot tidak menampilkan timestamp saat Node 5 dimatikan dan saat Node 4 menjadi leader baru.

Pada pengujian kedua, Node 5 dihentikan menggunakan Ctrl+C, yang ditandai dengan munculnya KeyboardInterrupt pada terminal. Setelah itu, Node 4 menjalankan proses pemilihan leader dan menampilkan log broadcast COORDINATOR, saya jadi leader. Hasil ini menunjukkan bahwa Node 4 mengambil alih posisi leader setelah Node 5 berhenti. Hal tersebut sesuai dengan aturan Bully Algorithm, yaitu node dengan ID tertinggi yang masih aktif akan menjadi leader baru.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 20 Oktober 2026 | ChatGPT | Bantu memahami kendala saat mengisi TODO 1–4 pada implementasi Bully Algorithm. | Menjelaskan alur komunikasi antar-node dan fungsi pesan ELECTION, OK, dan COORDINATOR dalam pemilihan leader. | Penjelasan digunakan sebagai referensi untuk memahami alur algoritma, kemudian disesuaikan dengan kendala yang dialami saat mengerjakan implementasi. |
