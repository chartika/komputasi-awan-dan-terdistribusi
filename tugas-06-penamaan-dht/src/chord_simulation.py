
"""
Tugas 6 - Simulasi Chord DHT
Single-process, tanpa jaringan sungguhan.

Memetakan ID Kurir ke IP melalui ring Chord.
Setiap node menyimpan mapping kurir yang menjadi tanggung jawabnya.
"""

import hashlib

M_BITS = 8
RING_SIZE = 2 ** M_BITS


def hash_id(key: str) -> int:
    """Mengubah ID node atau ID kurir menjadi hash 0..255."""
    digest = hashlib.sha1(key.encode()).digest()
    return int.from_bytes(digest, "big") % RING_SIZE


class ChordRing:
    def __init__(self):
        # ID node -> alamat IP node
        self.nodes: dict[int, str] = {}

        # ID node -> data kurir yang disimpan node tersebut
        # Format data: hash kurir -> (ID kurir, IP kurir)
        self.data: dict[int, dict[int, tuple[str, str]]] = {}

    def find_successor(self, key_hash: int) -> int:
        """Menemukan node dengan hash terkecil >= hash key."""
        if not self.nodes:
            raise ValueError("Ring belum memiliki node")

        node_ids = sorted(self.nodes.keys())

        for node_id in node_ids:
            if node_id >= key_hash:
                return node_id

        # Kembali ke node dengan ID terkecil jika melewati akhir ring.
        return node_ids[0]

    def join(self, node_name: str, node_ip: str):
        """Menambahkan node dan memindahkan data yang menjadi tanggung jawabnya."""
        node_id = hash_id(node_name)

        if node_id in self.nodes:
            print(f"[JOIN] Node '{node_name}' sudah terdaftar")
            return

        # Tambahkan node baru ke ring.
        self.nodes[node_id] = node_ip
        self.data[node_id] = {}

        print(
            f"[JOIN] Node '{node_name}' (id={node_id}) "
            f"bergabung, alamat {node_ip}"
        )

        # Periksa seluruh data pada node yang sudah ada.
        # Data dipindahkan jika successor-nya sekarang adalah node baru.
        for pemilik_lama in list(self.data.keys()):
            if pemilik_lama == node_id:
                continue

            for key_hash, (kurir_id, ip_kurir) in list(
                self.data[pemilik_lama].items()
            ):
                pemilik_baru = self.find_successor(key_hash)

                if pemilik_baru == node_id:
                    self.data[node_id][key_hash] = (
                        kurir_id, ip_kurir
                    )
                    del self.data[pemilik_lama][key_hash]

                    print(
                        f"[JOIN] Data {kurir_id} (hash={key_hash}) "
                        f"berpindah dari node {pemilik_lama} "
                        f"ke node {node_id}"
                    )

    def leave(self, node_name: str):
        """Mengeluarkan node dan memindahkan datanya ke successor baru."""
        node_id = hash_id(node_name)

        if node_id not in self.nodes:
            print(f"[LEAVE] Node '{node_name}' tidak ditemukan")
            return

        # Ambil data milik node sebelum node dihapus.
        data_node = list(self.data[node_id].items())

        # Hapus node dari ring dan penyimpanan aktifnya.
        del self.nodes[node_id]
        del self.data[node_id]

        print(
            f"[LEAVE] Node '{node_name}' (id={node_id}) "
            f"keluar dari ring"
        )

        if not self.nodes:
            if data_node:
                print(
                    "[LEAVE] Ring kosong. Data tidak dapat "
                    "dipindahkan karena tidak ada node penerima."
                )
            return

        # Pindahkan data ke successor berdasarkan topologi terbaru.
        for key_hash, (kurir_id, ip_kurir) in data_node:
            successor_baru = self.find_successor(key_hash)

            self.data[successor_baru][key_hash] = (
                kurir_id, ip_kurir
            )

            print(
                f"[LEAVE] Data {kurir_id} (hash={key_hash}) "
                f"berpindah ke node {successor_baru}"
            )

    def register_kurir(self, kurir_id: str, ip_kurir: str):
        """Menyimpan mapping pada node yang bertanggung jawab."""
        if not self.nodes:
            print("[REGISTER] Gagal: ring belum memiliki node")
            return

        key_hash = hash_id(kurir_id)
        node_id = self.find_successor(key_hash)

        # Simpan data secara nyata pada penyimpanan node pemilik.
        self.data[node_id][key_hash] = (kurir_id, ip_kurir)

        print(
            f"[REGISTER] {kurir_id} (hash={key_hash}) -> {ip_kurir}, "
            f"disimpan pada node {node_id}"
        )

    def lookup(self, kurir_id: str) -> str | None:
        """Mencari IP kurir pada node yang bertanggung jawab."""
        if not self.nodes:
            print("[LOOKUP] Ring kosong")
            return None

        key_hash = hash_id(kurir_id)
        node_id = self.find_successor(key_hash)

        # Pencarian dilakukan pada penyimpanan node pemilik.
        data_kurir = self.data[node_id].get(key_hash)

        if data_kurir is not None and data_kurir[0] == kurir_id:
            print(
                f"[LOOKUP] {kurir_id} -> {data_kurir[1]} "
                f"(penanggung jawab node {node_id})"
            )
            return data_kurir[1]

        print(f"[LOOKUP] {kurir_id} tidak ditemukan")
        return None

    def tampilkan_ring(self):
        """Menampilkan urutan node dan data yang disimpan."""
        print("\n--- Ring dan penyimpanan data ---")

        if not self.nodes:
            print("Ring kosong")
            return

        node_ids = sorted(self.nodes.keys())

        for node_id in node_ids:
            print(
                f"Node {node_id} ({self.nodes[node_id]}) "
                f"-> data: "
                f"{[item[0] for item in self.data[node_id].values()]}"
            )

        print("Urutan ring:", " -> ".join(map(str, node_ids)),
              "-> kembali ke", node_ids[0])


