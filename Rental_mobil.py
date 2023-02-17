listMobil = [{
    'id': 'Car01',
    'jenis' :'SUV',
    'merek' : 'Toyota Fortuner',
    'yype' : ' VNT',
    'keluar' : 2012,
    'hargaPerHari' : 2300000,
    'stock' : 4
},{
    'id': 'Car02',
    'jenis' :'MPV',
    'merek' : 'Mitsubishi Xpander',
    'type' : ' CVT',
    'keluar' : 2021,
    'harga' : 1600000,
    'stock' : 8
},{
    'id': 'Car03',
    'jenis' :'Hatchback',
    'merek' : 'Honda JAZZ',
    'type' : 'RT',
    'keluar' : 2013,
    'harga' : 1200000,
    'stock' : 5
},{
    'id': 'Car04',
    'jenis' :'SUV',
    'merek' : 'Honda CR-V',
    'type' : '1.5 S CVT',
    'keluar' : 2020,
    'harga' : 1600000,
    'stock' : 5
},{
    'id': 'Car05',
    'jenis' :'MPV',
    'merek' : 'Toyota Aplhard',
    'type' : 'Tranformer',
    'keluar' : 2022,
    'harga' : 2500000,
    'stock' : 2
}]

cast = []

def tampilDaftarMobil():
    print('Daftar Sewa Mobil')
    print('Idex\t| Jenis\t| Merek\t| Type\t| Tahun Keluaran\t| harga Per Harinya\t| Stock yang teersedia')
    for i in range(len(listMobil)) :
        print(i,f"{listMobil[i]['id']}\t| {listMobil[i]['jenis']}\t| {listMobil[i]['merek']}\t| {listMobil[i]['type']}\t| {listMobil[i]['keluar']}\t| {list[i]['harga']}\t| {list[i]['stock']}\t|")

while True :
    InputanNomor = input('''
        Selamat Datang di Pasar Buah

        List Menu :
        1. Menampilkan Daftar Buah
        2. Menambah Buah
        3. Menghapus Buah
        4. Membeli Buah
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(InputanNomor == 1) :
        tampilDaftarMobil()