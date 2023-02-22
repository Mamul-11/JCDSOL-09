listMobil = [
    {
        'code': 'Car01',
        'jenis': 'SUV',
        'merek': 'Fortuner',
        'keluar': 2012,
        'harga': 2300000,
        'stock': 4
    }, {
        'code': 'Car02',
        'jenis': 'MPV',
        'merek': 'Xpander',
        'keluar': 2021,
        'harga': 1600000,
        'stock': 8
    }, {
        'code': 'Car03',
        'jenis': 'sedan',
        'merek': 'JAZZ',
        'keluar': 2013,
        'harga': 1200000,
        'stock': 5
    }, {
        'code': 'Car04',
        'jenis': 'SUV',
        'merek': 'CR-V',
        'keluar': 2020,
        'harga': 1600000,
        'stock': 5
    }
]


cek_code = [listMobil[i]['code']
            for i in range(len(listMobil))]


def menu_see():
    while (True):
        print('\n|======== Menu Cek Data Mobil ========|')
        print('\n1. Menampilkan data mobil')
        print('2. Menampilkan data mobil berdasarkan kode')
        print('3. Kembali ke menu utama')
        input_see = input('Masukan angka menu hapus data mobil 1 atau 2:')
        if input_see == '1':
            if len(listMobil) == 0:
                print("\n>>>Data rental mobil tidak tersedia<<<")
            else:
                print('\nDaftar Sewa Mobil')
                print(
                    '| Code \t| Jenis \t| Merek \t| Keluaran \t| Harga/Hari \t| Stock\t|')

                for i in range(len(listMobil)):
                    print('| {} \t| {}   \t| {}  \t| {}  \t| {} \t| {} \t|'.format(
                        listMobil[i]['code'], listMobil[i]['jenis'], listMobil[i]['merek'],  listMobil[i]['keluar'], listMobil[i]['harga'], listMobil[i]['stock']))
        elif (input_see == '2'):
            if len(listMobil) == 0:
                print("\n>>>Data rental mobil tidak tersedia<<<")
            else:
                input_code_mobil = input(
                    'Masukan code mobil yang mau direntalkan :').capitalize()
                print(f'Data rental mobil dengan code : {input_code_mobil}')
                for i in range(len(listMobil)):
                    if (input_code_mobil == listMobil[i]['code']):
                        print(
                            '| Code\t | Jenis\t | Merek \t | Keluaran \t | Harga/Hari \t | Stock\t|')
                        print('| {}\t | {}\t | {}  \t| {}  \t | {} \t | {} \t |'.format(
                            listMobil[i]['code'], listMobil[i]['jenis'], listMobil[i]['merek'],  listMobil[i]['keluar'], listMobil[i]['harga'], listMobil[i]['stock']))

        elif (input_see == '3'):
            break
        else:
            print('\n\t>>>Mohon maaf angka yang anda masukan salah!<<<')


def menu_create():
    while True:
        print('\n|======== Menu Tambah Data Mobil ========|')
        print('\n1. Menambahkan data mobil')
        print('2. Kembali ke menu utama')
        input_create = input(
            'Masukan angka menu tambah data rebtal mobil 1-2 : ')
        if input_create == '1':
            input_add_code = input('Masukan code data Mobil : ').capitalize()
            if input_add_code in cek_code:
                print('\n\t>>>Mohon maaf code mobil tidak boleh sama!<<<')
            else:
                input_add_jenis = input('Masukan jenis mobil : ')
                input_add_merek = input('Masukan merek mobil : ')
                while True:
                    input_add_keluar = input('Masukan tahun keluaran mobil : ')
                    if ["input_add_keluar:%04d" % x for x in range(10000)]:
                        break
                input_add_harga = int(
                    int(input('Masukan Harga sewa mobil per harinya :')))
                while True:
                    input_add_stock = int(
                        int(input('Masukan stock mobil yang tersedia :')))
                    if [input_add_stock % x for x in range(40)]:
                        break

                while True:
                    conf_add = input('Apakah data akan disimpan? (Y/N) ')
                    if conf_add == 'Y' or conf_add == 'y' or conf_add == 'N' or conf_add == 'n':
                        break
                if conf_add == 'Y' or conf_add == 'y':
                    listMobil.append({
                        'code': input_add_code,
                        'jenis': input_add_jenis,
                        'merek':  input_add_merek,
                        'keluar': input_add_keluar,
                        'harga': input_add_harga,
                        'stock': input_add_stock
                    })
                    print('\n\t>>>Data rental mobil baru telah tersimpan<<<\n')
                elif conf_add == 'N' or conf_add == 'n':
                    print('\n\t>>>Data rental mobil tidak tersimpan<<<')

                print(
                    '| Code \t| Jenis \t| Merek \t| Keluaran \t| Harga/Hari \t| Stock\t|')
                for i in range(len(listMobil)):
                        print('| {} \t| {}   \t| {}  \t| {}  \t| {} \t| {} \t|'.format(
                        listMobil[i]['code'], listMobil[i]['jenis'], listMobil[i]['merek'],  listMobil[i]['keluar'], listMobil[i]['harga'], listMobil[i]['stock']))
        elif (input_create == '2'):
            break
        else:
            print('\n\t>>>Mohon maaf angka yang anda masukan salah!<<<')


