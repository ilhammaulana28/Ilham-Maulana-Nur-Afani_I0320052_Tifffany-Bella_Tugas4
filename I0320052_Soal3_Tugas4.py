print('Soal No. 3\n')
print('===Asumsi berat maks adalah 50 lbs===')  #Asumsi soal benar
x = 0.453592  #1 lbs atau 1 pound = 0.453592 kg
y = x * 50
print('Berat maks yang diizinkan adalah', y, 'kg')
#bagaimana jika berat lebih dari 110 kg
#bagaimana jika berat adalah 49 kg
p = 110
q = 49
print('Koper anda memiliki berat lebih dari berat maksimum?', p > y, '. Anda dilarang membawa beban berlebihan!')
print('Koper anda memiliki berat lebih dari berat maksimum?', q > y, '. Anda dilarang membawa beban berlebihan!')
print('Silahkan kurangi barang di koper anda!\n')

print('===Asumsi berat maks adalah 50 kg===')  #Asumsi soal salah
#beban maks adalah 50 kg
print('Beban maks yang diizinkan adalah 50 kg')
#apabila beban lebih dari 110 kg
print('Apabila berat koper anda > 110 kg maka berat koper anda melebihi berat maks = ', 110 > 50)
print('Apabila berat koper anda adalah 50 kg maka berat koper anda melebihi berat maks = ', 49 > 50)
berat_koper = int(input('Lebih detail, berapa berat koper anda?'))
if berat_koper > 50:
    print('Koper anda melebihi beban maks = ', berat_koper > 50)
    print('Silahkan mengurangi barang bawaan anda!')
else:
    print('Koper anda melebihi beban maks =', berat_koper > 50)
    print('Silahkan melanjutkan perjalanan anda\n')
input('Tekan enter untuk keluar..\n')
