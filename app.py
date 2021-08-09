#percobaan
data_array = ['BWM',10,3.14,True,'Apple']
print(f'data dalam array = {data_array}')

print(f'\nMelihat setiap tipe data')
print(24*'-')
for i, kata in enumerate(data_array) :
    type_data = type(kata)
    print(f'indeks kata ke - {i} dengan isi "{kata}"\t tipe data = {type_data}')

three_numbers = (1,2,3)
print('\n',type(list(three_numbers)))3
