# Data barang di Toko ATK
barang = [
    {"nama": "Pensil", "harga": 5000, "stok": 10},
    {"nama": "Buku", "harga": 7500, "stok": 5},
    {"nama": "Penggaris", "harga": 12000, "stok": 4},
    {"nama": "Pulpen", "harga": 5500, "stok": 10},
    {"nama": "Buku Gambar", "harga": 4000, "stok": 7},
    {"nama": "Pensil Warna", "harga": 15000, "stok": 5},
]

def tampilkan_barang():
    print(f"{'Nama Barang':<20} {'Harga Satuan':<15} {'Stok':<5}")
    print("=" * 40)
    for item in barang:
        print(f"{item['nama']:<20} Rp. {item['harga']:<14} {item['stok']}")

def beli_barang():
    total_harga = 0
    pembelian = []  # List untuk menyimpan data barang yang dibeli

    while True:
        nama_barang = input("\nMasukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk mengakhiri): ")
        if nama_barang.lower() == 'selesai':
            break
        jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))

        # Mencari barang yang diminta
        barang_ditemukan = False
        for item in barang:
            if item['nama'].lower() == nama_barang.lower():
                barang_ditemukan = True
                if item['stok'] >= jumlah_barang:
                    harga_barang = item['harga'] * jumlah_barang  # Menghitung total harga untuk barang ini
                    total_harga += harga_barang  # Menambahkan ke total harga
                    item['stok'] -= jumlah_barang  # Mengurangi stok setelah transaksi berhasil
                    print(f"\nPembelian {jumlah_barang} {item['nama']} berhasil! Total harga: Rp. {harga_barang}")
                    print(f"Sisa stok {item['nama']}: {item['stok']}")
                    
                    # Menyimpan data pembelian
                    pembelian.append({"nama": item['nama'], "jumlah": jumlah_barang, "total_harga": harga_barang})
                    
                    # Memeriksa apakah stok barang habis
                    if item['stok'] == 0:
                        print(f"Stok {item['nama']} habis!")
                    
                    # Menampilkan kembali data barang setelah pembelian
                    tampilkan_barang()
                else:
                    print(f"\nStok tidak cukup untuk {item['nama']}! Stok tersedia: {item['stok']}")
                break

        if not barang_ditemukan:
            print("\nBarang tidak ditemukan!")

    return total_harga, pembelian

def tampilkan_pembelian(pembelian, total_harga):
    print("\nData barang yang telah dibeli:")
    print(f"{'Nama Barang':<20} {'Jumlah':<10} {'Total Harga':<15}")
    print("=" * 40)
    for item in pembelian:
        print(f"{item['nama']:<20} {item['jumlah']:<10} Rp. {item['total_harga']:<15}")
    print(f"\nTotal harga semua pembelian: Rp. {total_harga}")

# Menampilkan data barang awal
tampilkan_barang()

# Memulai proses pembelian
total_harga, pembelian = beli_barang()

# Menampilkan data pembelian
tampilkan_pembelian(pembelian,total_harga)