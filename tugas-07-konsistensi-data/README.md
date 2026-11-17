# Tugas 7 (Pekan 7) — Konsistensi Data

**Materi terkait:** Data-Centric Consistency (Sequential, Eventual), Client-Centric Consistency.

## Studi Kasus

Data saldo *e-wallet* pelanggan FoodGo berbeda antara server wilayah **Jakarta** dan **Bandung** karena replikasi antar server berjalan lambat. Contoh kasus nyata: pelanggan top-up saldo lewat server Jakarta, lalu dalam hitungan detik memesan makanan lewat aplikasi yang tersambung ke server Bandung — saldo belum ter-update, transaksi ditolak padahal saldo sebenarnya cukup.

## Tugas Kelompok

### Bagian 1 — Analisis (wajib)

1. Tentukan: apakah kasus ini **membutuhkan Sequential Consistency** (semua replika melihat urutan operasi yang sama) atau **cukup Eventual Consistency** (replika akan konsisten "pada akhirnya", boleh sementara berbeda)? Berikan argumen berbasis dampak bisnis (mis. kasus saldo *e-wallet* jauh lebih sensitif dibanding kasus "jumlah like" di media sosial).
2. Jika kalian menyimpulkan Eventual Consistency saja **tidak cukup** untuk skenario ini, usulkan pendekatan **Client-Centric Consistency** yang relevan (mis. *Read-Your-Writes*: pelanggan yang baru top-up harus selalu melihat saldo terbarunya sendiri, walau replika lain belum sinkron).
3. Gambarkan **diagram alir urutan (sequence diagram)** yang menunjukkan operasi read/write antara pelanggan, server Jakarta, server Bandung, dan proses replikasi — untuk skenario **tanpa** jaminan konsistensi (bug terjadi) DAN skenario **dengan** solusi yang kalian usulkan (bug teratasi). Pakai Mermaid (`sequenceDiagram`) di `README.md` — lihat contoh cara pakai di Tugas 2.

### Bagian 2 — Simulasi (opsional, nilai tambah)

Skeleton `src/replica_simulation.py` mensimulasikan dua replika (Jakarta & Bandung) dengan delay replikasi buatan. Lengkapi TODO untuk:
1. Menunjukkan kondisi **inconsistent read** (replika Bandung masih menunjukkan saldo lama walau Jakarta sudah update).
2. Mengimplementasikan mekanisme **Read-Your-Writes** sederhana (mis. dengan version/timestamp per client) yang memperbaiki masalah tersebut.

```bash
python3 src/replica_simulation.py
```

### Analisis Bagian 1

