# Latihan untuk input user

print('Membuat luas Persegi panjang')
data_panjang = float(input('Masukkan panjang: '))
data_lebar = float(input('Masukkan lebar: '))

if (data_lebar <= 0 or data_panjang <= 0 ) :
    print('tidak boleh bernilai negatife')
else :
    luas = data_panjang * data_lebar
    print('luas = ', luas)