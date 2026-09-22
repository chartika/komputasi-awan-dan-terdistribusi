# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## [21 September 2026] 
- Peserta: [Chartika, Alexandria, Nur Aisyah]

- Poin diskusi:
1. Menentukan dan menyepakati untuk menggunakan 3 pitfall yaitu, "Latency Is Zero", "Single point of Failure", dan "The Network is Reliable"
2. Chartika memilih pitfall "Latency Is Zero" Karena komunikasi antar modul tidak berjalan dengan cepat dan membuat sistem aplikasi menjadi terhambat karena tidak ada batas waktu (timeout).
3. Alexandria memilih pitfall "Single point of Failure" karena ...
4. Nur Aisyah memilih pitfall "The Network is Reliable" karena jaringan pada FoodGo dianggap selalu dapat diandalkan sehingga tidak ada mekanisme retry ketika terjadi kegagalan komunikasi antar-service.

- Perbedaan pendapat (jika ada): ...

## [22 September 2026]
- Saling menjelaskan mengenai pitfall yang telah di identifikasi
- Melakukan review silang dari hasil analisis rekan tim

## Review Silang
- [Chartika] mengomentari analisis [Alexandria]: ...
- [Chartika] mengomentari analisis [Nur Aisyah]: ...
- [Alexandria] mengomentari analisis [Chartika]: ...
- [Alexandria] mengomentari analisis [Nur Aisyah]: ...
- [Nur Aisyah] mengomentari analisis [Chartika]: ...
- [Nur Aisyah] mengomentari analisis [Alexandria]: Menurut saya, analisis yang diberikan sudah cukup jelas dan sesuai dengan skenario FoodGo. Solusi penggunaan load balancing juga sudah relevan untuk mengatasi beban pada satu server. Namun, bagian solusi dapat diperjelas dengan menambahkan penggunaan beberapa server secara redundant, sehingga ketika salah satu server mengalami gangguan, sistem masih dapat berjalan melalui server lainnya

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 21-09-2026 | ChatGPT | Diberikan studi kasus sebagai berikut:<br><br>**Studi Kasus : FoodGo**<br>Startup **FoodGo** (aplikasi pesan-antar makanan) mengalami kegagalan sistem saat pesanan melonjak (misalnya jam makan siang atau saat promo besar). Gejala yang dilaporkan tim engineering FoodGo:<br>- Aplikasi jadi sangat lambat, beberapa permintaan *timeout*.<br>- Server backend kadang *crash* total dan perlu di-restart manual.<br>- Tim menemukan bahwa kode mereka menulis asumsi seperti `# network is always reliable, no need for retry` dan tidak ada *timeout* sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu).<br>- Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama.<br><br>Ini merupakan gejala klasik dari **kesalahan asumsi tentang jaringan dan skala** yang terkenal di literatur sebagai *Fallacies of Distributed Computing* (Peter Deutsch et al.), ditambah masalah desain terkait skalabilitas.<br><br>Dari daftar *Fallacies of Distributed Computing* terdapat pitfall "the network is reliable", "latency is zero", "bandwidth is infinite", "the network is secure", "topology doesn't change", "there is one administrator", "transport cost is zero", "the network is homogeneous" **dan** mis. *single point of failure* karena arsitektur monolitik. Pitfall apa yang mungkin relevan dengan studi kasus diatas dan jelaskan secara spesifik alasannya! | Pitfall yang relevan adalah *the network is reliable* karena FoodGo menganggap jaringan selalu dapat diandalkan sehingga tidak menyediakan mekanisme retry ketika komunikasi gagal, *latency is zero* karena tidak ada timeout sehingga modul pesanan dapat menunggu respons pembayaran tanpa batas waktu, serta *single point of failure* karena seluruh modul berjalan dalam satu server dan proses monolitik, sehingga ketika server kewalahan atau crash, seluruh layanan ikut terganggu. | Menuliskan ulang alasan untuk setiap pitfall agar penjelasan lebih fokus pada penyebab teknis dan dampaknya |