modal = 100000000
laba = [modal * 0, modal * 0, modal * 1/100, modal * 2/100, modal * 5/100, modal * 6/100, modal * 5/100, modal * 3/100, modal * 4/100]
bulan = 0
sum = 0

for i in laba :
    sum = sum + i
    bulan += 1
    print ('laba bulan ke -', bulan, 'mendapat laba', i)
print ('keuntungan', bulan, 'bulan', sum)
    
