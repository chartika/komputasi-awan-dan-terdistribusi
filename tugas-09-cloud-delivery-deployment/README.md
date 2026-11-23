# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.
Jawab : Berdasarkan studi kasus, pemerintah ingin membangun Sistem Data Kependudukan yang menyimpan informasi penting masyarakat, seperti nama, NIK, alamat, dan data biometrik. Sistem ini akan digunakan oleh banyak instansi, mulai dari Dukcapil daerah, kepolisian, sampai bank untuk kebutuhan verifikasi identitas atau KYC.
Menurut kelompok kami, sistem ini memiliki beberapa kebutuhan utama:
 **Kerahasiaan data:** Data kependudukan tidak boleh diakses oleh pihak yang tidak memiliki wewenang. Terlebih lagi, data biometrik termasuk data pribadi yang bersifat spesifik berdasarkan UU Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.
**Ketersediaan layanan:** Sistem harus tetap bisa digunakan oleh berbagai instansi meskipun jumlah permintaan meningkat secara tiba-tiba.
**Skalabilitas:** Kapasitas server harus bisa disesuaikan ketika terjadi lonjakan akses, misalnya saat pemilu atau pendaftaran sekolah.
**Kontrol infrastruktur:** Pemerintah harus memiliki kendali atas lokasi penyimpanan, pengelolaan, keamanan, dan akses terhadap data.
**Integrasi antarinstansi:** Setiap instansi harus bisa mengakses data sesuai tugas dan kewenangannya tanpa harus memiliki salinan seluruh database kependudukan.
Dari kebutuhan tersebut, kami menyimpulkan bahwa sistem ngga cukup hanya mengutamakan keamanan, tetapi juga harus memperhatikan ketersediaan dan kemampuan infrastruktur dalam menangani banyak permintaan secara bersamaan. Berdasarkan studi kasus yang diberikan, kelompok kami memilih **Government Community Cloud** sebagai deployment model yang paling sesuai untuk Sistem Data Kependudukan karena sistem ini digunakan oleh banyak instansi pemerintah, seperti Dukcapil daerah, kepolisian, dan bank yang memiliki kewenangan untuk melakukan verifikasi identitas. Sistem ini menyimpan informasi penting masyarakat, seperti nama, NIK, alamat, dan data biometrik, sehingga membutuhkan keamanan dan pengawasan yang ketat. Menurut kami, Community Cloud cocok karena beberapa instansi yang memiliki kepentingan dan kebutuhan keamanan serupa dapat menggunakan infrastruktur cloud secara bersama-sama, sementara pengelolaannya tetap berada di bawah kendali pemerintah. Pemilihan tersebut juga dapat dikaitkan dengan lima karakteristik cloud computing menurut NIST SP 800-145. Pertama, On-Demand Self-Service memungkinkan pemerintah menyesuaikan kebutuhan sumber daya komputasi tanpa harus melakukan pengadaan server secara manual setiap kali kebutuhan meningkat. Kedua, Broad Network Access memungkinkan instansi yang memiliki izin mengakses layanan melalui jaringan yang aman tanpa harus menyimpan seluruh database di server masing-masing. Ketiga, Resource Pooling memungkinkan sumber daya seperti server, penyimpanan, dan jaringan digunakan bersama oleh berbagai instansi sehingga lebih efisien. Keempat, Rapid Elasticity memungkinkan kapasitas server ditambah ketika terjadi lonjakan permintaan, misalnya saat pemilu atau pendaftaran sekolah, kemudian dikurangi kembali ketika kondisi normal. Kelima, Measured Service memungkinkan pemerintah memantau penggunaan sumber daya, jumlah permintaan API, kapasitas penyimpanan, dan aktivitas setiap instansi agar penggunaan infrastruktur tetap terkendali. Menurut kelompok kami, **Government Community Cloud** dapat menyeimbangkan kebutuhan keamanan dan skalabilitas karena data utama tetap disimpan dalam infrastruktur yang dikendalikan pemerintah, sedangkan sumber daya komputasi dapat digunakan bersama oleh berbagai instansi. Keamanan juga harus didukung dengan enkripsi data, pembatasan hak akses, autentikasi, audit log, dan backup. Pemilihan ini sejalan dengan Perpres Nomor 95 Tahun 2018 tentang SPBE yang mengatur penggunaan infrastruktur SPBE Nasional secara bersama oleh instansi pemerintah. Namun, Community Cloud tidak otomatis menjamin keamanan karena pemerintah tetap harus mengatur tanggung jawab pengelolaan, akses, dan perlindungan data setiap instansi.


