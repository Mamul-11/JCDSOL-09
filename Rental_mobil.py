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
            if len(listMobil) == 0:  # data jika kosong
                print("\n>>>Data rental mobil tidak tersedia<<<")
            else:
                print('\nDaftar Sewa Mobil')
                print(
                    '| Code\t | Jenis Mobil\t | Merek Mobil\t | Keluaran\t| Harga/Hari\t | Stock |\n')
                for i in range(len(listMobil)):  # membaca semua data
                    print('| {}\t | {}   \t | {}   \t |{}   \t | {}\t | {} |'.format(
                        listMobil[i]['code'], listMobil[i]['jenis'], listMobil[i]['merek'],  listMobil[i]['keluar'], listMobil[i]['harga'], listMobil[i]['stock']))
        elif (input_see == '2'):
            if len(listMobil) == 0:
                print("\n>>>Data rental mobil tidak tersedia<<<")
            else:
                see_code_mobil = input(
                    'Masukan code mobil yang mau direntalkan :').capitalize()
                print(f'Data rental mobil dengan code : {see_code_mobil}')
                for i in range(len(listMobil)):  # membaca semua data
                    if (see_code_mobil == listMobil[i]['code']):
                        print(
                            '| Code\t | Jenis Mobil\t | Merek Mobil\t | Keluaran\t | Harga/Hari\t | Stock |')
                        print('| {}\t | {}   \t | {}   \t| {}   \t | {}\t | {} |'.format(
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
            if input_add_code in cek_code:  # pengecekan code mbbil
                print('\n\t>>>Mohon maaf code mobil tidak boleh sama!<<<')
            else:
                input_add_jenis = input('Masukan jenis mobil : ').capitalize()
                input_add_merek = input('Masukan merek mobil : ').capitalize()
                while True:
                    input_add_keluar = int(
                        input('Masukan tahun keluaran mobil : '))
                    if input_add_keluar != int:
                        break
                input_add_harga = int(
                    input('Masukan Harga sewa mobil per harinya :'))
                while True:
                    input_add_stock = int(
                        input('Masukan stock mobil yang tersedia :'))
                    if ["input_add_stock:%04d" % x for x in range(40)]:
                        break

                while True:
                    # pemberian kepastian
                    conf_add = input(
                        'Apakah data akan disimpan? (Y/N)').upper()
                    if conf_add == 'Y' or conf_add == 'N':
                        break
                if conf_add == 'Y':
                    listMobil.append({  # fungsi untuk menambahkan data
                        'code': input_add_code,
                        'jenis': input_add_jenis,
                        'merek':  input_add_merek,
                        'keluar': input_add_keluar,
                        'harga': input_add_harga,
                        'stock': input_add_stock
                    })
                    print('\n\t>>>Data rental mobil baru telah tersimpan<<<\n')
                elif conf_add == 'N':
                    print('\n\t>>>Data rental mobil tidak tersimpan<<<')

                print(
                    '| Code \t| Jenis Mobil\t| Merek Mobil\t| Keluaran\t| Harga/Hari\t| Stock |')
                for i in range(len(listMobil)):  # membaca semua data
                    print('| {}\t| {}   \t| {}   \t| {}   \t| {}\t| {} |'.format(
                        listMobil[i]['code'], listMobil[i]['jenis'], listMobil[i]['merek'],  listMobil[i]['keluar'], listMobil[i]['harga'], listMobil[i]['stock']))
        elif (input_create == '2'):
            break
        else:
            print('\n\t>>>Mohon maaf angka yang anda masukan salah!<<<')


def menu_update():
    while (True):
        print('\n|======== Menu Ubah Data Mobil ========|')
        print('\n1. Mengubah data mobil')
        print('2. Kembali ke menu utama')
        input_update = input('Masukan angka menu ubah data mobil 1-2 : ')
        if (input_update == '1'):
            input_code_update = input(
                'Masukan Code data rental mobil : ').capitalize()
            if input_code_update in cek_code:  # cek code mobil
                i = cek_code.index(input_code_update)
                print(
                    '| Code\t | Jenis Mobil\t | Merek Mobil\t | Tahun Keluaran\t | Harga/Hari\t | Stock |')
                print('| {}\t | {}   \t | {}   \t| {}   \t | {}\t | {} |'.format(
                    listMobil[i]['code'],  listMobil[i]['jenis'],  listMobil[i]['merek'], listMobil[i]['keluar'], listMobil[1]['harga'], listMobil[i]['stock']))
                while (True):
                    conf_update = input(
                        f"Apakah anda yakin ingin mengubah data rental mobil dengan code {input_code_update}? (Y/N) : ").upper()
                    if conf_update == 'Y' or conf_update == 'N':
                        break
                if conf_update == 'Y':
                    while True:
                        print("\n|======== Pilih data yang ingin diubah ========|")
                        print("\n1.Tulis 'jenis' = Update jenis mobile ")
                        print("2. Tulis 'merek' = Update merek mobil")
                        print("3. Tulis 'keluar' = Update tahun keluaran mobil")
                        print("4. Tulis 'harga' = Update harga sewa mobil per hari")
                        print("5. Tulis 'stock' = Update stock mobil")
                        data_ubah = input(
                            'Masukan kolom keterangan yang ingin diubah: ')
                        if data_ubah == 'jenis' or data_ubah == 'merek' or data_ubah == 'keluar' or data_ubah == 'harga' or data_ubah == 'stock':
                            data_ubah_akhir = input(
                                f'Masukan {data_ubah} data rental mobil baru: ').capitalize()
                            while (True):
                                conf_ubah = input(
                                    'Apakah data akan diubah? (Y/N): ').upper()
                                if conf_ubah == 'Y' or conf_ubah == 'N':
                                    break
                            if conf_ubah == 'Y':
                                listMobil[i][data_ubah] = data_ubah_akhir
                                print('\n\t>>>Selamat data berhasil di ubah<<<')
                                break
                            elif conf_ubah == 'N':
                                print(
                                    '\n\t>>>Mohon maaf data tidak jadi di ubah<<<')
                                break
                            else:
                                print('\n\t>>>Mohon maaf input anda salah!<<<')
                                break
                elif conf_update == 'N':
                    print('\n\t>>>Mohon maaf angka yang anda masukan salah!<<<')
            else:
                print('\n\t>>>Mohon maaf data rental mobil tidak ada !<<<')
        elif (input_update == '2'):
            break
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
            print(
                '| Code\t| Jenis Mobil\t| Merek Mobil\t| Keluaran\t| Harga/Hari\t| Stock |')
            for i in range(len(listMobil)):
                print('| {}\t| {}   \t| {}   \t| {}   \t| {}\t| {} |'.format(
                    listMobil[i]['code'], listMobil[i]['jenis'], listMobil[i]['merek'],  listMobil[i]['keluar'], listMobil[i]['harga'], listMobil[i]['stock']))

            input_del_code = input(
                'Masukan code data mobil untuk dihapus : ').capitalize()
            cek_code_del = [
                i for i in listMobil if i['code'] == input_del_code]
            if len(cek_code_del) != 0:
                while (True):
                    print("")
                    print(
                        '| Code\t| Jenis Mobil\t| Merek Mobil\t| Keluaran\t| Harga/Hari\t| Stock |')
                    print(
                        f"|{cek_code_del[0]['code']}\t| {cek_code_del[0]['jenis']}   \t| {cek_code_del[0]['merek']}   \t| {cek_code_del[0]['keluar']}   \t|{cek_code_del[0]['harga']}\t| {cek_code_del[0]['stock']} |")
                    conf_del = input(
                        "Apakah data rental mobil ingin dihapus? (Y/N): ").upper()
                    if conf_del == 'Y':
                        listMobil.remove(cek_code_del[0])
                        print('\n\t>>>Data Rental Mobil Berhasil dihapus!!!<<<')
                    elif conf_del == 'N':
                        print('\n\t>>>Mohon maaf data tidak terhapus<<<')
                    else:
                        print('\n\t>>>Mohon maaf salah input<<<')
                        continue
                    break
            else:
                print('\n\t>>>Mohon maaf data mobil yang dicari tidak ada<<<')
        elif input_del == '2':
            break
        else:
            print('\n\t>>>Mohon maaf angka yang anda masukan salah!<<<')


while (True):
    print('\n|=========Menu Laporan Daftar Mobil Rental Tahun 2022=========|')
    print('\n1. Menampilkan data mobil rental')
    print('2. Menambah data mobil rental')
    print('3. Mengubah data mobil rental')
    print('4. Menghapus data mobil rental')
    print('5. Keluar dari program\n')
    input_utama = input('Masukan angka Menu dari 1-5 :')
    if (input_utama == '1'):
        menu_see()
    elif (input_utama == '2'):
        menu_create()
    elif (input_utama == '3'):
        menu_update()
    elif (input_utama == '4'):
        menu_del()
    elif (input_utama == '5'):
        print('\n\tTerima kasih atas kerja kerasnya :):)')
        break
    else:
        print('\n\t!!!!!Mohon maaf angka yang anda masukan salah!!!!!')


#
