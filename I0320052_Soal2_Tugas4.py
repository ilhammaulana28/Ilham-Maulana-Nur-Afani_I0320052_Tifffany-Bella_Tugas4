print('Soal No. 2\n')

print('Program Sederhana Operation Floor')
data1 = int(input('Masukkan bilangan bulat pertama anda : '))
data2 = int(input('Masukkan bilangan bulat kedua anda   : '))
print('\n==== Angka anda adalah', data1, 'dan', data2, '====\n')
op_floor = data1 // data2
x = str(input('Ketik "Yes" untuk menjalankan Operation floor :'))
if x == 'Yes':
    print('Hasil operation floor bilangan anda adalah', op_floor)
    input('Tekan enter untuk keluar..')
else:
    input('Tekan enter untuk keluar..')