2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).
Jawab : Untuk service model, kelompok kami merekomendasikan kombinasi IaaS, PaaS, dan SaaS karena setiap komponen Sistem Data Kependudukan memiliki kebutuhan pengelolaan yang berbeda. IaaS digunakan untuk database utama dan penyimpanan data biometrik karena pemerintah membutuhkan kontrol lebih besar terhadap server, sistem operasi, jaringan, penyimpanan, dan konfigurasi keamanan. PaaS digunakan untuk layanan API verifikasi NIK, autentikasi, dan integrasi antarinstansi karena pengembang dapat lebih fokus membangun dan mengelola aplikasi tanpa harus menangani seluruh infrastruktur dari awal. Sementara itu, SaaS digunakan untuk dashboard administrasi, monitoring, dan portal informasi layanan yang tidak menampilkan data sensitif secara langsung karena pengguna cukup menggunakan aplikasi yang sudah disediakan tanpa mengelola server sendiri. Pembagian tersebut dipilih agar setiap komponen mendapatkan model layanan yang sesuai dengan kebutuhannya, sehingga pemerintah tetap mempunyai kontrol terhadap data utama tetapi tidak harus mengelola seluruh aplikasi secara manual. Penggunaan SaaS juga harus tetap berada pada lingkungan yang memenuhi kebijakan keamanan pemerintah dan tidak menjadi alasan untuk memindahkan data sensitif ke layanan eksternal yang tidak terkendali.


3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).
Jawab : Risiko pertama adalah kebocoran data akibat kesalahan atau penyalahgunaan hak akses antarinstansi, misalnya ketika bank yang hanya membutuhkan verifikasi NIK justru dapat melihat alamat dan data biometrik masyarakat, sehingga mitigasinya adalah menerapkan Role-Based Access Control (RBAC), prinsip least privilege, Multi-Factor Authentication (MFA), enkripsi, dan pencatatan aktivitas melalui audit log agar setiap instansi hanya dapat mengakses informasi sesuai kewenangannya. Risiko kedua adalah server mengalami overload ketika terjadi lonjakan permintaan saat pemilu atau pendaftaran sekolah, sehingga layanan menjadi lambat bahkan tidak dapat diakses, dan mitigasinya adalah menggunakan autoscaling, load balancing, rate limiting, monitoring kapasitas, serta melakukan load testing sebelum periode dengan perkiraan lonjakan akses. Risiko ketiga adalah gangguan pusat data yang dapat menyebabkan banyak instansi kehilangan akses secara bersamaan, sehingga pemerintah perlu menyediakan backup berkala, Disaster Recovery Center (DRC) di lokasi berbeda, serta menentukan Recovery Time Objective (RTO) dan Recovery Point Objective (RPO) agar layanan dapat dipulihkan ketika terjadi gangguan. Risiko keempat adalah penyalahgunaan API untuk mengambil data kependudukan secara massal menggunakan akun instansi yang sudah terdaftar, sehingga mitigasinya adalah menggunakan API Gateway, pembatasan jumlah permintaan, token akses dengan hak tertentu, serta monitoring aktivitas untuk mendeteksi permintaan yang tidak normal.


4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).
Jawab : Alternatif pertama yang kami pertimbangkan tetapi tidak dipilih adalah Public Cloud murni karena meskipun mempunyai kemampuan skalabilitas yang baik, penggunaan infrastruktur penyedia eksternal untuk menyimpan seluruh database kependudukan dan data biometrik kurang sesuai dengan kebutuhan kontrol infrastruktur pemerintah. Hal ini menjadi perhatian karena data biometrik termasuk data pribadi spesifik berdasarkan UU Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi, sedangkan pengelolaan sistem elektronik lingkup publik juga diatur dalam PP Nomor 71 Tahun 2019. Bukan berarti semua Public Cloud tidak aman atau otomatis dilarang, tetapi penggunaannya harus mempertimbangkan ketentuan, lokasi pengelolaan data, dan kontrol pemerintah. Alternatif kedua adalah Private Cloud murni, yang sebenarnya mempunyai tingkat kontrol infrastruktur lebih besar karena digunakan secara eksklusif oleh satu organisasi, tetapi kurang menjadi pilihan utama apabila setiap instansi harus menyediakan dan mengelola server sendiri. Hal tersebut dapat meningkatkan biaya, membuat penggunaan sumber daya kurang efisien, dan menyulitkan integrasi antarwilayah. Oleh karena itu, kami lebih memilih Government Community Cloud karena infrastruktur dapat digunakan bersama oleh banyak instansi dengan pengelolaan dan kebijakan keamanan yang terpusat.

## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model | 25% | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal |
| Analisis risiko & mitigasi | 25% | Risiko spesifik ke konteks data kependudukan (bukan risiko generik) |
| Perbandingan dengan alternatif yang ditolak | 20% | Argumen penolakan jelas dan berdasar |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.
