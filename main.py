sayi1 = int(input("başlangıç sayısı: "))
sayi2 = int(input("bitiş sayısı: "))
print(sayi1, "ile", sayi2, "arasındaki sayılar")
for sayi in range(sayi1, sayi2):
    if (sayi % 3 == 0 and sayi % 5 == 0):
        print("FizBuzz")

    elif sayi % 3 == 0:
        print("Fizz")

    elif sayi % 5 == 0:
        print("Buzz")
    else:
        print(sayi)
