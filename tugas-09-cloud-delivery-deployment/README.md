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

Jawab : Berdasarkan studi kasus, kelompok kami memilih Government Community Cloud sebagai deployment model untuk Sistem Data Kependudukan. Sistem ini menyimpan data penting masyarakat, seperti nama, NIK, alamat, dan biometrik yang tidak boleh diakses oleh sembarang pihak. Selain itu, sistem harus dapat digunakan oleh banyak instansi dan mampu menangani lonjakan akses.
Community Cloud memungkinkan berbagai instansi menggunakan infrastruktur yang sama tanpa harus membangun server masing-masing. Pengelolaan dan kebijakan keamanannya juga dapat diatur oleh pemerintah.
Pemilihan ini sesuai dengan lima karakteristik NIST. On-Demand Self-Service memungkinkan pemerintah menyesuaikan sumber daya sesuai kebutuhan. Broad Network Access memudahkan instansi mengakses sistem melalui jaringan yang aman. Resource Pooling memungkinkan penggunaan server dan penyimpanan secara bersama. Rapid Elasticity memungkinkan kapasitas ditambah saat terjadi lonjakan akses, sedangkan Measured Service membantu pemerintah memantau penggunaan sumber daya dan aktivitas setiap instansi.
Dengan demikian, Government Community Cloud dapat memenuhi kebutuhan keamanan dan skalabilitas sistem. Penerapannya tetap harus didukung enkripsi, pembatasan hak akses, autentikasi, dan pencatatan aktivitas.


2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).

Jawab :
Kelompok kami memilih kombinasi IaaS, PaaS, dan SaaS karena setiap komponen sistem memiliki kebutuhan yang berbeda. IaaS digunakan untuk database utama dan penyimpanan data biometrik karena membutuhkan kontrol lebih besar terhadap server, penyimpanan, dan keamanan. PaaS digunakan untuk API verifikasi NIK, autentikasi, dan integrasi antarinstansi agar pengembang lebih mudah membangun dan mengelola aplikasi. Sementara itu, SaaS digunakan untuk dashboard administrasi dan monitoring karena administrator dapat menggunakan aplikasi yang sudah tersedia tanpa mengelola server sendiri.
Kombinasi ketiganya dipilih agar pengelolaan sistem lebih sesuai dengan kebutuhan setiap komponen, sementara keamanan data utama tetap menjadi tanggung jawab pemerintah.


3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).

Jawab :
- Risiko pertama adalah kebocoran data akibat penyalahgunaan hak akses. Contohnya, bank yang hanya membutuhkan verifikasi NIK justru dapat melihat alamat dan data biometrik penduduk. Untuk mencegahnya, diperlukan pembatasan hak akses, MFA, enkripsi, dan audit log.
- Risiko kedua adalah server mengalami overload ketika terjadi lonjakan permintaan, misalnya saat pemilu atau pendaftaran sekolah. Hal ini dapat menyebabkan sistem lambat atau tidak dapat diakses. Mitigasinya adalah menggunakan autoscaling, load balancing, rate limiting, dan load testing.
- Risiko ketiga adalah gangguan pusat data yang menyebabkan instansi tidak dapat mengakses layanan. Untuk mengatasinya, pemerintah perlu menyediakan backup berkala, Disaster Recovery Center (DRC), serta menentukan RTO dan RPO.
- Risiko keempat adalah penyalahgunaan API untuk mengambil data penduduk secara massal. Mitigasinya adalah menggunakan API Gateway, pembatasan jumlah permintaan, token akses, dan pemantauan aktivitas yang mencurigakan.


4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

Jawab :
Alternatif yang tidak dipilih adalah Public Cloud murni. Public Cloud memiliki kelebihan dalam hal skalabilitas dan kemudahan menambah sumber daya. Namun, infrastruktur fisiknya dikelola oleh penyedia layanan sehingga pemerintah tidak memiliki kendali langsung atas seluruh infrastruktur. Hal ini kurang sesuai dengan kebutuhan Sistem Data Kependudukan yang mengharuskan pengelolaan dan penyimpanan data berada dalam kendali pemerintah.
Oleh karena itu, kelompok kami memilih Government Community Cloud karena dapat digunakan bersama oleh berbagai instansi dengan pengelolaan dan kebijakan keamanan yang ditetapkan pemerintah.

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
