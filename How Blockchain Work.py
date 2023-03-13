import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        # Membuat objek hash dengan algoritma SHA-256
        sha = hashlib.sha256()

        # Menggabungkan timestamp, data, dan previous hash ke dalam satu string
        block_content = str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8')

        # Menghitung hash dari string yang telah digabungkan
        sha.update(block_content)

        # Mengembalikan nilai hash dalam format hexadecimal
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        # Inisialisasi blockchain dengan genesis block
        self.chain = [Block("Genesis Block", "0")]

    def add_block(self, data):
        # Mencari blok terakhir di dalam blockchain
        previous_block = self.chain[-1]

        # Membuat blok baru dengan data yang diberikan dan hash blok sebelumnya
        new_block = Block(data, previous_block.hash)

        # Menambahkan blok baru ke dalam blockchain
        self.chain.append(new_block)

    def print_chain(self):
        # Meloop setiap blok dalam blockchain
        for block in self.chain:
            # Mencetak timestamp, data, previous hash, dan hash dari setiap blok
            print("Timestamp: ", block.timestamp)
            print("Data: ", block.data)
            print("Previous Hash: ", block.previous_hash)
            print("Hash: ", block.hash)
            print("\n")

if __name__ == "__main__":
    # Inisialisasi blockchain
    blockchain = Blockchain()

    while True:
        # Menampilkan menu kepada pengguna
        print("\n1. Tambahkan blok baru")
        print("2. Lihat blockchain")
        print("3. Penjelasan tentang blockchain")
        print("4. Keluar")

        # Meminta input dari pengguna
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            # Meminta data untuk blok baru dari pengguna
            data = input("Masukkan data untuk blok baru: ")

            # Menambahkan blok baru ke dalam blockchain
            blockchain.add_block(data)

            # Menampilkan pesan bahwa blok baru telah ditambahkan
            print("Blok baru berhasil ditambahkan!")
        elif choice == "2":
            # Mencetak seluruh isi dari blockchain
            blockchain.print_chain()
        elif choice == "3":
            # Menampilkan penjelasan tentang cara kerja blockchain
            print("Blockchain adalah sebuah database terdistribusi yang digunakan untuk mencatat transaksi. Setiap transaksi disimpan dalam sebuah blok, dan setiap blok dihubungkan satu sama lain dengan menggunakan hash dari blok sebelumnya. Dalam blockchain, setiap blok harus diverifikasi oleh jaringan sebelum ditambahkan ke dalam blockchain. Ini membuat blockchain aman dan transparan, karena setiap orang di jaringan dapat melihat seluruh isi dari blockchain.")
        elif choice == "4":
            print("Terimaksih")
            # Keluar dari program
           