def main():
    ring = ChordRing()

    # 1. Empat node awal bergabung.
    ring.join("node-jakarta-1", "10.0.0.1")
    ring.join("node-jakarta-2", "10.0.0.2")
    ring.join("node-bandung-1", "10.0.0.3")
    ring.join("node-surabaya-1", "10.0.0.4")

    ring.tampilkan_ring()

    # 2. Daftarkan tiga kurir.
    ring.register_kurir("kurir-001", "192.168.1.10")
    ring.register_kurir("kurir-002", "192.168.1.11")
    ring.register_kurir("kurir-003", "192.168.1.12")

    print("\n--- Lookup sebelum perubahan topologi ---")
    ring.lookup("kurir-001")
    ring.lookup("kurir-002")

    # 3. Cari ID kurir uji yang hash-nya berada pada rentang
    # yang akan diambil alih node baru dengan ID 123.
    kurir_uji = None

    for i in range(10000):
        kandidat = f"kurir-join-{i:03d}"

        if 102 < hash_id(kandidat) <= hash_id("node-medan-1"):
            kurir_uji = kandidat
            break

    if kurir_uji is not None:
        print("\n--- Persiapan uji perpindahan saat join ---")
        ring.register_kurir(kurir_uji, "192.168.1.20")

    # 4. Node baru bergabung.
    print("\n--- Node baru bergabung ---")
    ring.join("node-medan-1", "10.0.0.5")
    ring.tampilkan_ring()

    if kurir_uji is not None:
        ring.lookup(kurir_uji)

    ring.lookup("kurir-001")

    # 5. Node yang menyimpan kurir-001 keluar.
    print("\n--- Sebuah node keluar ---")
    ring.leave("node-jakarta-2")
    ring.tampilkan_ring()

    # 6. Pastikan mapping tetap dapat ditemukan setelah leave.
    print("\n--- Lookup setelah node keluar ---")
    ring.lookup("kurir-001")
    ring.lookup("kurir-002")
    ring.lookup("kurir-003")

    if kurir_uji is not None:
        ring.lookup(kurir_uji)


if __name__ == "__main__":
    main()