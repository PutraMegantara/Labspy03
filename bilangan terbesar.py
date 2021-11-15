n = 0
while True:
    a = int(input('masukan nilai : '))
    if n < a:
        n = a
    if a == 0 :
        break
print ('bilangan terbesar', n)
