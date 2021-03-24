print('Soal No. 5\n')
s = "Hey there! what should this string be?"  # panjang string ini harusnya 20
print('String soal : ', s)
print('Panjang dari s = %d' % len(s))

# huruf pertama "a" harusnya di indeks No. 8
print('Kemunculan pertama a = %s' % s.index("a"))
# jumlah huruf a harusnya 2
print('a muncul sebanyak %s kali' % s.count('a'))
# memotong string berdasarkan indeks
print('Lima karakter pertama adalah "%s"' % s[:5])  # start to 5
print('Lima karakter berikutnya adalah "%s"' % s[5:10])  # 5 to 10
print('Karakter ketiga belas adalah "%s"' % s[12])  # just number 12
print('Karakter dengan indeks ganjil adalah"%s"' % s[1::2])  # (0-based indexing)
print('Lima karakter terakhir adalah "%s"' % s[-5:])  # 5th from last to end

# konversikan ke upercase
print('String dalam huruf besar :%s' % s.upper())

# konversikan ke lowercase
print('String dalam huruf kecil : %s' % s.lower())

# cek bagaimana string itu dimulai
if s.startswith('Str'):
    print('String dimulai dengan "Str". Good!')

# cek bagaimana string itu diakhiri
if s.endswith('ome!'):
    print('String diakhiri dengan "ome!". Good!')

# pisahkan string menjadi tiga string yang terpisah
# masing-masing hanya berisi satu kata
# print('Pisahkan kata-kata dari string tersebut: %s' % s.split(''))

print('\nAnalisis jawaban')
# 1. Huruf a pertama seharusnya di indeks 8
new_s = s.replace('r', 'a', 1)
print('1. Saya memasukkan a pada karakter ke 8, belum sempurna tapi setidaknya karakter ke 8 tergantikan oleh a')
print('   Hasilnya adalah', '"', new_s, '"', 'dengan jumlah total indeks adalah', len(new_s))
# 2. 2 indeks pertama adalah "Str"
new_s1 = new_s.replace('Hey', 'Str', 1)
print('2. Mengganti 2 indeks pertama')
print('   Hasilnya adalah', '"', new_s1, '"', 'dengan jumlah total indeks adalah', len(new_s1))
# 3. indeks total harusnya 20
print('3. Total indeks string lama adalah', len(new_s1), 'berarti harus dipotong', len(new_s1) - 19)
print('   (karena pengindeksan dimulai dari 0)')
new_s2 = new_s1[:19]
print('   Hasilnya menjadi "', new_s2, '" dan total indeks menjadi', len(new_s2))
# 4. 4 indeks terakhir adalah "ome!"
indeks_terakhir = new_s1[15:19]
new_s3 = new_s2.replace(indeks_terakhir, 'ome!')
print('4. Mengganti 4 indeks terakhir')
print('   Hasilnya adalah', '"', new_s3, '"')
# 5. indeks a harusnya muncul 2 kali, berarti harus di cek di string terakhirnya, apakah sudah 2 kali.
print('5. Pengecekan kemunculan huruf a')
print('   Kemunculan huruf a masih %d' % new_s3.count('a'), 'kali')
new_s4 = new_s3.replace('what', 'wh t')
print('   Setelah dihilangkan 1 a menjadi "', new_s4, '"')
# 6. Analisis string terakhir hingga menjadi string yang bisa dipahami
print('6. Analisis string terakhir yaitu "', new_s4, '" sehingga bisa dipahami')
new_s_finale = 'String are awesome!'
print('   Hasil yang saya temukan adalah "', new_s_finale, '"')

print('\nAnalisis string baru dengan script soal')

print('1. Panjang dari s = %d (20 karakter termasuk spasi)' % len(new_s_finale))

# huruf pertama "a" harusnya di indeks No. 8
print('2. Kemunculan pertama a = %s (pengindeksan dimulai dari 0, jadi index 7 = karakter ke 8)' % new_s_finale.index("a"))
# jumlah huruf a harusnya 2
print('3. a muncul sebanyak %s kali' % new_s_finale.count('a'))
# memotong string berdasarkan indeks
print('4. Lima karakter pertama adalah "%s"' % new_s_finale[:5])  # start to 5
print('5. Lima karakter berikutnya adalah "%s"' % new_s_finale[5:10])  # 5 to 10
print('6. Karakter ketiga belas adalah "%s"' % new_s_finale[12])  # just number 12
print('7. Karakter dengan indeks ganjil adalah"%s"' % new_s_finale[1::2])  # (0-based indexing)
print('8. Lima karakter terakhir adalah "%s"' % new_s_finale[-5:])  # 5th from last to end

# konversikan ke upercase
print('9. String dalam huruf besar :%s' % new_s_finale.upper())

# konversikan ke lowercase
print('10. String dalam huruf kecil : %s' % new_s_finale.lower())

# cek bagaimana string itu dimulai
if s.startswith('Str'):
    print('11. String dimulai dengan "Str". Good!')

# cek bagaimana string itu diakhiri
if s.endswith('ome!'):
    print('12. String diakhiri dengan "ome!". Good!')

print('\nPemisahan string')
print('String baru adalah "', new_s_finale, '"')
print('Pisahkan kata-kata dari string tersebut : %s' % new_s_finale.split())

s_finale1 = new_s_finale[:6]
print('String 1 =', s_finale1)
s_finale2 = new_s_finale[7:10]
print('String 1 =', s_finale2)
s_finale3 = new_s_finale[11:]
print('String 1 =', s_finale3)

input('Program selesai, tekan enter untuk keluar...')
