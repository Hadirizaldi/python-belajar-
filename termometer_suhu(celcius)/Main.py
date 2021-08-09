## latihan konversi suhu

# konversi celcius
print ('\nPROGRAM KONVERSI TEMPERATUR\n')

celcius = float(input("Masukkan suhu dalam celcius : ", ))
reamur = celcius * (4/5)
fahrenheit = (celcius * (9/5)) + 32
kelvin = celcius + 273
print('---Hasil konversi suhu celcius---')
print('---------------------------------')
print(celcius,'konversi menjadi', reamur, 'reamur')
print(celcius,'konversi menjadi', fahrenheit, 'fahrenheit')
print(celcius,'konversi menjadi', kelvin, 'kelvin')