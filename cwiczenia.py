import random
print('siema graczu będziesz mial test z matmy')

print ('jak sie nazywasz?')
imie =input()
print ('ile masz lat')

wiek=int(input())
if wiek <= 10:
    print('czesc')
else:
    print('dzen dobry')

numer = 0
bankpunktow = 0

while True:
    numer = numer + 1 
    o = random.randint(1, 20)
    p = random.randint(1, 20)
    wynik = p + o
    print ('ile to %s plus %s'%(p, o))
    rownanie = int(input())
    if rownanie == wynik:
        bankpunktow = bankpunktow + 1
        print ('udalo ci sie')
    else:
        bankpunktow = bankpunktow - 1
        print ('ups cos ci nie wyszło, ci sie uda:)')
    
    if numer > 10:
        break

print ("Hej %s! Twoj wynik to %s" % (imie, bankpunktow))
input()