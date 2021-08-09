#Operasi dalam string

# 1 concate(menyambung string)
nama_depan = "Monkey"
nama_tengah = "D"
nama_belakang= "Luffy"

nama_lengkap = nama_depan + " " + nama_tengah +"'"+nama_belakang
print(nama_lengkap) 

# 2 Menghitung panjang string
panjang = len(nama_lengkap)
print('panjang : ', panjang, '\n')

# 3 Operator untuk string

# mencoba indexing
for i, char in enumerate(nama_lengkap) :
    print ('indeks ke - ',i,' adalah ',char )

# 4 Operator dalam bentuk method
data = "Roronoa Zoro"
jumlah = data.count('o')

print('\nJumlah char o adalah ', str(jumlah))
