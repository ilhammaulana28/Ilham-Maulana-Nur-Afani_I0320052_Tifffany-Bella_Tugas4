print('Soal No. 4\n')
#untuk mendaftar kursus online, siswa harus berusia min. 21 th
#telah lulus ujian kualifikasi
#berapa usia kamu?
#apakah anda sudah lulus ujian kualifikasi (Y/T)?
#respons pertanyaan program sbg berikut.
#1. Anda dapat mendaftar di kursus.
#2. Anda tidak dapat mendaftar di kursus.
print('Rencana pengujian kursus')
print('Syarat      : 1. Berusia minimal 21 tahun.')
print('              2. Telah lulus ujian kualifikasi.\n')
usia = int(input('Berapa usia kamu?'))
kualifikasi = str(input('Apakah anda sudah lulus ujian kualifikasi (Y/T)?'))
if kualifikasi == 'Y' and usia >=21:
    print('Anda dapat mendaftar di kursus.')
else:
    print('Anda tidak dapat mendaftar di kursus\n')
input('Tekan enter untuk keluar..')
