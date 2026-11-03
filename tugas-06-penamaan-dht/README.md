# Tugas 6 (Pekan 6) — Penamaan & Resolusi Lokasi

**Materi terkait:** Flat Naming, Structured Naming (DNS), Distributed Hash Table (DHT)/Chord.

## Studi Kasus

Pelanggan FoodGo kesulitan menemukan alamat IP server kurir yang **dinamis** (kurir berpindah lokasi/jaringan, IP-nya sering berubah). FoodGo butuh cara memetakan **ID Kurir** (identitas tetap) ke **alamat IP terkininya** tanpa server pusat tunggal yang jadi bottleneck/single point of failure.

## Tugas Kelompok

Implementasikan **simulasi Chord DHT** sederhana (single-process, tidak perlu jaringan sungguhan — cukup simulasi struktur data & algoritma di satu program Python) yang memetakan ID Kurir ke alamat IP mereka.

Konsep yang harus terlihat jalan dalam simulasi kalian:
1. **Consistent hashing**: ID Kurir dan ID Node di-hash ke ruang angka yang sama (mis. 0–255 untuk kesederhanaan, `m=8` bit).
2. **Ring topology**: node-node diurutkan melingkar berdasarkan hasil hash-nya.
3. **Lookup**: fungsi `lookup(kurir_id)` yang menemukan node mana yang bertanggung jawab menyimpan mapping ID Kurir tersebut → alamat IP-nya (aturan Chord: node dengan ID hash **terkecil yang lebih besar atau sama dengan** hash key, disebut *successor*).
4. **Perubahan topologi**: simulasikan minimal satu node baru bergabung (`join`) atau satu node keluar (`leave`), tunjukkan bagaimana mapping berpindah tanggung jawab ke node lain.

Skeleton disediakan di `src/chord_simulation.py` dengan fungsi hashing dan struktur ring sudah ada — bagian `lookup()`, `join()`, dan `leave()` sengaja dikosongkan.

### Cara Menjalankan

```bash
python3 src/chord_simulation.py
```

## Tugas Analisis (`README.md`)

1. Jelaskan **kenapa DHT/Chord** lebih cocok untuk kasus ini dibanding **flat naming sederhana** (mis. tabel pusat ID→IP) atau **DNS konvensional** — kaitkan dengan sifat "IP kurir sering berubah" dan kebutuhan tanpa titik gagal tunggal.
2. Gambarkan (boleh pakai Mermaid, lihat Tugas 2) ring topology dari simulasi kalian, tandai node mana yang bertanggung jawab atas ID Kurir mana.
3. Jelaskan apa yang terjadi pada mapping saat sebuah node **keluar** dari ring (siapa yang mengambil alih tanggung jawabnya) — dukung dengan output program.

## Jawaban Analisis Kelompok
2. Diagram 1: Sebelum Join
![Diagram Ring Awal](<diagram/Diagram_ring_awal (sebelum Join).png>)
Pada diagram pertama, ring terdiri dari empat node, yaitu node 40 (Bandung), node 102 (Jakarta-2), node 136 (Surabaya), dan node 177 (Jakarta-1). Setiap kurir akan diarahkan ke node successor berdasarkan nilai hash masing-masing.

Diagram 2: Setelah Join
![Diagram Setelah Join](diagram/Diagram_setelah_Join.png)
Kemudian, pada diagram kedua, terjadi proses join, yaitu bergabungnya node 123 (Medan) ke dalam ring. setelah node tersebut bergabung, urutan ring berubah menjadi 40 → 102 → 123 → 136 → 177 → 40. perubahan ini menyebabkan kurir-012 dengan hash 116 berpindah tanggung jawab dari Node 136 ke Node 123

Diagram 3: Setelah Leave
![Diagram Setelah Leave](diagram/Diagram_setelah_leave.png)
Selanjutnya, pada diagram ketiga, terjadi proses leave, yaitu keluarnya node 102 (Jakarta-2) dari ring. setelah node tersebut keluar, urutan ring berubah menjadi 40 → 123 → 136 → 177 → 40. akibatnya, tanggung jawab kurir-001 dengan hash 50 yang sebelumnya berada di node 102 berpindah ke node 123

3. Dalam simulasi ini, node-jakarta-2 dengan ID hash 102 dikonfigurasikan keluar dari ring. Sebelumnya, data kurir-001 (ID hash 50) dikelola oleh node 102 karena posisinya sebagai successor dari kunci kurir tersebut. Pasca keluarnya node 102, mekanisme Chord menetapkan successor baru berdasarkan aturan ID hash terdekat yang lebih besar atau sama, sehingga node-medan-1 (ID hash 123) mengambil alih tanggung jawab penyimpanan kurir-001. Akibatnya, data pemetaan dipindahkan dari node 102 ke node 123, sementara alamat IP kurir (192.168.1.10) tidak mengalami perubahan karena modifikasi hanya berdampak pada node pengelolanya. Di sisi lain, pemetaan kurir-002 tidak terpengaruh dan tetap berada di bawah tanggung jawab node Bandung (ID hash 40) karena statusnya sebagai successor yang valid.

    ![Bukti Output Program](bukti/output_program_node_keluar_ring.png)

    Berdasarkan hasil simulasi, mekanisme leave() berhasil memindahkan mapping dari node yang keluar ke successor baru. Hal ini menunjukkan bahwa pembagian tanggung jawab dalam Chord DHT dapat menyesuaikan perubahan topologi tanpa mengubah informasi alamat IP kurir.
## Struktur Submission

```
tugas-06-penamaan-dht/
├── README.md      # Analisis + diagram ring
├── JURNAL.md
├── src/
│   └── chord_simulation.py
└── bukti/          # Output program (screenshot/log) untuk skenario join & leave
```

## Rubrik Penilaian (Tugas 6)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi lookup/join/leave benar | 35% | Consistent hashing & successor lookup sesuai aturan Chord |
| Bukti perubahan topologi (join/leave) | 25% | Output menunjukkan mapping berpindah dengan benar |
| Analisis kenapa DHT vs flat naming/DNS | 25% | Argumen spesifik ke kasus IP kurir dinamis, bukan definisi umum |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya konsep umum consistent hashing/Chord ke AI; **tidak boleh** meminta AI menuliskan isi `# TODO` di `src/chord_simulation.py` (`find_successor`, `join`, `leave`, dst). Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `README.md` wajib menelusuri manual (langkah demi langkah) bagaimana `lookup()` menemukan successor untuk salah satu ID Kurir contoh yang dipakai di `chord_simulation.py` — bukan cuma menempelkan output program.
