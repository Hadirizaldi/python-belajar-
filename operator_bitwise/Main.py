# membuat operator bitwise, operasi biner, operasi binary

print('\nPROGRAM KONVERSI BITWISE\n')
a = int(input('Masukkan angka pertama: '))
b = int(input('Masukkan angka kedua: '))

print ('\n======Konversi ke bit======')
print ('nilai a: ',a,' , binary: ', format(a,'08b'))
print ('nilai a: ',b,' , binary: ', format(b,'08b'))

# bitwise OR (|)
hasil = a | b
print ('\n======OR======')
print ('nilai a: ',a,' , binary: ', format(a,'08b'))
print ('nilai a: ',b,' , binary: ', format(b,'08b'))
print ('------------------------------------------(|)')
print ('nilai hasil: ',hasil,' , binary: ', format(hasil,'08b'))

# bitwise and (&)
hasil = a & b
print ('\n======AND======')
print ('nilai a: ',a,' , binary: ', format(a,'08b'))
print ('nilai a: ',b,' , binary: ', format(b,'08b'))
print ('------------------------------------------(&)')
print ('nilai hasil: ',hasil,' , binary: ', format(hasil,'08b'))