1. Menurut kelompok kami, berdasar pada studi kasus FoodGo, Eventual Consistency saja tidak cukup untuk menangani permasalahan saldo e-wallet. Saldo adalah data yang berhubungan langsung dengan uang, sehingga angka yang ditampilkan harus selalu sesuai dengan saldo terbaru. Sebagai contoh, pelanggan melakukan top-up melalui server Jakarta, lalu langsung memesan makanan melalui server Bandung sebelum proses replikasi selesai. Pada saat itu, server Bandung masih membaca saldo lama. Akibatnya, pesanan pelanggan bisa ditolak padahal saldo sebenarnya sudah cukup.
Karena itu, Sequential Consistency lebih sesuai. Model ini membuat semua replika melihat urutan operasi yang sama, sehingga top-up yang dilakukan lebih dulu pasti diperhitungkan sebelum saldo dibaca untuk transaksi berikutnya. Hal ini berbeda dengan data seperti jumlah like di media sosial. Data tersebut boleh terlambat diperbarui karena tidak berpengaruh langsung pada transaksi keuangan. Jadi, konsistensi data saldo perlu diprioritaskan agar tidak terjadi kesalahan transaksi dan kepercayaan pelanggan tetap terjaga.
2. Untuk mengatasi masalah tersebut, pendekatan Client-Centric Consistency yang dapat digunakan adalah Read-Your-Writes Consistency. Pendekatan ini memastikan pelanggan selalu dapat melihat perubahan data yang baru saja ia lakukan sendiri. Dalam kasus FoodGo, setelah pelanggan melakukan top-up melalui server Jakarta, sistem menyimpan informasi versi terbaru dari saldo tersebut. Ketika pelanggan memesan makanan melalui server Bandung, sistem akan memeriksa apakah versi saldo di server Bandung sudah yang terbaru. Jika versi di server Bandung masih lebih lama, sistem dapat melakukan salah satu dari dua hal: mengarahkan permintaan baca saldo ke server Jakarta yang sudah memiliki data terbaru, atau menunggu sampai proses replikasi selesai. Dengan begitu, pelanggan tetap melihat saldo yang sudah termasuk top-up, bukan data lama dari server Bandung. Pendekatan ini membantu mengurangi transaksi yang ditolak akibat keterlambatan replikasi. Namun, agar transaksi saldo tetap aman, sistem juga perlu menerapkan validasi dan pengelolaan transaksi yang tepat.
3. Sequence Diagram
    a. Skenario tanpa jaminan konsistensi (bug terjadi)
    ```mermaid
    sequenceDiagram
    actor P as Pelanggan
    participant J as Server Jakarta
    participant B as Server Bandung
    participant R as Proses Replikasi

    P->>J: Top-up saldo Rp50.000
    J->>J: Perbarui saldo menjadi Rp50.000
    J-->>P: Top-up berhasil

    Note over J,B: Replikasi belum selesai

    P->>B: Memesan makanan
    B->>B: Membaca saldo pelanggan
    B-->>P: Saldo masih Rp0
    B-->>P: Transaksi ditolak

    J->>R: Kirim perubahan saldo
    R->>B: Replikasi saldo Rp50.000
    B->>B: Perbarui saldo menjadi Rp50.000 
    ```
    b. Skenario dengan Read-Your-Writes (bug teratasi)
    ```mermaid
    sequenceDiagram
    actor P as Pelanggan
    participant J as Server Jakarta
    participant B as Server Bandung
    participant R as Proses Replikasi

    P->>J: Top-up saldo Rp50.000
    J->>J: Perbarui saldo menjadi Rp50.000 (versi 1)
    J-->>P: Top-up berhasil (versi 1)

    Note over J,B: Replikasi masih tertunda

    P->>B: Memesan makanan (versi minimal 1)
    B->>B: Memeriksa versi saldo

    Note over B: Versi Bandung masih 0

    B->>J: Meminta saldo minimal versi 1
    J-->>B: Mengirim saldo Rp50.000 (versi 1)

    B->>B: Menggunakan saldo terbaru
    B-->>P: Saldo Rp50.000
    B-->>P: Transaksi dapat dilanjutkan

    J->>R: Kirim perubahan saldo
    R->>B: Replikasi saldo versi 1
    B->>B: Perbarui data saldo
    ```

## Struktur Submission

```
tugas-07-konsistensi-data/
├── README.md      # Analisis konsistensi + sequence diagram Mermaid
├── JURNAL.md
├── src/            # (opsional) simulasi replikasi
└── bukti/          # (jika mengerjakan simulasi) output program
```

## Rubrik Penilaian (Tugas 7)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan pemilihan model konsistensi | 30% | Argumen berbasis dampak bisnis nyata, bukan hafalan definisi |
| Kualitas sequence diagram | 30% | Menunjukkan jelas titik kegagalan & titik perbaikan |
| Usulan solusi client-centric | 25% | Solusi konkret dan dapat diimplementasikan (bukan wacana abstrak) |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history (+ bonus jika simulasi dikerjakan) |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya konsep umum consistency model ke AI untuk brainstorming; **tidak boleh** meminta AI menuliskan analisis akhir/sequence diagram atau isi `# TODO` di `src/replica_simulation.py` yang tinggal ditempel. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Sebagai bukti pemahaman konsep (bukan hafalan jawaban skenario FoodGo saja), `README.md` wajib menyertakan **satu skenario tambahan** yang kalian buat sendiri (mis. kasus lain di aplikasi ojek online) dan menentukan model konsistensi yang tepat untuk skenario tambahan tersebut.
