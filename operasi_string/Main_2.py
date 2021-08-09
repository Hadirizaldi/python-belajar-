# merubah dalam bentuk uppercase 
salam = 'bro'
print(salam.upper())

# memisahkan komponen (split)
kalimat = 'halo selamat pagi mahasiswa baru'
list_kalimat = kalimat.split(' ')

print(list_kalimat, '\n')

for i, kata in enumerate(list_kalimat) :
    print ('urutan kata ke - '+ str(i+1),' adalah '+ kata)