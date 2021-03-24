print('EXERCISE 4.6')
#operator string

#pengecekan membership-not in
#bagian false
needle1 = 'lr'
haystack1 = 'Hello World'
print('Needle1  = "lr"', '\nHaystack = "Hello World"')

#pengecekan false
if needle1 in haystack1 :
    print(needle1, 'is present in string', haystack1, '\n')
else:
    print(needle1, 'not found in', haystack1, '\n')

#bagian true
needle = 'rl'
haystack = 'Hello World'
print('Needle  = "rl"', '\nHaystack = "Hello World"')
#pengecekan true
if needle in haystack :
    print(needle, 'is present in string', haystack,'\n')
else:
    print(needle, 'not found in', haystack, '\n')
