# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## [Tanggal diskusi 1]
- Peserta: [nama-nama yang hadir]
- Poin diskusi: ...
- Perbedaan pendapat (jika ada): ...

## [Tanggal diskusi 2]
- ...

## Review Silang
- [Nama] mengomentari analisis [Nama lain]: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 21-09-2026 | ChatGpt | Diberikan studi kasus sebagai berikut:
Studi Kasus: FoodGo
Startup **FoodGo** (aplikasi pesan-antar makanan) mengalami kegagalan sistem saat pesanan melonjak (misalnya jam makan siang atau saat promo besar). Gejala yang dilaporkan tim engineering FoodGo:
- Aplikasi jadi sangat lambat, beberapa permintaan *timeout*.
- Server backend kadang *crash* total dan perlu di-restart manual.
- Tim menemukan bahwa kode mereka menulis asumsi seperti `# network is always reliable, no need for retry` dan tidak ada *timeout* sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu).
- Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama.
Ini merupakan gejala klasik dari **kesalahan asumsi tentang jaringan dan skala** yang terkenal di literatur sebagai *Fallacies of Distributed Computing* (Peter Deutsch et al.), ditambah masalah desain terkait skalabilitas.

Dari daftar *Fallacies of Distributed Computing* terdapat pitfal "the network is reliable", "latency is zero", "bandwidth is infinite", "the network is secure", "topology doesn't change", "there is one administrator", "transport cost is zero", "the network is homogeneous" **dan** mis. *single point of failure* karena arsitektur monolitik. Piftal apa yang mungkin relevan dengan studi kasus diatas dan jelaskan secara spesifik alasannya! | Pitfall yang relevan adalah _the network is reliable_ karena FoodGo menganggap jaringan selalu dapat diandalkan sehingga tidak menyediakan mekanisme retry ketika komunikasi gagal, _latency is zero_ karena tidak ada timeout sehingga modul pesanan dapat menunggu respons pembayaran tanpa batas waktu, serta _single point of failure_ karena seluruh modul berjalan dalam satu server dan proses monolitik, sehingga ketika server kewalahan atau crash, seluruh layanan ikut terganggu.   | ... |
