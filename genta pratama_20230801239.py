class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"

class Pustaka:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def cari_buku_judul(self, judul):
        hasil = [buku for buku in self.daftar_buku if judul.lower() in buku.judul.lower()]
        return hasil

    def cari_buku_penulis(self, penulis):
        hasil = [buku for buku in self.daftar_buku if penulis.lower() in buku.penulis.lower()]
        return hasil

    def cari_buku_tahun(self, tahun):
        hasil = [buku for buku in self.daftar_buku if buku.tahun == tahun]
        return hasil

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Tidak ada buku dalam pustaka.")
        else:
            for buku in self.daftar_buku:
                print(buku)

def main():
    pustaka = Pustaka()
    
    while True:
        print("\nMenu:")
        print("1. Cari buku berdasarkan judul")
        print("2. Cari buku berdasarkan penulis")
        print("3. Cari buku berdasarkan tahun")
        print("4. Tampilkan buku")
        print("5. Input buku")
        print("6. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            hasil = pustaka.cari_buku_judul(judul)
            if hasil:
                for buku in hasil:
                    print(buku)
            else:
                print("Buku tidak ditemukan")
        
        elif pilihan == "2":
            penulis = input("Masukkan penulis buku: ")
            hasil = pustaka.cari_buku_penulis(penulis)
            if hasil:
                for buku in hasil:
                    print(buku)
            else:
                print("Buku tidak ditemukan")
        
        elif pilihan == "3":
            tahun = input("Masukkan tahun buku: ")
            try:
                tahun = int(tahun)
                hasil = pustaka.cari_buku_tahun(tahun)
                if hasil:
                    for buku in hasil:
                        print(buku)
                else:
                    print("Buku tidak ditemukan")
            except ValueError:
                print("Tahun harus berupa angka")
        
        elif pilihan == "4":
            pustaka.tampilkan_buku()
        
        elif pilihan == "5":
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan penulis buku: ")
            tahun = input("Masukkan tahun buku: ")
            try:
                tahun = int(tahun)
                buku = Buku(judul, penulis, tahun)
                pustaka.tambah_buku(buku)
                print("Buku berhasil ditambahkan!")
            except ValueError:
                print("Tahun harus berupa angka")
        
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
