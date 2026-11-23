# Jurnal Proses — Tugas 9

## Diskusi deployment model
- Opsi yang dipertimbangkan dan kenapa akhirnya memilih salah satu: Dalam pengerjaan tugas ini, kelompok kami mempertimbangkan Private Cloud, Public Cloud, Hybrid Cloud, dan Community Cloud. Private Cloud mempunyai kelebihan dalam hal kontrol infrastruktur, tetapi jika setiap instansi harus mengelola server sendiri akan membutuhkan biaya dan pengelolaan yang lebih besar. Public Cloud mempunyai skalabilitas yang baik, tetapi kurang sesuai jika seluruh data kependudukan harus berada dalam infrastruktur yang tidak dikendalikan pemerintah. Hybrid Cloud memberikan fleksibilitas, tetapi membutuhkan pengamanan dan pengelolaan integrasi yang lebih kompleks. Setelah membandingkan beberapa pilihan tersebut, kami memilih Government Community Cloud karena dapat digunakan bersama oleh berbagai instansi pemerintah dengan pengelolaan dan kebijakan keamanan yang terpusat.


## Diskusi service model per komponen
Kelompok kami memilih kombinasi IaaS, PaaS, dan SaaS karena setiap komponen mempunyai kebutuhan berbeda. IaaS digunakan untuk database utama dan penyimpanan biometrik karena membutuhkan kontrol infrastruktur yang lebih besar, PaaS digunakan untuk API verifikasi NIK dan integrasi antarinstansi karena mempermudah pengembangan aplikasi, sedangkan SaaS digunakan untuk dashboard administrasi dan monitoring agar administrator dapat menggunakan aplikasi yang sudah disediakan.

## Diskusi Risiko dan Mitigasi 
Kami mengidentifikasi beberapa risiko yang dapat terjadi, yaitu kebocoran data akibat penyalahgunaan hak akses, server overload ketika terjadi lonjakan permintaan, gangguan pusat data, dan penyalahgunaan API untuk mengambil data secara massal. Untuk mengurangi risiko tersebut, kami mengusulkan penggunaan kontrol akses, enkripsi, MFA, autoscaling, load balancing, rate limiting, audit log, backup, dan Disaster Recovery Center.


## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|23 November 2026|ChatGpt|Berikan saya pemahaman tentang studi kasus yang didapatkan dan Mencari gambaran deployment model yang cocok untuk sistem data kependudukan.|Ai menyarankan hybrid namun dari penjelasan dari setiap model deployment kami sepakat memakai Gonverentment Community Cloud |Kami menulis sendiri dengan pemahaman dan juga bukti terkait agar menguatkan teori kami|
| ... | ... | ... | ... | ... |
