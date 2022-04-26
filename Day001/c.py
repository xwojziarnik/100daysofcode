"""Zwrot z inwestycji przy użyciu pętli while"""


n = 1           #liczba okresów w latach
pv = 1000       #wartość obecna
r = 0.04        #roczna stopa procentowa
fv = pv * (1+r)          #wartość przyszła

while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f"Wartość przyszła: {fv:.2f} PLN. Liczba lat: {n}")