print(menu_create())


def menu_update():
    print('\n|======== Menu Ubah Data Mobil ========|')
    print('\n1. Mengubah data mobil')
    print('2. Kembali ke menu utama')
    input_update = input('Masukan angka menu hapus data mobil 1 atau 2 :')
    if input_update == '1':
        input_code_update = ('Masukan Code data rental mobil : ')
        if input_code_update in cek_code:
            a = cek_code inde
    elif (input_update == '2'):
        main_utama()
    else:
        print('\n\t>>>Mohon maaf angka yang anda masukan salah!<<<')


def menu_del():
    while (True):
        print('\n|=========Menu Hapus Data Mobil=========|')
        print('\n1. Menghapus data mobil')
        print('2. Kembali ke menu utama')
        input_del = input('Masukan angka menu hapus data mobil 1 atau 2:')
        if input_del == '1':
            print('\nDaftar Sewa Mobil')
            print('| Code \t| Jenis \t| Merek \t| Keluaran \t| Harga/Hari \t| Stock\t|')
            for i in range(len(listMobil)):
                print('| {} \t| {}   \t| {}  \t| {}  \t| {} \t| {} \t|'.format(
                    listMobil[i]['code'], listMobil[i]['jenis'], listMobil[i]['merek'],  listMobil[i]['keluar'], listMobil[i]['harga'], listMobil[i]['stock']))

            input_del_code = input('Masukan code data mobil untuk dihapus : ')

            if input_del_code in cek_code:
                while (True):
                    conf_del = input(
                        'Apakah kontak siswa akan dihapus? (Y/N): ')
                    if conf_del == 'Y' or conf_del == 'y' or conf_del == 'n' or conf_del == 'N':
                        break

                if conf_del == 'Y' or conf_del == 'y':
                    for i in range(len(listMobil)):
                        if listMobil[i]['code'] == input_del_code:
                            del listMobil[i]
                            print('\n\t>>>Data Rental Mobil Berahil dihapus!!!<<<')
                            break
                    else:
                        print('>>>Mohon maaf data mobil tidak tersedian<<<')
                elif conf_del == 'N' or conf_del == 'n':
                    print('\n\t>>>Kontak tidak terhapus<<<')
            else:
                print('\n\t>>>Mohon maaf data mobil yang dicari tidak ada<<<')
        elif input_del == '2':
            break
        else:
            print('\n\t>>>Mohon maaf angka yang anda masukan salah!<<<')


# def main_utama():
#     while (True):
#         print('\n|=========Menu Laporan Daftar Mobil Rental Tahun 2022=========|')
#         print('\n1. Menampilkan data mobil rental')
#         print('2. Menambah data mobil rental')
#         print('3. Mengubah data mobil rental')
#         print('4. Menghapus data mobil rental')
#         print('5. Keluar dari program\n')
#         input_utama = input('Masukan angka Menu dari 1-5 :')
#         if (input_utama == '1'):
#             menu_see()
#         elif(input_utama == '2'):
#             menu_create()
#         elif(input_utama == '3'):
#             menu_update()
#         elif(input_utama == '4'):
#             menu_del()
#         elif(input_utama == '5'):
#             print('\n\tTerima kasih atas kerja kerasnya :):)')
#             break
#         else:
#             print('\n\t!!!!!Mohon maaf angka yang anda masukan salah!!!!!')

# main_utama()
