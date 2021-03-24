print('Soal No. 6\n')

# 4 adalah 100 dalam biner dan 11 adalah 1011. Apa keluaran dari operator bitwise berikut?
# a. 4|11  ?
# b. 4 >> 11 ?
# c. 4 ^ 11 ?
# d. ~4 ?
# e. 11 & 4 ?
print('Operation bitwise\n')
print('Operation bitwise (masing-masing bit) adalah salah satu operasi dengan basis bilangan biner atau binery')
print('operation bitwise juga menggunakan operasi logika seperti and (&), or (|), not (~), dan xor (^)')
print('Contohnya adalah sebagai berikut.')
a = 4  # binary = 00000100
b = 11  # binary = 00001011
print('Data adalah', a, '(binary = ', bin(a), ')', 'dan', b,  '(binary = ', bin(b), ')')
c = a | b
print('4 | 11     =', c,  '(binary = ', bin(c), ')')
d = a >> b
print('4 >> 11    =', d,  ' (binary = ', bin(d), ')')
e = a ^ b
print('4 ^ 11     =', e,  '(binary = ', bin(e), ')')
f = ~a
print('~4         =', f,  '(binary = ', bin(f), ')')
