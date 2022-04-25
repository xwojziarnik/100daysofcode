#Udemy excercises

#----------------------------------------
names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for name in names:
    if not isinstance(name, str):
        continue
    print(name)

#----------------------------------------

counter = 0
number = 2
liczby_pierwsze = []

while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        liczby_pierwsze.append(str(number))
        counter += 1
    number += 1

print(','.join(liczby_pierwsze))

#----------------------------------------

n = 1           #liczba okresów w latach
pv = 1000       #wartość obecna
r = 0.04        #roczna stopa procentowa
fv = pv * (1+r)          #wartość przyszła

while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f"Wartość przyszła: {fv:.2f} PLN. Liczba lat: {n}")

#----------------------------------------

max_iters = 10000
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

while previous_step_size> precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_prev - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1
print(f'Minimum lokalne w punkcie: {w_0:.2f}')

#----------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = int((start + end) // 2)
    if start > end:
        break
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

if flag:
    print('Znaleziono')
else:
    print('Nie znaleziono')

#----------------------------------------